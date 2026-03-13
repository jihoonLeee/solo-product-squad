---
name: security
description: 보안 취약점 분석·위협 모델링·출시 전 보안 게이트 검증 (output/security/findings.md 생성)
type: orchestrator
user-invocable: true
agent: security-analyst
---

# Security

[security 활성화 — 보안 검토 단계]

## 목표

코드베이스와 인프라 설정을 대상으로 OWASP Top 10 기준 보안 취약점을 분석하고
`output/security/findings.md`에 심각도별 결과를 기록함.

## 활성화 조건

- build-frontend 또는 build-backend 완료 후 출시 전 보안 검토 필요 시
- 인증/인가 구조가 변경된 경우
- 새 API 엔드포인트 또는 DB 스키마 추가 후
- 보안 이슈 제보 또는 의심 증상 발생 시

## 컨텍스트 로드 순서

1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `contracts/openapi.yaml` (API 계약 확인)
4. `contracts/authz.md` (권한 규격 확인)
5. 프로젝트의 `CLAUDE.md` (프로젝트별 보안 규칙)

## 워크플로우

### Step 1: 범위 확정
검토 대상 영역을 명시함: API 레이어 / 인증·인가 / 입력 검증 / 환경변수 / DB 접근

### Step 2: OWASP Top 10 체크 → Agent: security-analyst

**A01 접근통제 실패**
- API 엔드포인트별 인증 필요 여부 검증
- 관리자 경로 비인증 접근 가능 여부 확인
- RBAC/ABAC 정책 적용 확인

**A02 암호화 실패**
- 민감 데이터 전송 암호화(HTTPS) 확인
- 환경변수 클라이언트 노출 여부 (`NEXT_PUBLIC_` 등)
- 비밀번호/토큰 평문 저장 여부

**A03 인젝션**
- SQL/NoSQL 쿼리 파라미터 직접 삽입 여부
- 사용자 입력 이스케이프 처리 확인
- ORM/쿼리 빌더 파라미터 바인딩 사용 여부

**A05 보안 설정 오류**
- 개발용 설정이 프로덕션에 노출된 경우
- CORS 정책 과도한 허용 여부
- 불필요한 HTTP 메서드 허용 여부

**A07 인증 및 세션 관리 실패**
- 토큰 만료 정책 확인
- CSRF 토큰 적용 여부 (OAuth, form submit)
- 세션 고정 공격 방어 여부

### Step 3: 심각도 분류 및 보고서 생성

`output/security/findings.md`를 생성 또는 갱신:

```markdown
# Security Findings

## Critical
- [이슈 설명] / [파일:라인] / [재현 방법] / [권장 수정]

## High
...

## Medium
...

## Low / Info
...

## 출시 판정
BLOCKED (Critical/High 미해결) / CONDITIONAL (Medium만 남음) / PASS
```

### Step 4: 상태 문서 갱신
- `output/project-state.md` 보안 섹션 갱신
- `output/stage-handoff.md`에 보안 판정 결과 기록

## 품질 게이트

- Critical 이슈 0건이어야 출시 판정 PASS 가능
- High 이슈는 수정 계획 명시 시 CONDITIONAL 허용
- `output/security/findings.md` 없으면 release-checklist BLOCKED 유지
