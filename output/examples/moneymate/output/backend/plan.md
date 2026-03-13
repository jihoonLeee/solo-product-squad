# 백엔드 구현 계획

## 기술 스택 최종 결정 및 근거

- 기술 스택: Next.js Route Handlers + Prisma + PostgreSQL
- 근거: MVP 속도 우선, 단일 리포지토리 유지, CRUD 중심 도메인

## 서비스 레이어 구조

- AuthService
- ExpenseService
- BudgetService
- InsightService

## 인증/인가 구현 방식

- JWT access token
- 사용자 본인 데이터만 접근 가능하도록 userId 기준 필터
- 관리자 권한은 운영 화면에서만 사용

## 주요 비즈니스 로직 설명

- 지출 등록/수정/삭제 후 월간 예산 잔액 재계산
- 구독/고정비 카테고리는 인사이트에서 별도 강조
- 인사이트는 최근 7일 지출 패턴과 예산 대비 비율 기반으로 생성
