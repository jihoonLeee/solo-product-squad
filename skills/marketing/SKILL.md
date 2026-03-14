---
name: marketing
description: Produce market, positioning, competitor, and GTM artifacts for the current product.
type: orchestrator
user-invocable: true
agent: marketing-analyst
---

# Marketing

## Goal
Turn the current product idea and scope into concrete market, positioning, competitor, and GTM outputs.

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/idea-brief.md`
4. `output/mvp-scope.md`
5. `boricori-place/CLAUDE.md` when project-specific market context matters

## Workflow
1. Clarify the target segment, positioning, and competitor frame.
2. Write `output/marketing/strategy.md`, `output/marketing/competitor-analysis.md`, and `output/marketing/gtm-plan.md`.
3. Keep recommendations tied to the current MVP rather than an imagined future product.
4. Update `output/project-state.md` and `output/stage-handoff.md`.

## Must Do
- Call out assumptions when evidence is weak.
- Keep outputs useful for validation and planning, not just branding.
- Run `python scripts/validate_artifacts.py --root . --stage marketing` if this stage is part of the active workflow.

## Must Not Do
- Do not run campaigns or invent unsupported market facts.
- Do not expand the MVP scope without routing back to planning.
