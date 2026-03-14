# solo-product-squad

> 1인 창업자·솔로 개발자를 위한 수익화 아이템 개발 표준 워크플로우 DMAP 플러그인

---

## 레이어 구조

solo-product-squad는 혼자서 아이디어→기획→디자인→설계→개발→테스트→운영까지
반복하며 수익화 아이템을 빠르게 만들 수 있도록 표준 워크플로우를 제공하는 DMAP 플러그인임.

3-레이어 구조에서 solo-product-squad가 담당하는 워크플로우와 에이전트:

- **OMC**: 최상위 오케스트레이터. 복잡한 멀티에이전트 태스크 조율, 에이전트 라우팅, verifier/reviewer 교차검토, 상태 추적 담당.
- **solo-product-squad**: 수익화 아이템 개발 표준 워크플로우. 각 단계의 전문 에이전트가 산출물을 넘기는 파이프라인 구조.
- **DMAP**: solo-product-squad를 비롯한 다양한 플러그인을 로드·관리하는 플러그인 런타임.

**주요 특징:**
- 8단계 워크플로우로 아이디어를 운영 중인 제품으로 전환
- 각 단계의 산출물이 다음 단계의 입력으로 재사용됨 (파이프라인 구조)
- 기술 스택 기본값: Next.js 풀스택 (Spring Boot 분리 조건 명시)
- 코드 반영 전 반드시 사용자 승인 요청 (build-frontend, build-backend)
- 비밀값 파일 저장 금지 원칙 적용
- 새 단계 시작 전 output/stage-handoff.md를 먼저 읽어 잠긴 결정과 컨텍스트 파악
- OMC의 verifier/reviewer를 활용하여 review 단계에서 최상위 품질 검증

## 에이전트 구성

| 에이전트 | 역할 | 티어 |
|---------|------|------|
| founder-strategist | 아이디어·수익 가설·검증 실험 설계 | HIGH |
| pm-scoper | MVP 범위·우선순위·일정 결정 | HIGH |
| ux-designer | IA·와이어프레임·디자인 토큰 산출 | MEDIUM |
| tech-architect | API 계약·DB 스키마·도메인 모델 확정 | HIGH |
| frontend-engineer | 프론트엔드 구현 계획 및 코드 반영 | MEDIUM |
| backend-engineer | 백엔드 구현 계획 및 코드 반영 | MEDIUM |
| qa-engineer | 테스트 전략·케이스·릴리즈 게이트 | MEDIUM |
| review-agent | OMC verifier/reviewer 기반 교차검토 및 출시 리스크 정리 | HIGH |
| ops-manager | 배포·모니터링·장애대응·운영 루틴 | MEDIUM |
| security-analyst | OWASP 기반 보안 취약점 분석·위협 모델링·수정 권고 | HIGH |
| marketing-analyst | 시장 분석·경쟁사 비교·GTM 전략·수익화 경로 수립 | HIGH |

---

## 설치

### 사전 요구사항

- Claude Code CLI 설치
- Node.js 18+ (context7 MCP용)

### 플러그인 설치

**방법 1: 마켓플레이스 — GitHub (권장)**

Adding marketplace...
SSH not configured, cloning via HTTPS: https://github.com/jihoo/solo-product-squad.git
Refreshing marketplace cache (timeout: 120s)…
Cloning repository (timeout: 120s): https://github.com/jihoo/solo-product-squad.git
HTTPS clone failed, retrying with SSH: git@github.com:jihoo/solo-product-squad.git
Refreshing marketplace cache (timeout: 120s)…
Cloning repository (timeout: 120s): git@github.com:jihoo/solo-product-squad.git
Installing plugin "solo-product-squad@solo-product-squad"...
✔ Successfully installed plugin: solo-product-squad@solo-product-squad (scope: user)
Installed plugins:

  ❯ dmap@unicorn
    Version: 1.1.9
    Scope: project
    Status: ✔ enabled

  ❯ oh-my-claudecode@omc
    Version: 4.7.1
    Scope: project
    Status: ✔ enabled

  ❯ solo-product-squad@solo-product-squad
    Version: 0.0.1
    Scope: user
    Status: ✔ enabled

**방법 2: 마켓플레이스 — 로컬**

Installing plugin "solo-product-squad@solo-product-squad"...
✔ Successfully installed plugin: solo-product-squad@solo-product-squad (scope: user)
Installed plugins:

  ❯ dmap@unicorn
    Version: 1.1.9
    Scope: project
    Status: ✔ enabled

  ❯ oh-my-claudecode@omc
    Version: 4.7.1
    Scope: project
    Status: ✔ enabled

  ❯ solo-product-squad@solo-product-squad
    Version: 0.0.1
    Scope: user
    Status: ✔ enabled

> **설치 후 setup 스킬 실행:**
> 

---

## 업그레이드

