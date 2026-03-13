---
name: test
description: Build the test plan, test cases, execution evidence, and release checklist for the current scope.
type: orchestrator
user-invocable: true
agent: qa-engineer
---

# Test

## Goal

Turn the current implementation and contract artifacts into a repeatable QA package:
- `output/qa/test-plan.md`
- `output/qa/test-cases.md`
- `output/qa/execution-evidence.md`
- `output/qa/release-checklist.md`

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/qa/verification-matrix.md`
4. `contracts/openapi.yaml`
5. `output/frontend/`
6. `output/backend/`
7. `boricori-place/CLAUDE.md` when project-specific rules matter

## Workflow
### Step 1: Confirm prerequisites
- Verify that contract and implementation artifacts exist.
- If not, route back to the missing stage.

### Step 2: Build the QA plan
Produce or refresh:
- `output/qa/test-plan.md`
- `output/qa/test-cases.md`

The cases must cover:
- happy path
- exception and edge cases
- auth/authz and validation checks
- release blockers

### Step 3: Capture automated evidence
For JavaScript/TypeScript apps, prefer:
- `python scripts/quality_gate.py --root . --project-dir <project-dir>`

This should refresh:
- `output/qa/execution-evidence.md`
- `output/qa/release-checklist.md`

### Step 4: Add manual evidence
If UI, API, or user-flow checks are run manually, record them in `output/qa/execution-evidence.md` and keep the release checklist in sync.

### Step 5: Update state docs
- refresh `output/project-state.md`
- refresh `output/stage-handoff.md`
- run `python scripts/validate_artifacts.py --root . --stage test`

## Must Do
- keep automated and manual evidence separate but adjacent
- leave release status as `BLOCKED` when evidence is incomplete
- hand off to `/solo-product-squad:review`

## Must Not Do
- do not mark release `READY` without execution evidence
- do not skip security-related test cases