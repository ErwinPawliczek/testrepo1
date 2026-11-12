# Agent rules

Every coding agent follows this checklist in order. Do not edit `PLAN.md`. Only the orchestrator (ErwinPawliczek) edits it.

## 1. Start-of-task

1. Run the sync loop in section 2.
2. Choose an open GitHub Issue with your workstream label (`ws-1-frontend`, `ws-2-backend`, or `ws-3-ml`) and `status:ready`. It must have no assignee.
3. Claim it before any code: assign the issue to your human's GitHub user, then comment `claimed`.
4. Stop if the issue is unassigned after that, or if it is assigned to someone else. Never start work on it.

## 2. During work

Before every new chunk of work:

1. `git pull origin main`
2. Re-read `AGENTS.md` and `contracts/`. Build against `contracts/`, not against another workstream's code.
3. Read the latest comment by ErwinPawliczek on the pinned issue titled `SYNC`. That issue is the orchestrator's status board; do not edit it.
4. Check open draft pull requests for overlap with this chunk.
5. If you are blocked, comment `BLOCKED: <reason>` on your issue, add the label `status:blocked`, and stop.
6. Stay in your workstream folder (`frontend/`, `backend/`, or `ml/`). A change to anything in `contracts/` is a separate pull request labelled `contract-change`.

## 3. Opening PR

1. On the first commit, open a draft pull request into `main`. The body must contain `Closes #<issue>` for the issue you claimed.
2. Keep pushing later commits to that same branch.
3. Mark the pull request Ready for review when the task is done.

## 4. After review

1. Answer orchestrator review comments by pushing fixes to the same branch. Do not open a new pull request for that feedback.
2. Never merge your own pull request.
3. Never force-push `main`.
