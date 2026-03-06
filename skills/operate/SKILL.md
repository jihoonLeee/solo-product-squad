---
name: operate
description: 배포·모니터링·알림·백업·장애대응·운영 루틴 정의 및 실행 (output/ops/ 생성)
type: orchestrator
user-invocable: true
agent: ops-manager
---

# Operate

[operate 활성화 — 운영 단계]

## 목표

릴리즈 체크리스트 통과 후 배포, 모니터링, 알림, 백업, 장애대응, 운영 루틴을 정의하고
output/ops/ 하위에 runbook.md, alerts.yml, release-run.md를 생성함.

## 활성화 조건

- test 단계 완료 후 배포·운영 준비가 필요할 때
- 모니터링, 알림, 장애대응 절차를 정의해야 할 때
- 릴리즈 실행 체크리스트가 필요할 때

## 워크플로우

### Step 1: 선행 산출물 확인
output/qa/release-checklist.md가 존재하는지 확인.
없으면 사용자에게 /solo-product-squad:test 먼저 실행을 안내.

### Step 2: 운영 계획 수립 → Agent: ops-manager
- **TASK**: output/qa/release-checklist.md, output/backend/plan.md를 기반으로 output/ops/runbook.md, alerts.yml, release-run.md 생성
- **EXPECTED OUTCOME**: 단독 실행 가능한 배포 절차, 임계값 정의된 알림 규칙, 릴리즈 당일 체크리스트
- **MUST DO**: 3개 파일 모두 저장, 비밀값 실제 값 금지(키 이름만), 롤백 절차 포함
- **MUST NOT DO**: 비밀값(환경 변수 실제 값) 파일 저장 금지, 코드 수정 금지
- **CONTEXT**: output/qa/release-checklist.md, output/backend/plan.md, contracts/ 참조

### Step 3: 완료 보고
생성된 파일 경로와 핵심 내용을 사용자에게 요약 보고함.
전체 워크플로우 완료를 축하하고, 반복 사이클 안내:
- 새 기능 추가 → /solo-product-squad:plan 부터
- 긴급 버그 수정 → /solo-product-squad:build-frontend 또는 build-backend
- 새 제품 아이디어 → /solo-product-squad:validate 부터
