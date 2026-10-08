"""Job-market insights: static dataset, optional live listings via Adzuna."""
import requests
from data.knowledge import ROLES

def insights(role, experience="Fresher"):
    r = ROLES[role]
    lo, hi = r["salary"].get(experience, r["salary"]["Fresher"])
    return {"role": role, "experience": experience, "salary_lpa": {"min": lo, "max": hi, "avg": round((lo+hi)/2, 1)},
            "salary_by_level": {k: {"min": v[0], "max": v[1]} for k, v in r["salary"].items()},
            "demand_score": r["demand"], "growth": r["growth"], "top_companies": r["companies"],
            "top_skills": [s for s, l in sorted(r["skills"].items(), key=lambda x: x[1])][:6]}

def trending():
    return sorted(({"role": k, "demand": v["demand"], "growth": v["growth"]} for k, v in ROLES.items()),
                  key=lambda x: -x["demand"])

def live_jobs(role, app_id, app_key, country="in", limit=6):
    """Fetch live listings from Adzuna; returns [] if keys missing or request fails (graceful fallback)."""
    if not (app_id and app_key): return []
    try:
        res = requests.get(f"https://api.adzuna.com/v1/api/jobs/{country}/search/1",
            params={"app_id": app_id, "app_key": app_key, "what": role, "results_per_page": limit}, timeout=6)
        res.raise_for_status()
        return [{"title": j.get("title"), "company": (j.get("company") or {}).get("display_name"),
                 "location": (j.get("location") or {}).get("display_name"), "url": j.get("redirect_url")}
                for j in res.json().get("results", [])]
    except Exception:
        return []
