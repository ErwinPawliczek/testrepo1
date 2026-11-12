# CenterPoint Energy hackathon — team workspace

Shared repo for a three-person team at the CenterPoint Energy hackathon in Houston. Each teammate runs their own coding agent. An orchestrator bot reviews every pull request and keeps `PLAN.md` up to date.

## How the workflow runs

1. Claim a GitHub Issue (assign it to your human and comment `claimed`) before writing code. See `TASKS.md`.
2. Before each chunk of work, run `git pull origin main`, re-read `AGENTS.md` and `contracts/`, and read the latest orchestrator comment on the pinned `SYNC` issue.
3. On the first commit, open a draft pull request that says `Closes #<issue>`. Push follow-ups to the same branch, then mark it ready for review.
4. Build against `contracts/`. Do not edit `PLAN.md` (orchestrator only).

Agent rules are in `AGENTS.md`. Pull requests use `.github/pull_request_template.md`.
