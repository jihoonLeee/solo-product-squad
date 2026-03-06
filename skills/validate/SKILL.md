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

## 워크플로우

### Step 1: 컨텍스트 수집
사용자에게 아이디어에 대한 정보를 수집함 (간단한 설명, 타깃 고객, 해결 문제).
이미 충분한 정보가 있으면 바로 Step 2로 진행.

### Step 2: 아이디어 검증 → Agent: founder-strategist
- **TASK**: 사용자의 아이디어를 분석하여 output/idea-brief.md와 output/validation-plan.md를 생성
- **EXPECTED OUTCOME**: 수익 가설, 타깃 고객, 검증 실험 목록, KPI가 담긴 두 파일
- **MUST DO**: output/idea-brief.md와 output/validation-plan.md 모두 저장, 모든 섹션 완성
- **MUST NOT DO**: 기술 구현 계획 포함 금지, 비밀값 파일 저장 금지
- **CONTEXT**: 사용자 아이디어 정보, output/ 디렉토리 기존 파일 참조

### Step 3: 완료 보고
생성된 파일 경로와 핵심 내용을 사용자에게 요약 보고함.
다음 단계(/solo-product-squad:plan)를 안내함.
