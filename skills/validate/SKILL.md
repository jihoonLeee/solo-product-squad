---
name: validate
description: 아이디어·수익 가설·검증 실험·KPI 정리 (output/idea-brief.md, output/validation-plan.md 생성)
type: orchestrator
user-invocable: true
agent: founder-strategist
---

# Validate

[validate 활성화 — 아이디어 검증 단계]

## 목표

사용자의 아이디어를 수익 가능한 제품 가설로 구체화하고,
검증 실험과 KPI를 설계하여 output/idea-brief.md와 output/validation-plan.md를 생성함.

## 활성화 조건

- 새로운 수익화 아이디어를 검증하고 싶을 때
- 아이디어·수익 가설·검증 실험·KPI 정리가 필요할 때
- 제품 개발 첫 번째 단계를 시작할 때

## 컨텍스트 로드 순서

1. `output/project-state.md`를 먼저 읽어 현재 단계와 열린 질문을 확인함
2. `output/stage-handoff.md`를 읽어 잠긴 결정과 주요 리스크를 확인함
3. `output/context-index.md`가 있으면 stage map만 확인함
4. 사용자 아이디어 설명만 추가로 읽고 바로 검증을 시작함
5. validate 단계에서는 불필요하게 `contracts/`, `output/ux/`, 구현 문서를 읽지 않음

## 워크플로우

### Step 1: 컨텍스트 수집
사용자에게 아이디어에 대한 정보를 수집함 (간단한 설명, 타깃 고객, 해결 문제).
이미 충분한 정보가 있으면 바로 Step 2로 진행.

### Step 2: 아이디어 검증 → Agent: founder-strategist
- **TASK**: 사용자의 아이디어를 분석하여 output/idea-brief.md와 output/validation-plan.md를 생성
- **EXPECTED OUTCOME**: 수익 가설, 타깃 고객, 검증 실험 목록, KPI가 담긴 두 파일
- **MUST DO**: output/idea-brief.md와 output/validation-plan.md 모두 저장, 모든 섹션 완성, 고객 세그먼트별 우선순위와 지불 의사 신호를 명시
- **MUST NOT DO**: 기술 구현 계획 포함 금지, 비밀값 파일 저장 금지
- **CONTEXT**: 사용자 아이디어 정보, `output/project-state.md`, `output/stage-handoff.md`, `output/context-index.md`, `output/_template/idea-brief.md.template`, `output/_template/validation-plan.md.template`

### Step 2.5: 상태 문서 및 품질 게이트
- `output/project-state.md`에 현재 단계, 핵심 가정, 다음 단계 입력을 갱신함
- `output/stage-handoff.md`에 validate 결과 요약, 다음 단계 필수 읽기, 검증되지 않은 가정을 갱신함
- `python scripts/validate_artifacts.py --root . --stage validate` 검증을 통과해야 완료로 처리함

### Step 3: 완료 보고
생성된 파일 경로와 핵심 내용을 사용자에게 요약 보고함.
다음 단계(/solo-product-squad:plan)를 안내함.

## 품질 게이트

- 아이디어 브리프에 "왜 지금 이 고객이 이 문제를 돈 내고 해결할지"가 문장으로 적혀 있어야 함
- validation-plan에는 실험별 기간, 예상 비용, 성공/실패 임계값이 있어야 함
- KPI는 측정 방법과 목표값이 숫자 또는 명확한 임계치로 정의되어 있어야 함
- 근거가 약한 가정은 "검증 전 가정"으로 분리 표시해야 함