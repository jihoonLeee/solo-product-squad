---
name: setup
description: solo-product-squad 플러그인 초기 설정 및 도구 설치
type: setup
user-invocable: true
---

# Setup

[solo-product-squad 설정 시작]

## 목표

solo-product-squad 플러그인의 초기 설정을 수행하고,
gateway/install.yaml 기반으로 필요한 도구를 설치하며,
산출물 디렉토리 구조를 생성함.

## 워크플로우

### Step 1: install.yaml 읽기
`gateway/install.yaml`을 읽어 설치 대상 도구 목록 확인.

### Step 2: context7 MCP 설치

현재 OS를 확인하여 적절한 설치 명령을 안내함.

**Windows:**
```bash
claude mcp add-json context7 "{\"type\":\"stdio\",\"command\":\"cmd\",\"args\":[\"/c\",\"npx\",\"-y\",\"@upstash/context7-mcp@latest\"]}" -s user
```

**macOS/Linux:**
```bash
claude mcp add-json context7 '{"type":"stdio","command":"npx","args":["-y","@upstash/context7-mcp@latest"]}' -s user
```

이미 설치된 경우 건너뜀. 실패해도 플러그인 기본 동작에는 영향 없음 (required: false).

### Step 3: 산출물 디렉토리 생성

아래 디렉토리가 없으면 생성함:
- `contracts/`
- `output/`
- `output/ux/`
- `output/frontend/`
- `output/backend/`
- `output/qa/`
- `output/ops/`

### Step 4: GitHub 저장소 생성 안내 (선택)

새로운 수익화 아이템을 시작하는 경우, create_repo 도구로 GitHub 저장소를 자동 생성할 수 있음.
사용자에게 저장소 생성 여부를 확인함.

### Step 5: 적용 범위 설정

사용자에게 플러그인 활성화 범위를 질문함:
1. **모든 프로젝트** — `~/.claude/CLAUDE.md`에 solo-product-squad 라우팅 등록
2. **이 프로젝트만** — `./CLAUDE.md`에 solo-product-squad 라우팅 등록

### Step 6: 설치 완료 보고

설치 결과를 요약하여 사용자에게 보고함:
- 설치된 도구 목록
- 생성된 디렉토리 목록
- 사용 가능한 슬래시 명령 목록
- 시작 방법: `/solo-product-squad:validate` 또는 `/solo-product-squad:help`
