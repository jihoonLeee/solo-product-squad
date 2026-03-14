---
name: plan
description: Lock the MVP boundary, priorities, and milestones.
type: orchestrator
user-invocable: true
agent: pm-scoper
---

# Plan

## Goal
Convert validation outputs into a clear MVP boundary with priorities, out-of-scope decisions, and near-term milestones.

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/idea-brief.md`
4. `output/validation-plan.md`

## Workflow
1. Clarify what is in scope, out of scope, and intentionally deferred.
2. Write `output/mvp-scope.md` with priorities, milestones, and acceptance criteria.
3. Keep the scope realistic for the current team and stack.
4. Update `output/project-state.md` and `output/stage-handoff.md`.

## Must Do
- Keep the scope disciplined.
- Make the next design and architecture steps obvious.
- Run `python scripts/validate_artifacts.py --root . --stage plan` before closing the stage.

## Must Not Do
- Do not implement features here.
- Do not smuggle speculative features into the MVP.
