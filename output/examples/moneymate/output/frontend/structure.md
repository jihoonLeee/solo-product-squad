# 프론트엔드 구조

## 디렉토리 구조

- `app/(marketing)` 랜딩
- `app/(auth)` 로그인/회원가입
- `app/(dashboard)` 대시보드, 지출, 예산, 인사이트
- `components/ui` 공통 UI
- `components/finance` 도메인 컴포넌트

## 상태 관리 전략

- 서버 상태: React Query
- 폼 상태: React Hook Form
- 세션 상태: 서버 쿠키 + 미들웨어

## API 클라이언트 설계

- `lib/api/client.ts`에 fetch wrapper
- 에러 코드 매핑
- 인증 토큰 자동 포함

## 주요 컴포넌트 목록

- BudgetHeroCard
- ExpenseQuickForm
- CategorySpendChart
- WeeklyCoachCard
