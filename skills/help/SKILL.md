---
name: help
description: solo-product-squad 사용 가능한 명령 목록 및 워크플로우 안내
type: utility
user-invocable: true
---

# Help

**중요: 추가적인 파일 탐색이나 에이전트 위임 없이, 아래 내용을 즉시 사용자에게 출력하세요.**

## 목표

solo-product-squad 플러그인의 사용 가능한 명령과 워크플로우를 안내함.

---

## solo-product-squad 슬래시 명령

| 명령 | 설명 | 주요 산출물 |
|------|------|------------|
| `/solo-product-squad:validate` | 아이디어·수익 가설·검증 실험·KPI 정리 | output/idea-brief.md, output/validation-plan.md |
| `/solo-product-squad:plan` | MVP 범위·우선순위·일정 고정 | output/mvp-scope.md |
| `/solo-product-squad:design` | IA·와이어프레임·디자인 토큰 산출 | output/ux/ia.md, wireframes.md, design-tokens.md |
| `/solo-product-squad:architect` | API 계약·DB 스키마·도메인 모델·에러코드·권한 규격 | contracts/ 전체 |
| `/solo-product-squad:build-frontend` | 프론트엔드 구현 계획 수립 → 승인 후 코드 반영 | output/frontend/ + 코드 |
| `/solo-product-squad:build-backend` | 백엔드 구현 계획 수립 → 승인 후 코드 반영 | output/backend/ + 코드 |
| `/solo-product-squad:test` | 테스트 전략·케이스·릴리즈 체크리스트 | output/qa/ |
| `/solo-product-squad:operate` | 배포·모니터링·알림·백업·장애대응·운영 루틴 | output/ops/ |
| `/solo-product-squad:core` | 전체 워크플로우 안내 및 모호한 요청 라우팅 | — |
| `/solo-product-squad:setup` | 초기 설정 및 도구 설치 | — |
| `/solo-product-squad:help` | 이 도움말 출력 | — |

## 표준 워크플로우

```
/validate → /plan → /design → /architect → /build-frontend → /build-backend → /test → /operate
```

각 단계의 산출물이 다음 단계의 입력으로 재사용됩니다.

## 기술 스택 결정 원칙

- **기본값**: Next.js 풀스택 (프론트+백엔드 통합)
- **Spring Boot 분리 조건** (아래 중 1개라도 해당 시):
  - 결제/정산/권한/감사로그 로직
  - 배치/스케줄링/대용량 처리 (큐, 리트라이, DLQ)
  - 고객사별 커스텀/복잡한 정책 로직

## 보안 원칙

- 비밀값(토큰/키/비밀번호)은 어떤 파일에도 저장하지 않음
- 코드 반영 전 반드시 사용자 승인 요청 (build-frontend, build-backend)
