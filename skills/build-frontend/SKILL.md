---
name: build-frontend
description: Create the frontend implementation plan, wait for approval, then implement and capture at least one verification result.
type: orchestrator
user-invocable: true
agent: frontend-engineer
---

# Build Frontend

## Goal

Turn the approved product scope, UX artifacts, and API contract into a concrete frontend plan and, after approval, frontend code changes with recorded verification evidence.

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/mvp-scope.md`
4. `output/ux/`
5. `contracts/openapi.yaml`
6. `output/frontend/approval.md`
7. `boricori-place/CLAUDE.md` when project-specific rules matter

## Workflow
### Step 1: Confirm prerequisites
- If `contracts/openapi.yaml` is missing, stop and route to `/solo-product-squad:architect`.
- If `output/frontend/approval.md` is not `APPROVED`, create or update the plan only. Do not change code.

### Step 2: Plan the implementation
Produce:
- `output/frontend/structure.md`
- `output/frontend/pages.md`

The plan must cover:
- page/component structure
- API integration points
- loading, empty, error, and permission states
- acceptance criteria for each in-scope surface

### Step 3: Ask for approval
- Update `output/frontend/approval.md`
- Explicitly request approval before code changes

### Step 4: Implement after approval
After approval only:
- implement the frontend code
- run at least one verification command
- append or refresh evidence in `output/qa/execution-evidence.md`

Preferred verification path for JavaScript/TypeScript apps:
- `python scripts/quality_gate.py --root . --project-dir <project-dir>`

### Step 5: Update state docs
- refresh `output/project-state.md`
- refresh `output/stage-handoff.md`
- run `python scripts/validate_artifacts.py --root . --stage build-frontend`

## Must Do
- obey project overlay rules in `boricori-place/CLAUDE.md`
- keep approval and evidence explicit
- hand off to `/solo-product-squad:test` after implementation

## Must Not Do
- do not implement before approval
- do not claim completion without at least one recorded verification result