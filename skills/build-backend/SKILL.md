---
name: build-backend
description: Create the backend implementation plan, wait for approval, then implement and capture at least one verification result.
type: orchestrator
user-invocable: true
agent: backend-engineer
---

# Build Backend

## Goal

Turn the approved scope and architecture artifacts into a concrete backend plan and, after approval, backend code changes with recorded verification evidence.

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/mvp-scope.md`
4. `contracts/openapi.yaml`
5. `contracts/domain-model.md`
6. `output/backend/approval.md`
7. `boricori-place/CLAUDE.md` when project-specific rules matter

## Workflow
### Step 1: Confirm prerequisites
- If the contract files are missing, stop and route to `/solo-product-squad:architect`.
- If `output/backend/approval.md` is not `APPROVED`, create or update the plan only. Do not change code.

### Step 2: Plan the implementation
Produce:
- `output/backend/plan.md`
- `output/backend/migrations.md`

The plan must cover:
- service and API boundaries
- schema and migration intent
- authz, validation, and error handling
- acceptance criteria for each in-scope backend capability

### Step 3: Ask for approval
- Update `output/backend/approval.md`
- Explicitly request approval before code changes

### Step 4: Implement after approval
After approval only:
- implement the backend code
- run at least one verification command
- append or refresh evidence in `output/qa/execution-evidence.md`

Preferred verification path for JavaScript/TypeScript apps:
- `python scripts/quality_gate.py --root . --project-dir <project-dir>`

### Step 5: Update state docs
- refresh `output/project-state.md`
- refresh `output/stage-handoff.md`
- run `python scripts/validate_artifacts.py --root . --stage build-backend`

## Must Do
- keep authz, validation, and error handling explicit
- keep approval and evidence explicit
- hand off to `/solo-product-squad:test` after implementation

## Must Not Do
- do not implement before approval
- do not claim completion without at least one recorded verification result