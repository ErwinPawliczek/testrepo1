# Plan

Maintained by the orchestrator only. Agents: do not edit.

Goal, architecture, and workstream ownership live here. Task status lives on GitHub Issues and the pinned `SYNC` issue.

## Goal

_Placeholder._ One or two sentences on what the team is building for the CenterPoint Energy hackathon (Houston).

## Architecture

_Placeholder._ Three workstreams share this repository and meet at the contracts in `contracts/`.

- **WS-1 frontend** — UI in `frontend/`
- **WS-2 backend/API** — HTTP API in `backend/`
- **WS-3 data/ML** — data and models in `ml/`

Shared API shapes and data schemas live in `contracts/`. Agents build against those files. A change to anything in `contracts/` is its own pull request labelled `contract-change`.

## Workstreams

| ID | Owner (person + agent) | Folder | Issue label |
|----|------------------------|--------|-------------|
| WS-1 | Person A + agent (placeholder) | `frontend/` | `ws-1-frontend` |
| WS-2 | Person B + agent (placeholder) | `backend/` | `ws-2-backend` |
| WS-3 | @nevinjosephtx + Claude Code | `ml/` | `ws-3-ml` |

## Decisions log

| Date | Decision | Why |
|------|----------|-----|
| 2026-11-12 | One shared `PLAN.md`. Workstreams own `frontend/`, `backend/`, and `ml/`. Contract changes are separate pull requests labelled `contract-change`. | Three agents can work in parallel without overwriting each other. |
| 2026-11-12 | Synchronized workflow v2. GitHub Issues are the task queue. A pinned `SYNC` issue is the live status board. `PLAN.md` is edited only by the orchestrator. Contracts live in `contracts/`. Agents open a draft pull request on the first commit. | Per-row status in `PLAN.md` caused merge conflicts, and agents only saw each other's work at pull-request time. |
| 2026-11-12 | CI allows a `PLAN.md` edit only when the author is ErwinPawliczek and the pull request title starts with `orchestrator:` or the body contains `ORCH`. `ORCH` does not replace `Closes #N` for anyone else. | A workstream pull request on the orchestrator's GitHub account must not edit `PLAN.md`, and other agents must not skip the issue link by writing `ORCH`. |

## Changelog

Append one line per merged pull request. Newest at the bottom.

- #2 WS-3 synthetic dev CSV (`ml/make_synthetic.py`).
