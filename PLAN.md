# Plan

Single source of truth for this repo. Every coding agent reads this file before starting work. The orchestrator updates the changelog when a pull request merges.

## Goal

_Placeholder._ One or two sentences on what the team is building for the CenterPoint Energy hackathon (Houston).

## Architecture overview

_Placeholder._ Three workstreams share this repository and meet only at the interface contracts below.

- **WS-1 frontend** — UI in `frontend/`
- **WS-2 backend/API** — HTTP API in `backend/`
- **WS-3 data/ML** — data and models in `ml/`

## Interface contracts

API shapes and data schemas between workstreams. A change to any contract is its own pull request labelled `contract-change`.

### Example: health (WS-2, consumed by anyone)

```http
GET /health
200 application/json
{ "status": "ok" }
```

### Example: meter reading (WS-3 produces, WS-2 serves, WS-1 displays)

```text
MeterReading {
  id: string
  timestamp: string    # ISO-8601
  value: number
  unit: string         # e.g. "kWh"
}
```

Replace these examples with the real contracts before another workstream depends on them.

## Workstreams

| ID | Owner (person + agent) | Folder | Status | Current task | Blockers |
|----|------------------------|--------|--------|--------------|----------|
| WS-1 | Person A + agent (placeholder) | `frontend/` | todo | — | — |
| WS-2 | Person B + agent (placeholder) | `backend/` | todo | — | — |
| WS-3 | @nevinjosephtx + Claude Code | `ml/` | in-progress | T-2: `ml/make_synthetic.py` synthetic dev CSV | — |

Status is one of `todo`, `in-progress`, `review`, `done`. Only the owning workstream edits its row.

## Decisions log

| Date | Decision | Why |
|------|----------|-----|
| 2026-11-12 | One shared `PLAN.md`. Workstreams own `frontend/`, `backend/`, and `ml/`. Contract changes are separate pull requests labelled `contract-change`. | Three agents can work in parallel without overwriting each other. |

## Changelog

Append one line per merged pull request. Newest at the bottom.

- _No merged pull requests yet._
