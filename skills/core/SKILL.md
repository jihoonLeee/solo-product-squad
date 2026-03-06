---
name: core
description: solo-product-squad 전체 행동 규범 및 모호한 요청 라우팅
type: core
user-invocable: true
---

# Core

[solo-product-squad 활성화]

## 목표

solo-product-squad 플러그인의 전체 행동 규범을 정의하고,
모호한 사용자 요청을 적절한 스킬로 라우팅함.

## 행동 규범

- 모든 산출물은 파일로 저장하며, 각 단계의 출력이 다음 단계의 입력으로 재사용됨
- 비밀값(토큰/키/비밀번호)은 어떤 파일에도 저장하지 않음 (마스킹 처리)
- 기술 스택 기본값: Next.js 풀스택. Spring Boot 분리 조건은 mvp-scope.md를 따름
- 사용자 승인 없이 코드를 직접 반영하지 않음 (build-frontend, build-backend 단계)

## 활성화 조건

- 사용자 요청이 어느 스킬에 해당하는지 불명확할 때
- 여러 단계에 걸친 복합 요청일 때
- 플러그인 전체 워크플로우를 시작하려 할 때

## 라우팅 규칙

| 요청 키워드 | 라우팅 대상 |
|------------|------------|
| 아이디어, 수익, 가설, 검증, KPI | validate |
| MVP, 범위, 기능, 우선순위, 일정 | plan |
| IA, 와이어프레임, 디자인, UX | design |
| API, 스키마, 계약, 도메인, DB | architect |
| 프론트, 프론트엔드, UI, 화면 | build-frontend |
| 백엔드, API 구현, 서버, DB 구현 | build-backend |
| 테스트, QA, 릴리즈 체크 | test |
| 배포, 모니터링, 운영, 장애 | operate |
| 전체, 처음부터, 파이프라인 | core (전체 단계 안내) |
| 설치, 설정, setup | setup |
| 도움말, 명령어, 사용법 | help |

## 워크플로우

### Step 1: 요청 의도 분류
사용자 요청을 분석하여 위 라우팅 규칙에 따라 대상 스킬을 결정함.

### Step 2: 선행 산출물 확인
라우팅 대상 스킬이 필요로 하는 선행 산출물(output/, contracts/)이 존재하는지 확인함.
존재하지 않으면 사용자에게 선행 단계 실행을 안내함.

### Step 3: 스킬 라우팅
결정된 스킬로 요청을 전달함.
