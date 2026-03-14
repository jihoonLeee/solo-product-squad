---
name: review
description: Cross-check test outputs, release risks, and remaining gaps, then write review findings.
type: orchestrator
user-invocable: true
agent: review-agent
---

# Review

Use this stage after `test` and before `operate`.
Its job is to decide whether the current implementation and evidence justify moving closer to release.

## Inputs

Read these first:

1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/qa/release-checklist.md`
4. `output/qa/execution-evidence.md`

Open `output/frontend/`, `output/backend/`, or `contracts/` only when the evidence points to a specific risk or mismatch.

## Workflow

1. Confirm that test artifacts exist and are current.
2. Compare release-checklist claims against execution evidence.
3. Check whether the implementation, contracts, and QA outputs tell the same story.
4. Write explicit findings in `output/review/findings.md`.
5. Hand off to `ops-manager` if the remaining risk is acceptable, otherwise hand back to the implementation owner.

## Output Contract

`output/review/findings.md` must include:

- what was found
- what was fixed
- why that judgment was made
- remaining risks
- next work

## Guardrails

- Do not declare release readiness without evidence.
- Do not hide high-risk issues behind a vague summary.
- Do not skip the findings document, even when the outcome is mostly positive.
