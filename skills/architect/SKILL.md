---
name: architect
description: 도메인·DB·API 계약·에러코드·권한 규격을 contracts/ 단일 소스로 확정
type: orchestrator
user-invocable: true
agent: tech-architect
---

# Architect

[architect 활성화 — 기술 설계 단계]

## 목표

MVP 스코프와 UX 산출물을 기반으로 도메인 모델, DB 스키마, OpenAPI 계약,
에러 코드, 권한 규격을 contracts/ 단일 소스로 확정하여
프론트엔드·백엔드 계약 기반 개발을 가능하게 함.

## 활성화 조건

- plan 또는 design 단계 완료 후 기술 설계가 필요할 때
- API 계약, DB 스키마, 도메인 모델을 정의해야 할 때

## 컨텍스트 로드 순서

1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/mvp-scope.md`, `output/ux/ia.md`, `output/ux/wireframes.md`
4. 구현 세부는 계약이 필요한 경우에만 `contracts/`로 확장함

## 워크플로우

### Step 1: 선행 산출물 확인
output/mvp-scope.md가 존재하는지 확인.
output/ux/ia.md가 있으면 함께 참조.
없으면 사용자에게 /solo-product-squad:plan 먼저 실행을 안내.

### Step 2: 기술 설계 → Agent: tech-architect
- **TASK**: output/mvp-scope.md, output/ux/ 산출물을 기반으로 contracts/ 전체(openapi.yaml, domain-model.md, error-codes.md, authz.md) 생성
- **EXPECTED OUTCOME**: 모든 In-Scope 기능을 커버하는 OpenAPI 계약, 일관된 도메인 모델, 에러 코드 체계, 권한 규격
- **MUST DO**: 4개 파일 모두 생성, OpenAPI 3.x 형식 준수, 비밀값 파일 저장 금지, 입력 검증/인증/인가/주요 비기능 제약을 문서화
- **MUST NOT DO**: 코드 구현 포함 금지, 실제 API 키나 비밀번호 파일에 포함 금지
- **CONTEXT**: `output/project-state.md`, `output/stage-handoff.md`, `output/mvp-scope.md`, `output/ux/ia.md`, `output/ux/wireframes.md`

### Step 2.5: 상태 문서 및 품질 게이트
- `output/project-state.md`에 기술 설계 결정, 미해결 리스크, 다음 단계 입력을 갱신함
- `output/stage-handoff.md`에 architect 결과 요약, 다음 단계 필수 읽기, 잠긴 결정을 갱신함
- `python scripts/validate_artifacts.py --root . --stage architect` 검증을 통과해야 완료로 처리함

### Step 3: 완료 보고
생성된 파일 경로와 핵심 내용을 사용자에게 요약 보고함.
다음 단계(/solo-product-squad:build-frontend, /solo-product-squad:build-backend)를 안내함.

## 품질 게이트

- 모든 In-Scope 기능은 API 또는 명시적 비-API 처리 방식으로 추적 가능해야 함
- 주요 엔터티에는 생성/수정/삭제 규칙과 불변 조건이 있어야 함
- 에러 코드는 사용자 오류와 서버 오류를 구분해야 함
- 권한 규격은 최소 역할, 리소스, 액션 기준으로 빠짐없이 정의되어야 함