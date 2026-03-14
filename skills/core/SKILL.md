---
name: core
description: Core orchestration rules for solo-product-squad and its project extensions.
type: core
user-invocable: true
---

# Core

Use this skill as the top-level operating manual for `solo-product-squad`.
It defines hierarchy, context loading rules, stage ownership, and minimum quality gates.

## Hierarchy

- `OMC` is the top runtime orchestrator.
- `solo-product-squad` is the active workflow system.
- `boricori-extension` is a project extension layer, not a replacement workflow.
- `DMAP` is a design and improvement layer, not a runtime router.

## Required Context

Before doing substantial work, read these in order:

1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/context-index.md`
4. `output/solo-product-squad-flow.md`
5. Current stage artifacts
6. Immediate upstream artifacts

Open project overlay docs such as `boricori-place/CLAUDE.md` only when project-specific rules are needed.

## Stage System

| Stage | Owner | Purpose |
|---|---|---|
| `validate` | `founder-strategist` | clarify the problem, user, and validation plan |
| `marketing` | `marketing-analyst` | optional market, positioning, and GTM work |
| `plan` | `pm-scoper` | lock MVP scope, priorities, and milestones |
| `design` | `ux-designer` | define IA, flows, wireframes, and design tokens |
| `architect` | `tech-architect` | define contracts, domain rules, and authz |
| `build-frontend` | `frontend-engineer` | implement the frontend against UX and contracts |
| `build-backend` | `backend-engineer` | implement backend changes against contracts |
| `security` | `security-analyst` | optional security review and risk findings |
| `test` | `qa-engineer` | gather execution evidence and release gating data |
| `review` | `review-agent` | cross-check release readiness and remaining risk |
| `operate` | `ops-manager` | prepare runbooks, release ops, and monitoring |

## Operating Rules

- Read only the smallest useful set of docs before producing the first draft.
- Prefer canonical docs over bridge or legacy docs.
- Keep `output/project-state.md` and `output/stage-handoff.md` current when a stage ends.
- Use explicit handoffs rather than silently switching roles.
- Keep implementation decisions aligned with the current contracts and stage outputs.

## Gate Rules

- `build-frontend` and `build-backend` require approval docs marked `APPROVED`.
- `test` must refresh `output/qa/execution-evidence.md` and `output/qa/release-checklist.md`.
- `review` must produce `output/review/findings.md`.
- `operate` starts only after review findings and release evidence are explicit.
- Use `python scripts/validate_artifacts.py --root . --stage <stage>` to verify artifact completeness.

## Context Efficiency Rules

- Use `output/context-index.md` as the compact routing map.
- Use `python scripts/context_pack.py --root . --stage <stage>` when you want a minimal stage-specific bundle.
- Prefer generated agent metadata in `agents/INDEX.md` over scanning every agent folder manually.

## Metadata Maintenance

- After editing any agent Quick Index, run `python scripts/generate_agent_index.py`.
- Then run `python scripts/agent_index_lint.py`.
