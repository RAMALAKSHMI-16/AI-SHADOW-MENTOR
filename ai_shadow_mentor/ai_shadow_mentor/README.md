# AI Shadow Mentor
AI career assistant: skill-gap analysis, personalized roadmap, job/salary insights, 24/7 chatbot, progress tracking.
**Team Dream Finder**

## Architecture
Frontend (HTML + Tailwind + JS) -> REST APIs (Flask) -> Services (analyzer, jobs, chatbot) -> MySQL (SQLAlchemy)

```
app.py            Flask app, pages, auth, REST endpoints
config.py         env-based config      models.py   User, Profile, Progress, ChatMessage
schema.sql        MySQL schema          data/       roles, skills, resources, salaries, FAQ
services/         analyzer.py (skill gap + roadmap), jobs.py (insights/live), chatbot.py
templates/ static/  UI pages, CSS
```

## Run
```bash
python -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                # edit DATABASE_URL
```
**MySQL:** run `mysql -u root -p < schema.sql`, set `DATABASE_URL=mysql+pymysql://user:pass@localhost:3306/ai_shadow_mentor`.
**No MySQL?** Leave `DATABASE_URL` empty and it uses SQLite automatically.
```bash
python app.py        # http://localhost:5000
```

## REST API
| Method | Endpoint | Purpose |
|---|---|---|
| POST | /api/analyze | `{role, skills, experience}` -> score, matched, missing |
| POST | /api/roadmap | phased plan + saved progress |
| POST | /api/progress | (login) save step done |
| GET | /api/jobs/insights?role=&experience= | salary, demand, companies, live jobs |
| GET | /api/jobs/trending | role demand ranking |
| POST | /api/chat | `{message}` -> `{reply}` |
| GET | /api/dashboard | (login) progress summary |

## How it works
1. User enters role + skills -> analyzer normalizes skills and computes weighted readiness vs. role requirements.
2. Missing skills are grouped into phases (Foundations, Core, Advanced) with free resources and a final portfolio phase.
3. Job insights come from the built-in dataset; add Adzuna keys in `.env` for live openings.
4. Chatbot detects intent (salary, skills, trends, projects, FAQ) and uses the logged-in user's profile for context.
5. Checkmarks and chat history persist in the database.

## Extending
Edit `data/knowledge.py` to add roles/skills. To plug in an LLM, replace `services/chatbot.reply()`.
