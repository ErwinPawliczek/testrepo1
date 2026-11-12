# TASKS — smoke test for the multi-agent workflow

Point your coding agent at this repo and tell it: **"Read AGENTS.md, PLAN.md and TASKS.md, then do your assigned task."**
Each task is tiny on purpose. The goal is to test the loop: branch, PR, orchestrator review, fix, merge.

## Rules (short version, full rules in AGENTS.md)
- Work on a new branch named `ws-<n>/<short-task-name>`.
- Only touch files in your workstream folder, plus your own row in `PLAN.md`.
- Open a PR into `main` using the PR template and include your Workstream ID.
- If the orchestrator requests changes on your PR, push the fixes to the same branch.

## T-1 — WS-1 frontend (`frontend/`) — @freakybongwater
Make `frontend/index.html`, one static page with no build step and no frameworks.
- Title: "Team Dashboard (test)"
- A "Check API" button that calls `GET http://localhost:8000/health` and shows the returned `status`, or "API offline" if the request fails.
- Done when: opening the file in a browser shows the page, and the button handles both cases.

## T-2 — WS-3 data/ML (`ml/`) — @nevinjosephtx
Make `ml/make_synthetic.py`, which generates a fake CSV for development use only.
- Writes `data/synthetic.csv` (the `data/` folder is gitignored) with 100 rows and columns `id` (int), `timestamp` (ISO datetime), and `value` (float).
- Use a fixed random seed and only the Python standard library.
- Print only aggregates (row count, mean of `value`), never raw rows.
- Make sure `.gitignore` covers `data/` and `*.csv`. If you add it, mention that in the PR.
- Done when: `python ml/make_synthetic.py` runs and prints the summary.

## Status
Update your row in `PLAN.md` when you start (in-progress) and when you open the PR (review).
