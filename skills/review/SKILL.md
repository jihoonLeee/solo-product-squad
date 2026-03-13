---
name: review
description: OMC verifier/reviewer 기반 교차 검토 및 리스크 정리
type: orchestrator
user-invocable: true
agent: review-agent
---

# Review

[review 활성화 — 교차 검토 단계]

## 목표

test 단계 산출물과 구현 결과를 바탕으로 OMC의 verifier/reviewer 계층을 활용해
무엇을 발견했고, 무엇을 수정했고, 어떤 리스크가 남았는지 정리하여
output/review/findings.md를 생성함.

## 활성화 조건

- test 단계 완료 후 operate 단계 전에 최종 점검이 필요할 때
- 구현 결과를 verifier/reviewer 관점으로 다시 검토하고 싶을 때
- release-checklist가 READY이더라도 남은 리스크를 문서로 잠그고 싶을 때

## 컨텍스트 로드 순서

1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/qa/release-checklist.md`, `output/qa/execution-evidence.md`
4. 필요한 경우에만 `output/frontend/`, `output/backend/`, `contracts/`로 확장함

## 워크플로우

### Step 1: 선행 산출물 확인
output/qa/release-checklist.md와 output/qa/execution-evidence.md가 존재하는지 확인.
없으면 사용자에게 /solo-product-squad:test 먼저 실행을 안내.

### Step 2: 교차 검토 수행 → Agent: review-agent
- **TASK**: OMC verifier/reviewer를 활용하여 구현 결과, 실행 증거, 릴리즈 체크리스트를 교차 검토
- **EXPECTED OUTCOME**: 발견 내용, 수정 내용, 판단 이유, 남은 리스크, 다음 작업이 담긴 findings 문서
- **MUST DO**: output/review/findings.md 저장, 높은 우선순위 리스크는 별도 구분, 릴리즈 가능 여부를 명확히 서술
- **MUST NOT DO**: 증거 없는 완료 선언 금지, 미해결 고위험 리스크 은폐 금지
- **CONTEXT**: `output/project-state.md`, `output/stage-handoff.md`, `output/qa/`, `output/frontend/`, `output/backend/`, `contracts/`

### Step 2.5: 상태 문서 및 품질 게이트
- `output/project-state.md`에 review 결과와 남은 리스크를 갱신함
- `output/stage-handoff.md`에 review 결과 요약, operate 단계 필수 읽기, 남은 고위험 리스크를 갱신함
- `python scripts/validate_artifacts.py --root . --stage review` 검증을 통과해야 완료로 처리함

### Step 3: 완료 보고
생성된 findings 문서 경로와 핵심 리스크를 요약 보고함.
남은 고위험 이슈가 없으면 /solo-product-squad:operate를 안내함.

## 품질 게이트

- findings에는 아래 5개 섹션이 모두 있어야 함
  - 무엇을 발견했는가
  - 무엇을 수정했는가
  - 왜 그렇게 판단했는가
  - 남은 리스크
  - 다음 작업
- 열린 고위험 리스크가 있으면 operate 단계에서 실제 릴리즈 실행으로 간주하지 않음