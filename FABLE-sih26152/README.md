# FABLE - SIH26152: Social Media Analytics

Team FABLE — SIH26152 (Social Media Analytics), team ID P-2025-29-CD-042-AY26-27, vertical: Cloud & DevOps.

**Team:**
- AJ — Team Lead / Product + User Validation
- Charan — Analytics / Baseline + Evaluation
- Adiya — Research / UI-UX + Visualization
- Ashwin — Data / Backend + Integration

## What this is

A unified analytics dashboard: upload data (starting with CSV), get automatic
analysis (sentiment, topics, trends) and visualizations, plus a plain-English
overall insight. MVP focuses on Mode 2 (Data Analyst / CSV upload) first.

## Project structure

```
FABLE-sih26152/
├── frontend/          # plain HTML/CSS/JS (Adiya)
├── backend/
│   ├── main.py        # FastAPI app (Ashwin)
│   ├── modules/
│   │   ├── data_processing.py   # Ashwin
│   │   ├── analysis.py          # Charan
│   │   └── visualization.py     # Adiya
│   ├── requirements.txt
│   └── sample_data/   # test CSVs go here
└── docs/               # SIH slides, validation notes
```

## Setup (backend)

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to confirm it's running and test the
`/upload` endpoint directly.

## Setup (frontend)

No build step yet. Just open `frontend/index.html` in a browser, or serve it
with a simple local server:

```bash
cd frontend
python -m http.server 5500
```

Then visit http://127.0.0.1:5500.

## Current status

Step 1 only: `/upload` endpoint accepts a file and echoes back its name and
size. No real analysis yet — that's next. See `backend/modules/*.py` for
what each member builds next.
