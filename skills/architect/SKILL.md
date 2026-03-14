---
name: architect
description: Define contracts, domain rules, authz, and error models.
type: orchestrator
user-invocable: true
agent: tech-architect
---

# Architect

## Goal
Create the contract and domain artifacts that let frontend and backend implementation proceed with clear constraints.

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/mvp-scope.md`
4. `output/ux/`
5. existing `contracts/` only when you need to extend or revise them

## Workflow
1. Define or refresh `contracts/openapi.yaml`, `contracts/domain-model.md`, `contracts/error-codes.md`, and `contracts/authz.md`.
2. Keep API shape, domain rules, authorization, and error behavior explicit.
3. Resolve the main architecture risks before implementation starts.
4. Update `output/project-state.md` and `output/stage-handoff.md`.

## Must Do
- Keep `contracts/` as the single source of truth for technical behavior.
- Make authz, validation, and error handling explicit.
- Run `python scripts/validate_artifacts.py --root . --stage architect` before closing the stage.

## Must Not Do
- Do not ship production feature code here.
- Do not leave contract-breaking assumptions implicit.
