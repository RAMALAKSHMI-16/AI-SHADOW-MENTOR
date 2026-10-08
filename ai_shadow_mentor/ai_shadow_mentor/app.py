"""AI Shadow Mentor - Flask backend (REST APIs + server-rendered pages)."""
from functools import wraps
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from config import Config
from models import db, User, Profile, Progress, ChatMessage
from data.knowledge import ROLES
from services import analyzer, jobs, chatbot

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()

def current_user():
    uid = session.get("uid")
    return db.session.get(User, uid) if uid else None

def login_required_api(f):
    @wraps(f)
    def w(*a, **k):
        if not current_user(): return jsonify(error="Login required"), 401
        return f(*a, **k)
    return w

@app.context_processor
def inject():
    return {"user": current_user(), "roles": list(ROLES)}

# ---------- Pages ----------
@app.route("/")
def home(): return render_template("index.html")
@app.route("/analyzer")
def analyzer_page(): return render_template("analyzer.html")
@app.route("/roadmap")
def roadmap_page(): return render_template("roadmap.html")
@app.route("/jobs")
def jobs_page(): return render_template("jobs.html")
@app.route("/chatbot")
def chatbot_page(): return render_template("chatbot.html")
@app.route("/about")
def about_page(): return render_template("about.html")

# ---------- Auth ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name, email, pw = (request.form.get(k, "").strip() for k in ("name", "email", "password"))
        if not (name and email and len(pw) >= 6):
            flash("Fill all fields (password min 6 chars).", "error")
        elif User.query.filter_by(email=email.lower()).first():
            flash("Email already registered.", "error")
        else:
            u = User(name=name, email=email.lower()); u.set_password(pw)
            db.session.add(u); db.session.commit()
            session["uid"] = u.id
            return redirect(url_for("home"))
    return render_template("auth.html", mode="register")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = User.query.filter_by(email=request.form.get("email", "").lower()).first()
        if u and u.check_password(request.form.get("password", "")):
            session["uid"] = u.id
            return redirect(url_for("home"))
        flash("Invalid email or password.", "error")
    return render_template("auth.html", mode="login")

@app.route("/logout")
def logout():
    session.clear(); return redirect(url_for("home"))

# ---------- REST APIs ----------
@app.get("/api/roles")
def api_roles(): return jsonify(list(ROLES))

@app.post("/api/analyze")
def api_analyze():
    d = request.get_json(force=True, silent=True) or {}
    try: result = analyzer.analyze(d.get("role"), d.get("skills", ""), d.get("experience", "Fresher"))
    except ValueError as e: return jsonify(error=str(e)), 400
    u = current_user()
    if u:
        p = Profile.query.filter_by(user_id=u.id).first() or Profile(user_id=u.id)
        p.target_role, p.skills, p.experience = d.get("role"), d.get("skills", ""), d.get("experience", "Fresher")
        db.session.add(p); db.session.commit()
    return jsonify(result)

@app.post("/api/roadmap")
def api_roadmap():
    d = request.get_json(force=True, silent=True) or {}
    try: rm = analyzer.roadmap(d.get("role"), d.get("skills", ""), d.get("experience", "Fresher"))
    except ValueError as e: return jsonify(error=str(e)), 400
    u = current_user()
    done = {}
    if u:
        done = {p.step_key: p.done for p in Progress.query.filter_by(user_id=u.id, role=d["role"]).all()}
    rm["done"] = done
    return jsonify(rm)

@app.post("/api/progress")
@login_required_api
def api_progress():
    d = request.get_json(force=True, silent=True) or {}
    u = current_user()
    row = Progress.query.filter_by(user_id=u.id, role=d.get("role"), step_key=d.get("step_key")).first() \
          or Progress(user_id=u.id, role=d.get("role"), step_key=d.get("step_key"))
    row.done = bool(d.get("done"))
    db.session.add(row); db.session.commit()
    return jsonify(ok=True)

@app.get("/api/jobs/insights")
def api_insights():
    role = request.args.get("role")
    if role not in ROLES: return jsonify(error="Unknown role"), 400
    exp = request.args.get("experience", "Fresher")
    out = jobs.insights(role, exp)
    out["live_jobs"] = jobs.live_jobs(role, app.config["ADZUNA_APP_ID"], app.config["ADZUNA_APP_KEY"])
    return jsonify(out)

@app.get("/api/jobs/trending")
def api_trending(): return jsonify(jobs.trending())

@app.post("/api/chat")
def api_chat():
    msg = (request.get_json(force=True, silent=True) or {}).get("message", "")[:500]
    u = current_user(); profile = None
    if u:
        p = Profile.query.filter_by(user_id=u.id).first()
        if p: profile = {"target_role": p.target_role, "skills": p.skills}
    ans = chatbot.reply(msg, profile)
    db.session.add_all([ChatMessage(user_id=u.id if u else None, sender="user", message=msg),
                        ChatMessage(user_id=u.id if u else None, sender="bot", message=ans)])
    db.session.commit()
    return jsonify(reply=ans)

@app.get("/api/dashboard")
@login_required_api
def api_dashboard():
    u = current_user()
    p = Profile.query.filter_by(user_id=u.id).first()
    if not p: return jsonify(profile=None)
    rm = analyzer.roadmap(p.target_role, p.skills, p.experience)
    keys = [s["key"] for ph in rm["phases"] for s in ph["steps"]]
    done = Progress.query.filter_by(user_id=u.id, role=p.target_role, done=True).filter(Progress.step_key.in_(keys)).count()
    return jsonify(profile={"role": p.target_role, "skills": p.skills, "experience": p.experience},
                   score=rm["analysis"]["score"], steps_total=len(keys), steps_done=done)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
