# context7

- [context7](#context7)
  - [기본 정보](#기본-정보)
  - [설치 정보](#설치-정보)
  - [제공 도구](#제공-도구)
  - [사용 예시](#사용-예시)

---

## 기본 정보

| 항목 | 값 |
|------|---|
| 도구명 | context7 |
| 카테고리 | MCP 서버 |
| 설명 | 라이브러리 공식 문서 검색 및 코드 예시 제공 |
| 제공자 | Upstash |

---

## 설치 정보

| 항목 | 값 |
|------|---|
| 필수 여부 | 선택 (없어도 플러그인 동작) |
| 의존성 | Node.js 18+, npx |

**설치 명령 (Windows):**

```bash
claude mcp add-json context7 "{\"type\":\"stdio\",\"command\":\"cmd\",\"args\":[\"/c\",\"npx\",\"-y\",\"@upstash/context7-mcp@latest\"]}" -s user
```

**설치 명령 (macOS/Linux):**

```bash
claude mcp add-json context7 '{"type":"stdio","command":"npx","args":["-y","@upstash/context7-mcp@latest"]}' -s user
```

---

## 제공 도구

| 도구명 | 설명 | 주요 파라미터 |
|--------|------|-------------|
| `resolve-library-id` | 라이브러리명을 Context7 ID로 변환 | `libraryName`: 라이브러리명, `query`: 검색 질의 |
| `query-docs` | 라이브러리 공식 문서 검색 | `libraryId`: Context7 ID, `query`: 검색 질의 |

---

## 사용 예시

```
1. resolve-library-id로 라이브러리 ID 획득
   → libraryName: "react", query: "useState hook"
   → 결과: "/facebook/react"

2. query-docs로 문서 검색
   → libraryId: "/facebook/react", query: "useState hook usage"
   → 결과: 공식 문서 내용 + 코드 예시
```
