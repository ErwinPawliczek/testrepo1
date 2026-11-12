# Agent rules

These rules apply to every coding agent on this repo (Cursor, Claude Code, Codex, and others).

1. Read `PLAN.md` first. It is the only shared plan.
2. Edit files only inside your workstream folder (`frontend/`, `backend/`, or `ml/`). The one exception: you may update your own row in the workstreams table in `PLAN.md`.
3. Never edit another workstream's row in `PLAN.md`.
4. Changing an interface contract (an API shape or data schema in `PLAN.md`) requires its own pull request labelled `contract-change`. Do not mix a contract change with other work.
5. Every pull request must name its workstream ID and task, and must update that workstream's `PLAN.md` row (status, current task, blockers).
6. Keep pull requests small.
7. Respond to orchestrator review comments by pushing fixes to the same branch. Do not open a follow-up pull request for review feedback.
8. Never force-push `main`.