Updating marketplace: solo-product-squad...
Refreshing marketplace cache (timeout: 120s)…
Found stale directory, cleaning up and re-cloning…
Cloning repository (timeout: 120s): https://github.com/jihoonLeee/solo-product-squad.git
Clone complete, validating marketplace…
✔ Successfully updated marketplace: solo-product-squad
Installing plugin "solo-product-squad@solo-product-squad"...
✔ Successfully installed plugin: solo-product-squad@solo-product-squad (scope: user)

---

## 사용법

### 표준 워크플로우



보조 스킬 (언제든 독립 실행 가능):


### 슬래시 명령

| 명령 | 설명 | 주요 산출물 |
|------|------|------------|
| /solo-product-squad:validate | 아이디어·수익 가설·검증 실험·KPI 정리 | output/idea-brief.md, output/validation-plan.md |
| /solo-product-squad:plan | MVP 범위·우선순위·일정 고정 | output/mvp-scope.md |
| /solo-product-squad:design | IA·와이어프레임·디자인 토큰 산출 | output/ux/ |
| /solo-product-squad:architect | API 계약·DB 스키마·도메인 모델 확정 | contracts/ |
| /solo-product-squad:build-frontend | 프론트엔드 구현 계획 → 승인 → 코드 | output/frontend/ + 코드 |
| /solo-product-squad:build-backend | 백엔드 구현 계획 → 승인 → 코드 | output/backend/ + 코드 |
| /solo-product-squad:test | 테스트 전략·케이스·릴리즈 체크리스트 | output/qa/ |
| /solo-product-squad:review | OMC verifier/reviewer 기반 교차검토·출시 리스크 정리 | output/review/findings.md |
| /solo-product-squad:security | OWASP Top 10 보안 취약점 분석·심각도 분류 | output/security/findings.md |
| /solo-product-squad:marketing | 시장 분석·경쟁사 비교·GTM 전략 수립 | output/marketing/ |
| /solo-product-squad:operate | 배포·모니터링·알림·운영 루틴 | output/ops/ |
| /solo-product-squad:setup | 초기 설정 및 도구 설치 | — |
| /solo-product-squad:help | 명령 목록 및 사용법 안내 | — |
| /solo-product-squad:core | 전체 워크플로우 안내 및 라우팅 | — |

---

## 산출물 경로



---

## 기술 스택 결정 원칙

| 조건 | 기술 스택 |
|------|----------|
| 기본값 | Next.js 풀스택 (프론트+백엔드 통합) |
| 결제/정산/권한/감사로그 포함 | Next.js + Spring Boot 분리 |
| 배치/스케줄링/대용량 처리 포함 | Next.js + Spring Boot 분리 |
| 고객사별 복잡 정책 로직 포함 | Next.js + Spring Boot 분리 |

---

## 보안 원칙

- network_access 기본 금지 (모든 에이전트)
- code_execute 기본 금지 — frontend-engineer·backend-engineer만 테스트/빌드 목적 허용
- 비밀값(토큰/키/비밀번호) 파일 저장 금지 (마스킹 처리)
- 코드 반영 전 반드시 사용자 승인 요청

---

## 컨텍스트 관리 원칙

- 새 단계 시작 전 반드시 output/stage-handoff.md를 읽어 잠긴 결정과 must-read 목록 파악
- 새 세션 시작 시 python scripts/context_pack.py --root . --stage <stage>로 최소 컨텍스트만 로드
- test 단계 종료 전 output/qa/release-checklist.md의 READY 여부 확인. BLOCKED면 operate 진행 금지
- review 단계는 독립 검토 후 confirm → operate 진입 허용
- operate 단계는 READY 확인 후에만 배포·운영 진행

---

## 요구사항

| 도구 | 유형 | 용도 |
|------|------|------|
| Claude Code | 런타임 | 플러그인 실행 환경 |
| Node.js 18+ | 선택 | context7 MCP 서버 실행 |
| context7 MCP | 선택 | 라이브러리 공식 문서 검색 (frontend/backend-engineer) |

---

## 디렉토리 구조



---

## Agent Metadata Maintenance

- agents/INDEX.md는 각 에이전트의 Quick Index 섹션을 모아 자동 생성됨.
- 에이전트 메타데이터 수정 후 다음 스크립트 실행:
  - python scripts/generate_agent_index.py
  - python scripts/agent_index_lint.py
  - python scripts/agent_digest.py --agent <agent-name>

## Root Canonical Context

- 크로스 프로젝트 컨텍스트는 output/project-state.md, output/stage-handoff.md, output/context-index.md, output/standardization-map.md를 먼저 읽을 것.
- 정식 루트 문서를 레거시 문서보다 우선 사용. 단, 정식 파일이 레거시 소스를 링크할 경우 예외.

---

## 라이선스

MIT License — jihoo
