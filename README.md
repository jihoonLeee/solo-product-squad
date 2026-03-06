# solo-product-squad

> 1인 창업자·솔로 개발자를 위한 수익화 아이템 개발 표준 워크플로우 DMAP 플러그인

---

## 개요

solo-product-squad는 혼자서 아이디어→기획→디자인→설계→개발→테스트→운영까지
반복하며 수익화 아이템을 빠르게 만들 수 있도록 표준 워크플로우를 제공하는 DMAP 플러그인임.

**주요 특징:**
- 8단계 워크플로우로 아이디어를 운영 중인 제품으로 전환
- 각 단계의 산출물이 다음 단계의 입력으로 재사용됨 (파이프라인 구조)
- 기술 스택 기본값: Next.js 풀스택 (Spring Boot 분리 조건 명시)
- 코드 반영 전 반드시 사용자 승인 요청 (build-frontend, build-backend)
- 비밀값 파일 저장 금지 원칙 적용

**에이전트 구성:**

| 에이전트 | 역할 | 티어 |
|---------|------|------|
| founder-strategist | 아이디어·수익 가설·검증 실험 설계 | HIGH |
| pm-scoper | MVP 범위·우선순위·일정 결정 | HIGH |
| ux-designer | IA·와이어프레임·디자인 토큰 산출 | MEDIUM |
| tech-architect | API 계약·DB 스키마·도메인 모델 확정 | HIGH |
| frontend-engineer | 프론트엔드 구현 계획 및 코드 반영 | MEDIUM |
| backend-engineer | 백엔드 구현 계획 및 코드 반영 | MEDIUM |
| qa-engineer | 테스트 전략·케이스·릴리즈 게이트 | MEDIUM |
| ops-manager | 배포·모니터링·장애대응·운영 루틴 | MEDIUM |

---

## 설치

### 사전 요구사항

