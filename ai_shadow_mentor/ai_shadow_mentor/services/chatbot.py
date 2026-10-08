"""24/7 AI mentor: intent matching over role knowledge + FAQ. Context-aware of the user's profile."""
import re
from data.knowledge import ROLES, FAQ, RESOURCES, PROJECTS
from services.analyzer import analyze, normalize
from services.jobs import insights

def _find_role(text):
    t = text.lower()
    for r in ROLES:
        if r.lower() in t: return r
    hints = {"ml":"Machine Learning Engineer","machine learning":"Machine Learning Engineer","data scien":"Data Scientist",
             "analyst":"Data Analyst","nlp":"AI/NLP Engineer","llm":"AI/NLP Engineer","web":"Full Stack Developer",
             "full stack":"Full Stack Developer","frontend":"Full Stack Developer","cloud":"Cloud Engineer","devops":"Cloud Engineer",
             "cyber":"Cybersecurity Analyst","security":"Cybersecurity Analyst"}
    for k, v in hints.items():
        if re.search(r"\b" + re.escape(k), t): return v
    return None

def reply(message, profile=None):
    t = message.lower().strip()
    if not t: return "Please type a question."
    role = _find_role(t) or (profile or {}).get("target_role")
    skills = (profile or {}).get("skills", "")

    if re.search(r"\b(salary|salaries|pay|lpa|earn|earning|earnings)\b", t):
        if role:
            i = insights(role); s = i["salary_lpa"]
            return f"{role} salaries (India, Fresher): {s['min']}-{s['max']} LPA. Growth: {i['growth']}. Top hirers: {', '.join(i['top_companies'][:4])}. See the Job Insights page for all levels."
        return "Which role? e.g. 'salary of data scientist'."
    if re.search(r"\b(skill|skills|learn|roadmap|gap|missing|need)\b", t) and role:
        a = analyze(role, skills)
        top = [m["skill"] for m in a["missing"][:4]]
        if top: return f"For {role} your readiness is {a['score']}%. Learn next: {', '.join(top)}. Generate the full plan on the Roadmap page."
        return f"You already cover all core {role} skills! Focus on projects and applications."
    if re.search(r"\b(demand|trend|trends|trending|job market|hiring)\b", t):
        if role:
            i = insights(role); return f"{role}: demand score {i['demand_score']}/100, growth {i['growth']}."
        top = sorted(ROLES.items(), key=lambda x: -x[1]["demand"])[:3]
        return "Hottest roles now: " + ", ".join(f"{k} ({v['demand']}/100)" for k, v in top) + "."
    if "project" in t and role:
        return f"Project ideas for {role}: " + "; ".join(PROJECTS[role]) + "."
    for s in {s for r in ROLES.values() for s in r["skills"]}:
        if s.lower() in t and s in RESOURCES:
            n, u, d = RESOURCES[s]; return f"To learn {s}: '{n}' ({d}) - {u}"
    for kws, ans in FAQ:
        if any(re.search(r"\b" + k, t) for k in kws): return ans
    if role: return f"{role} is a great path! Ask me about its skills, salary, demand or projects."
    return "I can help with career paths, skills, salaries, job trends, projects, resumes and interviews. Try: 'What skills do I need for Data Scientist?'"
