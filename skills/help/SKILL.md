---
name: help
description: Show the available solo-product-squad stages and how to use them.
type: utility
user-invocable: true
---

# Help

Use this skill when you need a quick map of the active workflow, context docs, and stage commands.

## Canonical Read Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/context-index.md`
4. `output/solo-product-squad-flow.md`
5. current stage artifacts

## Stage Commands
- `/solo-product-squad:validate`
- `/solo-product-squad:marketing`
- `/solo-product-squad:plan`
- `/solo-product-squad:design`
- `/solo-product-squad:frontend-design`
- `/solo-product-squad:architect`
- `/solo-product-squad:build-frontend`
- `/solo-product-squad:build-backend`
- `/solo-product-squad:security`
- `/solo-product-squad:test`
- `/solo-product-squad:review`
- `/solo-product-squad:operate`

## Practical Rules
- Start with the smallest useful set of docs.
- Prefer canonical docs over legacy references.
- Regenerate `agents/INDEX.md` after metadata edits with `python scripts/generate_agent_index.py`.
- Run `python scripts/agent_index_lint.py` and `python scripts/validate_artifacts.py --root . --stage all --allow-missing` after structural changes.
