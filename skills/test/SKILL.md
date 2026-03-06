---
name: test
description: 테스트 전략·케이스·회귀·릴리즈 체크리스트 작성 (output/qa/ 생성)
type: orchestrator
user-invocable: true
agent: qa-engineer
---

# Test

[test 활성화 — QA 및 릴리즈 검증 단계]

## 목표

구현 완료된 프론트엔드·백엔드를 기반으로 테스트 전략과 케이스를 작성하고,
릴리즈 체크리스트를 통해 출시 준비 상태를 검증하여
output/qa/ 하위에 test-plan.md, test-cases.md, release-checklist.md를 생성함.

## 활성화 조건

- build-frontend 또는 build-backend 단계 완료 후 QA가 필요할 때
- 테스트 전략, 케이스, 릴리즈 체크리스트가 필요할 때

## 워크플로우

### Step 1: 선행 산출물 확인
contracts/openapi.yaml과 output/frontend/ 또는 output/backend/가 존재하는지 확인.
없으면 사용자에게 이전 단계 실행을 안내.

### Step 2: QA 전략 및 체크리스트 수립 → Agent: qa-engineer
- **TASK**: contracts/openapi.yaml, output/frontend/, output/backend/를 기반으로 output/qa/test-plan.md, test-cases.md, release-checklist.md 생성
- **EXPECTED OUTCOME**: 모든 In-Scope 기능을 커버하는 테스트 계획, Happy Path+예외 케이스, 보안 항목 포함 릴리즈 체크리스트
- **MUST DO**: 3개 파일 모두 저장, 보안 검토 항목(인증/인가, 입력 검증) 포함
- **MUST NOT DO**: 코드 수정 금지, 배포 실행 금지
- **CONTEXT**: contracts/openapi.yaml, output/frontend/, output/backend/ 참조

### Step 3: 완료 보고
생성된 파일 경로와 핵심 내용을 사용자에게 요약 보고함.
릴리즈 준비 상태를 요약하고 다음 단계(/solo-product-squad:operate)를 안내함.
