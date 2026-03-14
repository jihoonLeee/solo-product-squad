---
name: setup
description: Set up the workspace, context docs, and metadata checks for solo-product-squad.
type: setup
user-invocable: true
---

# Setup

Use this skill when bootstrapping a new workspace or repairing the workflow scaffolding.

## Checklist
1. Confirm the active hierarchy: OMC -> solo-product-squad -> boricori-extension -> project overlay.
2. Confirm the canonical docs exist: `output/project-state.md`, `output/stage-handoff.md`, `output/context-index.md`.
3. Confirm the active stage artifacts and `contracts/` folders exist as needed.
4. Regenerate `agents/INDEX.md` with `python scripts/generate_agent_index.py`.
5. Run `python scripts/agent_index_lint.py`.
6. Run `python scripts/validate_artifacts.py --root . --stage all --allow-missing`.

## Notes
- Use `python scripts/context_pack.py --root . --stage <stage>` when you want a compact stage bundle.
- Keep `boricori-place/CLAUDE.md` as the only active project overlay document.
- Keep approval, evidence, and review artifacts explicit before release stages.
