---
name: frontend-design
description: Create distinctive visual direction and production-ready UI styling guidance for web products. Use when the user asks for polished landing pages, branded UI, standout visual identity, refined styling, beautified interfaces, or high-fidelity frontend design before or during implementation.
---

# Frontend Design

Use this skill to raise the visual quality of the product without breaking the main workflow.

## Goal

Translate product context into a memorable visual direction that a frontend engineer can implement consistently.
Do not replace IA or product scope work. Refine the look, feel, tone, interaction style, and visual differentiation.

## Context Load Order

1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/context-index.md`
4. `output/mvp-scope.md`
5. `output/ux/ia.md`, `output/ux/wireframes.md`, `output/ux/design-tokens.md` only if present
6. Avoid loading implementation plans unless visual direction directly depends on them

## When To Apply

- User explicitly asks for high-quality UI, polished styling, landing page quality, branding, or visual refinement
- Conversion, trust, or memorability is important to the product
- `skills/design` or `skills/build-frontend` need a stronger visual point of view

## Inputs

- `output/project-state.md`
- `output/stage-handoff.md`
- `output/context-index.md`
- `output/mvp-scope.md`
- `output/ux/ia.md` if present
- `output/ux/wireframes.md` if present
- `output/ux/design-tokens.md` if present

## Outputs

### `output/ux/visual-direction.md`

Include:
- product tone and target emotional response
- one clear aesthetic direction with rationale
- typography strategy
- color strategy and contrast guidance
- spacing, shape, border, and surface rules
- motion principles
- examples of what to avoid
- page-level visual priorities for key screens
- `output/_template/visual-direction.md.template`를 기본 골격으로 사용할 수 있음

### `output/ux/design-tokens.md`

Refine existing tokens when needed so they reflect the visual direction.
Keep names implementation-friendly.

## Workflow

1. Read the minimal product scope and existing UX artifacts in the load order above.
2. Pick one strong aesthetic direction that fits the product and audience.
3. Explain why that direction helps trust, clarity, conversion, or memorability.
4. Write `output/ux/visual-direction.md`.
5. Update `output/ux/design-tokens.md` if the existing tokens are too generic or inconsistent.
6. Update `output/project-state.md` with the chosen visual direction and downstream implementation notes.
7. Update `output/stage-handoff.md` with the locked visual decisions and the minimum files the next stage should read.

## Quality Bar

- Avoid generic AI aesthetics and interchangeable dashboard styling
- Match visual intensity to product purpose; not every product needs maximalism
- Keep accessibility, contrast, and readability intact
- Make the direction specific enough that another agent can implement it consistently