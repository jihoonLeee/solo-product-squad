# Agent Index

## Purpose

Use this file as the compact registry for agent discovery.
Read this file first, then open only the target agent's `AGENT.md`, `agentcard.yaml`, and `tools.yaml`.

## Read Order

1. `agents/INDEX.md`
2. Target agent `AGENT.md`
3. Target agent `agentcard.yaml`
4. Target agent `tools.yaml`

## Registry

| Agent | Stage | Read First | Produces | Handoff |
|------|------|------------|----------|---------|
| founder-strategist | validate | `output/project-state.md`, `output/stage-handoff.md`, `user brief` | `output/idea-brief.md`, `output/validation-plan.md` | `pm-scoper` |
| marketing-analyst | marketing | `output/project-state.md`, `output/stage-handoff.md`, `output/idea-brief.md`, `output/mvp-scope.md` | `output/marketing/strategy.md`, `output/marketing/competitor-analysis.md`, `output/marketing/gtm-plan.md` | `founder-strategist`, `pm-scoper` |
| pm-scoper | plan | `output/project-state.md`, `output/stage-handoff.md`, `output/idea-brief.md`, `output/validation-plan.md` | `output/mvp-scope.md` | `ux-designer`, `tech-architect` |
| ux-designer | design | `output/project-state.md`, `output/stage-handoff.md`, `output/mvp-scope.md` | `output/ux/ia.md`, `output/ux/wireframes.md`, `output/ux/design-tokens.md` | `tech-architect`, `frontend-engineer` |
| tech-architect | architect | `output/project-state.md`, `output/stage-handoff.md`, `output/mvp-scope.md`, `output/ux/` | `contracts/openapi.yaml`, `contracts/domain-model.md`, `contracts/error-codes.md`, `contracts/authz.md` | `frontend-engineer`, `backend-engineer` |
| frontend-engineer | build-frontend | `output/project-state.md`, `output/stage-handoff.md`, `output/mvp-scope.md`, `output/ux/`, `contracts/openapi.yaml` | `output/frontend/structure.md`, `output/frontend/pages.md`, `production frontend code` | `qa-engineer` |
| backend-engineer | build-backend | `output/project-state.md`, `output/stage-handoff.md`, `output/mvp-scope.md`, `contracts/` | `output/backend/plan.md`, `output/backend/migrations.md`, `production backend code` | `qa-engineer` |
| security-analyst | security | `output/project-state.md`, `output/stage-handoff.md`, `contracts/openapi.yaml`, `contracts/authz.md`, `output/backend/plan.md` | `output/security/findings.md` | `qa-engineer` |
| qa-engineer | test | `output/project-state.md`, `output/stage-handoff.md`, `contracts/openapi.yaml`, `output/frontend/`, `output/backend/` | `output/qa/test-plan.md`, `output/qa/test-cases.md`, `output/qa/execution-evidence.md`, `output/qa/release-checklist.md` | `review-agent`, `ops-manager` |
| review-agent | review | `output/project-state.md`, `output/stage-handoff.md`, `output/qa/release-checklist.md`, `output/qa/execution-evidence.md` | `output/review/findings.md` | `ops-manager`, `frontend-engineer`, `backend-engineer` |
| ops-manager | operate | `output/project-state.md`, `output/stage-handoff.md`, `output/qa/release-checklist.md`, `output/review/findings.md`, `output/backend/plan.md` | `output/ops/runbook.md`, `output/ops/alerts.yml`, `output/ops/release-run.md` | `pm-scoper`, `qa-engineer`, `backend-engineer` |

## Rules

- Keep `agents/INDEX.md` generated from each agent's Quick Index.
- Keep each `AGENT.md` Quick Index to 5 lines or fewer.
- Use `python scripts/generate_agent_index.py` after editing agent metadata.
- Use `python scripts/agent_index_lint.py` to verify index and handoff consistency.
