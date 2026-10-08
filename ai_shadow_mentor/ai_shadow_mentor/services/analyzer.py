"""Skill-gap analyzer + roadmap generator."""
import re
from data.knowledge import ROLES, RESOURCES, PROJECTS, LEVEL

ALIASES = {"ml":"Machine Learning","dl":"Deep Learning","tf":"TensorFlow/PyTorch","tensorflow":"TensorFlow/PyTorch",
  "pytorch":"TensorFlow/PyTorch","aws":"Cloud (AWS/GCP/Azure)","azure":"Cloud (AWS/GCP/Azure)","gcp":"Cloud (AWS/GCP/Azure)",
  "cloud":"Cloud (AWS/GCP/Azure)","pandas":"Pandas/NumPy","numpy":"Pandas/NumPy","spark":"Big Data (Spark)",
  "html":"HTML/CSS","css":"HTML/CSS","js":"JavaScript","node":"Node.js","nodejs":"Node.js","powerbi":"Power BI/Tableau",
  "power bi":"Power BI/Tableau","tableau":"Power BI/Tableau","llm":"LLMs & Prompting","llms":"LLMs & Prompting",
  "prompt engineering":"LLMs & Prompting","rest":"REST APIs","api":"APIs","k8s":"Kubernetes","viz":"Data Visualization",
  "visualization":"Data Visualization","stats":"Statistics","security":"Security Fundamentals","hacking":"Ethical Hacking"}

def normalize(raw):
    """'python, SQL, ml' -> set of canonical skill names."""
    canon = {s.lower(): s for r in ROLES.values() for s in r["skills"]}
    out = set()
    for tok in re.split(r"[,;\n/|]+", raw or ""):
        t = tok.strip().lower()
        if not t: continue
        if t in canon: out.add(canon[t])
        elif t in ALIASES: out.add(ALIASES[t])
        else:
            for k, v in canon.items():
                if t == k.split("/")[0].split(" (")[0].strip(): out.add(v)
    return out

def analyze(role, skills_raw, experience="Fresher"):
    if role not in ROLES: raise ValueError("Unknown role")
    req = ROLES[role]["skills"]
    have = normalize(skills_raw)
    matched = [s for s in req if s in have]
    missing = sorted([s for s in req if s not in have], key=lambda s: req[s])
    # weight: beginner skills count more toward readiness
    w = {1:3, 2:2, 3:1}
    total = sum(w[l] for l in req.values())
    got = sum(w[req[s]] for s in matched)
    score = round(100 * got / total)
    return {"role": role, "experience": experience, "score": score, "matched": matched,
            "missing": [{"skill": s, "level": LEVEL[req[s]], "priority": "High" if req[s]==1 else "Medium" if req[s]==2 else "Low"} for s in missing],
            "verdict": verdict(score)}

def verdict(s):
    if s >= 80: return "Job-ready! Polish projects and start applying."
    if s >= 50: return "Good foundation. Close the high-priority gaps next."
    if s >= 25: return "Early stage. Follow the roadmap step by step."
    return "Just starting. Begin with the fundamentals below."

def roadmap(role, skills_raw, experience="Fresher"):
    a = analyze(role, skills_raw, experience)
    req = ROLES[role]["skills"]
    phases, buckets = [], {1:[], 2:[], 3:[]}
    for m in a["missing"]:
        lvl = req[m["skill"]]
        title, url, dur = RESOURCES.get(m["skill"], ("Search official docs", "https://www.google.com/search?q="+m["skill"], "2 weeks"))
        buckets[lvl].append({"key": m["skill"], "skill": m["skill"], "resource": title, "url": url, "duration": dur})
    names = {1:"Phase 1 - Foundations", 2:"Phase 2 - Core Skills", 3:"Phase 3 - Advanced & Deployment"}
    for l in (1,2,3):
        if buckets[l]: phases.append({"name": names[l], "steps": buckets[l]})
    phases.append({"name": "Final Phase - Portfolio & Job Hunt", "steps": [
        {"key": "project-"+str(i), "skill": "Project", "resource": p, "url": "", "duration": "2-3 weeks"} for i, p in enumerate(PROJECTS[role])
    ] + [{"key":"resume","skill":"Resume","resource":"Build a 1-page resume + LinkedIn + GitHub","url":"","duration":"1 week"},
         {"key":"apply","skill":"Applications","resource":"Apply to 5 roles/week and do weekly mock interviews","url":"","duration":"ongoing"}]})
    weeks = sum(int(re.findall(r"\d+", s["duration"])[0]) for p in phases for s in p["steps"] if re.findall(r"\d+", s["duration"]))
    return {"analysis": a, "phases": phases, "estimated_weeks": weeks}
