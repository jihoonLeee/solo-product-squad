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
- 필요 시 `frontend-design` 스킬을 함께 사용하여 비주얼 방향을 강화할 수 있음

## 컨텍스트 로드 순서

1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/context-index.md`
4. `output/mvp-scope.md`
5. design 단계에서는 구현 세부 문서나 `contracts/` 전체를 불필요하게 읽지 않음

## 워크플로우

### Step 1: 선행 산출물 확인
output/mvp-scope.md가 존재하는지 확인.
없으면 사용자에게 /solo-product-squad:plan 먼저 실행을 안내.

### Step 2: UX 설계 → Agent: ux-designer
- **TASK**: output/mvp-scope.md를 기반으로 output/ux/ia.md, wireframes.md, design-tokens.md 생성
- **EXPECTED OUTCOME**: 모든 In-Scope 기능을 커버하는 IA, 주요 화면 와이어프레임, 프론트 개발에 바로 사용 가능한 디자인 토큰
- **MUST DO**: 3개 파일 모두 저장, IA는 mvp-scope.md의 모든 In-Scope 기능 커버, 주요 사용자 흐름에 empty/loading/error 상태 포함
- **MUST NOT DO**: 픽셀 단위 비주얼 디자인 금지, 코드 포함 금지
- **CONTEXT**: `output/project-state.md`, `output/stage-handoff.md`, `output/context-index.md`, `output/mvp-scope.md`, `output/_template/design-tokens.md.template`

### Step 2.5: 상태 문서 및 품질 게이트
- `output/project-state.md`에 핵심 UX 결정과 열린 질문을 갱신함
- `output/stage-handoff.md`에 UX 결정 요약, 다음 단계 필수 읽기, 시각 설계 리스크를 갱신함
- `python scripts/validate_artifacts.py --root . --stage design` 검증을 통과해야 완료로 처리함

### Step 3: 비주얼 강화 판단 → Skill: frontend-design

아래 중 하나라도 해당하면 `frontend-design` 스킬 사용을 우선 검토:
- 사용자가 시각적 완성도, 브랜딩, 세련된 UI를 명시적으로 요구
- 랜딩페이지, 마케팅 페이지, 대시보드 등 첫인상과 신뢰가 중요한 화면이 핵심
- 현재 design-tokens가 지나치게 일반적이라 제품 차별화가 약함

사용 시 `output/ux/visual-direction.md`를 생성 또는 갱신하고, 필요하면 `design-tokens.md`를 보강함.

### Step 4: 완료 보고
생성된 파일 경로와 핵심 내용을 사용자에게 요약 보고함.
다음 단계(/solo-product-squad:architect)를 안내함.

## 품질 게이트

- 핵심 전환 흐름은 시작점, 완료 조건, 실패 지점이 보여야 함
- 와이어프레임은 모바일과 데스크톱 차이를 명시해야 함
- 접근성 또는 가독성에 영향 주는 중요한 UI 결정은 이유를 적어야 함
- design-tokens는 바로 구현 가능한 이름 체계로 작성되어야 함
- `visual-direction.md`가 있으면 design-tokens와 충돌하지 않아야 함