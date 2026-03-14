---
name: validate
description: Clarify the idea, target user, validation assumptions, and success metrics.
type: orchestrator
user-invocable: true
agent: founder-strategist
---

# Validate

## Goal
Turn a rough idea into a clear problem statement, target user, business hypothesis, and validation plan before scope is locked.

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/context-index.md`
4. user brief

## Workflow
1. Clarify the user, problem, value hypothesis, and main business assumptions.
2. Write `output/idea-brief.md` and `output/validation-plan.md`.
3. Make KPIs, validation steps, and stop/go criteria explicit.
4. Update `output/project-state.md` and `output/stage-handoff.md`.

## Must Do
- Keep assumptions separate from validated facts.
- Make the riskiest unknown obvious.
- Run `python scripts/validate_artifacts.py --root . --stage validate` before closing the stage.

## Must Not Do
- Do not lock MVP scope here.
- Do not define architecture or start implementation.
