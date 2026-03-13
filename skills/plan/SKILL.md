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

## 컨텍스트 로드 순서

1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/idea-brief.md`, `output/validation-plan.md`
4. 충돌이나 공백이 있을 때만 레거시 기획 문서를 추가 로드함

## 워크플로우

### Step 1: 선행 산출물 확인
output/idea-brief.md와 output/validation-plan.md가 존재하는지 확인.
없으면 사용자에게 /solo-product-squad:validate 먼저 실행을 안내.

### Step 2: MVP 스코프 결정 → Agent: pm-scoper
- **TASK**: output/idea-brief.md와 output/validation-plan.md를 기반으로 output/mvp-scope.md 생성
- **EXPECTED OUTCOME**: In-Scope/Out-of-Scope 명확히 구분된 MVP 스코프, 우선순위, 기술 스택 결정, 일정
- **MUST DO**: In-Scope·Out-of-Scope·기술 스택 결정·마일스톤 모두 포함, 1인 기준 현실적 일정 수립, 각 In-Scope 기능에 완료 기준과 검증 목적 연결
- **MUST NOT DO**: 기술 구현 세부 사항 포함 금지, 검증되지 않은 기능 In-Scope 포함 금지
- **CONTEXT**: output/idea-brief.md, output/validation-plan.md 참조, `output/_template/mvp-scope.md.template` 활용 가능

### Step 2.5: 상태 문서 및 품질 게이트
- `output/project-state.md`에 현재 단계, 핵심 결정, 열린 질문, 다음 단계 입력을 갱신함
- `output/stage-handoff.md`에 plan 결과 요약, 다음 단계 필수 읽기, 잠긴 결정을 갱신함
- `python scripts/validate_artifacts.py --root . --stage plan` 검증을 통과해야 완료로 처리함

### Step 3: 완료 보고
생성된 파일 경로와 핵심 내용을 사용자에게 요약 보고함.
다음 단계(/solo-product-squad:design 또는 /solo-product-squad:architect)를 안내함.

## 품질 게이트

- 모든 In-Scope 기능은 수익 가설 또는 핵심 사용자 가치와 연결되어 있어야 함
- 각 기능에는 완료 기준(acceptance criteria) 또는 배제 사유가 있어야 함
- 일정에는 버퍼 또는 주요 리스크 대응이 포함되어야 함
- Out-of-Scope는 "왜 지금 안 하는지"가 적혀 있어야 함