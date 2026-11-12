# CenterPoint Energy hackathon — team workspace

Shared repo for a three-person team at the CenterPoint Energy hackathon in Houston. Each teammate runs their own coding agent. An orchestrator bot reviews every pull request and keeps `PLAN.md` up to date.

## How the workflow runs

1. Read `PLAN.md` before writing code. It is the single plan: goal, architecture, interface contracts, and your workstream row.
2. Work only in your folder: `frontend/` (WS-1), `backend/` (WS-2), or `ml/` (WS-3).
3. Open a small pull request that names the workstream ID and the task, and update only your own row in `PLAN.md`.
4. The orchestrator reviews the pull request. Push fixes to the same branch.
5. After merge, add one changelog line to `PLAN.md`.

Agent rules are in `AGENTS.md`. Pull requests use `.github/pull_request_template.md`.
