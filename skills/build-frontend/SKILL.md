---
name: build-frontend
description: API 계약 기반 프론트엔드 구현 계획 수립 → 사용자 승인 후 코드 반영
type: orchestrator
user-invocable: true
agent: frontend-engineer
---

# Build Frontend

[build-frontend 활성화 — 프론트엔드 구현 단계]

## 목표

contracts/openapi.yaml과 output/ux/ 산출물을 기반으로
프론트엔드 구현 계획을 먼저 수립하고, 사용자 승인 후 코드를 반영함.

## 활성화 조건

- architect 단계 완료 후 프론트엔드 구현이 필요할 때
- 프론트엔드 구현 계획 또는 코드 반영이 필요할 때

## 워크플로우

### Step 1: 선행 산출물 확인
contracts/openapi.yaml이 존재하는지 확인.
없으면 사용자에게 /solo-product-squad:architect 먼저 실행을 안내.

### Step 2: 구현 계획 수립 → Agent: frontend-engineer
- **TASK**: contracts/openapi.yaml, output/ux/, output/mvp-scope.md를 기반으로 output/frontend/structure.md, output/frontend/pages.md 생성 (코드 반영 없이 계획만)
- **EXPECTED OUTCOME**: 디렉토리 구조, 컴포넌트 목록, 페이지별 API 연동 계획이 담긴 두 파일
- **MUST DO**: 계획 파일 2개 저장, 기술 스택 명시, 모든 In-Scope 기능 커버
- **MUST NOT DO**: 이 단계에서 실제 코드 작성 금지 (계획만)
- **CONTEXT**: contracts/openapi.yaml, output/ux/, output/mvp-scope.md 참조

### Step 3: 사용자 승인 요청
생성된 계획(output/frontend/)을 요약하여 사용자에게 보고함.
**사용자 승인을 명시적으로 요청함** — 승인 없이 코드 반영 진행 금지.

### Step 4: 코드 반영 → Skill: oh-my-claudecode:ralph
사용자 승인 시에만 실행:
- **INTENT**: 확정된 output/frontend/ 구현 계획에 따라 프론트엔드 코드 반영
- **ARGS**: skills/build-frontend/assets/develop.md 템플릿, output/frontend/ 계획 파일들
- **RETURN**: 빌드 가능한 프론트엔드 코드 완성

### Step 5: 완료 보고
구현 완료된 파일 목록과 빌드 결과를 사용자에게 요약 보고함.
다음 단계(/solo-product-squad:test)를 안내함.
