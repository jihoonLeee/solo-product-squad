---
name: operate
description: Convert approved release evidence into release and operations artifacts.
type: orchestrator
user-invocable: true
agent: ops-manager
---

# Operate

## Goal

Turn review-approved release evidence into:
- `output/ops/runbook.md`
- `output/ops/alerts.yml`
- `output/ops/release-run.md`

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/qa/verification-matrix.md`
4. `output/qa/release-checklist.md`
5. `output/review/findings.md`
6. `output/backend/plan.md`

## Workflow
### Step 1: Confirm release gate status
- If `output/qa/release-checklist.md` is `BLOCKED`, you may draft operations artifacts but you must not present the release as ready.
- If review findings still contain unresolved high-risk items, keep the release blocked.

### Step 2: Draft the operations package
Create or refresh:
- runbook
- alert thresholds and channels
- release execution checklist

### Step 3: Keep evidence linked
- Reference the latest automated/manual evidence from `output/qa/execution-evidence.md`
- Reference the latest release decision from `output/qa/release-checklist.md`

### Step 4: Update state docs
- refresh `output/project-state.md`
- refresh `output/stage-handoff.md`
- run `python scripts/validate_artifacts.py --root . --stage operate`

## Must Do
- keep blocked vs ready explicit
- keep rollback, alerting, and ownership explicit

## Must Not Do
- do not claim release readiness when the checklist is blocked
- do not hide unresolved review risks