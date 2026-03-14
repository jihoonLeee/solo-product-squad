---
name: design
description: Create IA, flows, wireframes, and design tokens for the approved scope.
type: orchestrator
user-invocable: true
agent: ux-designer
---

# Design

## Goal
Translate the approved scope into information architecture, user flows, wireframes, and design tokens that implementation can follow.

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/context-index.md`
4. `output/mvp-scope.md`
5. `boricori-place/CLAUDE.md` when local UI rules matter

## Workflow
1. Define IA and the core user flows for every in-scope surface.
2. Write `output/ux/ia.md`, `output/ux/wireframes.md`, and `output/ux/design-tokens.md`.
3. Keep empty, loading, error, and permission states visible.
4. Use `/solo-product-squad:frontend-design` if stronger visual direction is needed.
5. Update `output/project-state.md` and `output/stage-handoff.md`.

## Must Do
- Keep outputs implementable rather than vague.
- Make accessibility and state coverage explicit.
- Run `python scripts/validate_artifacts.py --root . --stage design` before closing the stage.

## Must Not Do
- Do not write production code here.
- Do not redefine scope or contracts on your own.
