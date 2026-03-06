---
name: design
description: IA·와이어프레임·디자인 토큰 산출 (output/ux/ 생성)
type: orchestrator
user-invocable: true
agent: ux-designer
---

# Design

[design 활성화 — UX 설계 단계]

## 목표

MVP 스코프를 기반으로 정보 구조(IA), 와이어프레임, 디자인 토큰을 산출하여
output/ux/ 하위에 ia.md, wireframes.md, design-tokens.md를 생성함.

## 활성화 조건

- plan 단계 완료 후 UX 설계가 필요할 때
- IA, 와이어프레임, 디자인 토큰을 정의해야 할 때

## 워크플로우

### Step 1: 선행 산출물 확인
output/mvp-scope.md가 존재하는지 확인.
없으면 사용자에게 /solo-product-squad:plan 먼저 실행을 안내.

### Step 2: UX 설계 → Agent: ux-designer
- **TASK**: output/mvp-scope.md를 기반으로 output/ux/ia.md, wireframes.md, design-tokens.md 생성
- **EXPECTED OUTCOME**: 모든 In-Scope 기능을 커버하는 IA, 주요 화면 와이어프레임, 프론트 개발에 바로 사용 가능한 디자인 토큰
- **MUST DO**: 3개 파일 모두 저장, IA는 mvp-scope.md의 모든 In-Scope 기능 커버
- **MUST NOT DO**: 픽셀 단위 비주얼 디자인 금지, 코드 포함 금지
- **CONTEXT**: output/mvp-scope.md 참조

### Step 3: 완료 보고
생성된 파일 경로와 핵심 내용을 사용자에게 요약 보고함.
다음 단계(/solo-product-squad:architect)를 안내함.