- [Claude Code](https://claude.com/claude-code) CLI 설치
- Node.js 18+ (context7 MCP용)

### 플러그인 설치

**방법 1: 마켓플레이스 — GitHub (권장)**

```bash
# 1. GitHub 저장소를 마켓플레이스로 등록
claude plugin marketplace add jihoo/solo-product-squad

# 2. 플러그인 설치
claude plugin install solo-product-squad@solo-product-squad

# 3. 설치 확인
claude plugin list
```

**방법 2: 마켓플레이스 — 로컬**

```bash
# 1. 로컬 경로를 마켓플레이스로 등록
claude plugin marketplace add ./solo-product-squad

# 2. 플러그인 설치
claude plugin install solo-product-squad@solo-product-squad

# 3. 설치 확인
claude plugin list
```

> **설치 후 setup 스킬 실행:**
> ```
> /solo-product-squad:setup
> ```
> - context7 MCP 서버 설치 (선택)
> - 산출물 디렉토리 구조 생성
> - 플러그인 활성화 범위 설정

---

## 업그레이드

```bash
# 마켓플레이스 업데이트
claude plugin marketplace update solo-product-squad

# 플러그인 재설치
claude plugin install solo-product-squad@solo-product-squad
```

> **갱신이 반영되지 않는 경우:**
> ```bash
> claude plugin remove solo-product-squad@solo-product-squad
> claude plugin marketplace update solo-product-squad
> claude plugin install solo-product-squad@solo-product-squad
> ```

---

## 사용법

### 표준 워크플로우

```
/validate → /plan → /design → /architect → /build-frontend → /build-backend → /test → /operate
```

### 슬래시 명령

| 명령 | 설명 | 주요 산출물 |
|------|------|------------|
| `/solo-product-squad:validate` | 아이디어·수익 가설·검증 실험·KPI 정리 | output/idea-brief.md, output/validation-plan.md |
| `/solo-product-squad:plan` | MVP 범위·우선순위·일정 고정 | output/mvp-scope.md |
| `/solo-product-squad:design` | IA·와이어프레임·디자인 토큰 산출 | output/ux/ |
| `/solo-product-squad:architect` | API 계약·DB 스키마·도메인 모델 확정 | contracts/ |
| `/solo-product-squad:build-frontend` | 프론트엔드 구현 계획 → 승인 → 코드 | output/frontend/ + 코드 |
| `/solo-product-squad:build-backend` | 백엔드 구현 계획 → 승인 → 코드 | output/backend/ + 코드 |
| `/solo-product-squad:test` | 테스트 전략·케이스·릴리즈 체크리스트 | output/qa/ |
| `/solo-product-squad:operate` | 배포·모니터링·알림·운영 루틴 | output/ops/ |
| `/solo-product-squad:setup` | 초기 설정 및 도구 설치 | — |
| `/solo-product-squad:help` | 명령 목록 및 사용법 안내 | — |
| `/solo-product-squad:core` | 전체 워크플로우 안내 및 라우팅 | — |

### 사용 예시

```
# 새 아이디어 검증 시작
/solo-product-squad:validate
→ "구독 기반 개인 재무 관리 앱 아이디어가 있는데 검증해줘"

# 이후 순서대로 실행
/solo-product-squad:plan
/solo-product-squad:design
/solo-product-squad:architect
/solo-product-squad:build-frontend  # 계획 확인 후 승인 필요
/solo-product-squad:build-backend   # 계획 확인 후 승인 필요
/solo-product-squad:test
/solo-product-squad:operate
```

---

## 산출물 경로

```
contracts/
  openapi.yaml          ← API 계약 (단일 소스)
  domain-model.md       ← 도메인 모델
  error-codes.md        ← 에러 코드 체계
  authz.md              ← 권한 규격

output/
  idea-brief.md         ← 아이디어 브리프
  validation-plan.md    ← 검증 계획
  mvp-scope.md          ← MVP 스코프
  ux/
    ia.md               ← 정보 구조
    wireframes.md       ← 와이어프레임
    design-tokens.md    ← 디자인 토큰
  frontend/
    structure.md        ← 프론트엔드 구조
    pages.md            ← 페이지 구현 계획
  backend/
    plan.md             ← 백엔드 구현 계획
    migrations.md       ← DB 마이그레이션
  qa/
    test-plan.md        ← 테스트 계획
    test-cases.md       ← 테스트 케이스
    release-checklist.md← 릴리즈 체크리스트
  ops/
    runbook.md          ← 운영 런북
    alerts.yml          ← 알림 규칙
    release-run.md      ← 릴리즈 실행 체크리스트
```

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

- `network_access` 기본 금지 (모든 에이전트)
- `code_execute` 기본 금지 — frontend-engineer·backend-engineer만 테스트/빌드 목적 허용
- 비밀값(토큰/키/비밀번호) 파일 저장 금지 (마스킹 처리)
- 코드 반영 전 반드시 사용자 승인 요청

---

## 요구사항

| 도구 | 유형 | 용도 |
|------|------|------|
| Claude Code | 런타임 | 플러그인 실행 환경 |
| Node.js 18+ | 선택 | context7 MCP 서버 실행 |
| context7 MCP | 선택 | 라이브러리 공식 문서 검색 (frontend/backend-engineer) |

---

## 디렉토리 구조

```
solo-product-squad/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── .gitignore
├── README.md
├── gateway/
│   ├── install.yaml
│   ├── runtime-mapping.yaml
│   └── mcp/
│       └── context7.json
├── agents/
│   ├── founder-strategist/   (AGENT.md + agentcard.yaml + tools.yaml)
│   ├── pm-scoper/
│   ├── ux-designer/
│   ├── tech-architect/
│   ├── frontend-engineer/    (+ references/context7.md)
│   ├── backend-engineer/     (+ references/context7.md)
│   ├── qa-engineer/
│   └── ops-manager/
├── skills/
│   ├── core/       ├── setup/      ├── help/
│   ├── validate/   ├── plan/       ├── design/
│   ├── architect/  ├── build-frontend/ (+ assets/develop.md)
│   ├── build-backend/ (+ assets/develop.md)
│   ├── test/       └── operate/
├── commands/
│   └── (core, setup, help, validate, plan, design,
│       architect, build-frontend, build-backend, test, operate).md
├── contracts/
│   └── _template/  (openapi, error-codes, authz, domain-model 템플릿)
└── output/
    └── (ux/, frontend/, backend/, qa/, ops/)
```

---

## 라이선스

MIT License — jihoo
