---
name: security
description: Review the implementation and contracts for release-impacting security risks.
type: orchestrator
user-invocable: true
agent: security-analyst
---

# Security

## Goal
Inspect the current contracts and implementation artifacts for practical security issues and record findings by severity.

## Load Order
1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `contracts/openapi.yaml`
4. `contracts/authz.md`
5. `output/backend/plan.md`
6. `boricori-place/CLAUDE.md` when project-specific security rules matter

## Workflow
1. Review authz, validation, secret handling, and common application risk patterns.
2. Write or refresh `output/security/findings.md` with severity, impact, and remediation guidance.
3. Keep release impact explicit and route serious issues back into QA and implementation.
4. Update `output/project-state.md` and `output/stage-handoff.md`.

## Must Do
- Keep findings concrete and actionable.
- Separate critical, high, medium, and low severity clearly.
- Run `python scripts/validate_artifacts.py --root . --stage security` if this stage is active for the release.

## Must Not Do
- Do not change production code directly.
- Do not hide or soften release-impacting risk.
