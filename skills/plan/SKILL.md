---
name: plan
description: MVP 범위·우선순위·일정 고정 (output/mvp-scope.md 생성)
type: orchestrator
user-invocable: true
agent: pm-scoper
---

# Plan

[plan 활성화 — MVP 스코프 결정 단계]

## 목표

검증된 아이디어와 가설을 기반으로 MVP 범위를 고정하고,
기능 우선순위와 일정을 수립하여 output/mvp-scope.md를 생성함.

## 활성화 조건

- validate 단계 완료 후 MVP 범위를 결정하고 싶을 때
- 기능 우선순위와 일정을 정리해야 할 때

## 워크플로우

### Step 1: 선행 산출물 확인
output/idea-brief.md와 output/validation-plan.md가 존재하는지 확인.
없으면 사용자에게 /solo-product-squad:validate 먼저 실행을 안내.

### Step 2: MVP 스코프 결정 → Agent: pm-scoper
- **TASK**: output/idea-brief.md와 output/validation-plan.md를 기반으로 output/mvp-scope.md 생성
- **EXPECTED OUTCOME**: In-Scope/Out-of-Scope 명확히 구분된 MVP 스코프, 우선순위, 기술 스택 결정, 일정
- **MUST DO**: In-Scope·Out-of-Scope·기술 스택 결정·마일스톤 모두 포함, 1인 기준 현실적 일정 수립
- **MUST NOT DO**: 기술 구현 세부 사항 포함 금지, 검증되지 않은 기능 In-Scope 포함 금지
- **CONTEXT**: output/idea-brief.md, output/validation-plan.md 참조

### Step 3: 완료 보고
생성된 파일 경로와 핵심 내용을 사용자에게 요약 보고함.
다음 단계(/solo-product-squad:design 또는 /solo-product-squad:architect)를 안내함.
