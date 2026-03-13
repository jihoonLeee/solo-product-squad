# 페이지 구현 계획

## 라우트

- `/` 랜딩
- `/login`
- `/signup`
- `/dashboard`
- `/expenses`
- `/budget`
- `/insights`

## API 연동 포인트

- `/dashboard` -> `GET /budget/status`, `GET /coach/insights`
- `/expenses` -> `GET /expenses`, `POST /expenses`, `PATCH /expenses/{expenseId}`, `DELETE /expenses/{expenseId}`
- `/budget` -> 예산 현황 API와 저장 API 연동

## 인증 처리 방식

- 미인증 사용자는 `/dashboard` 접근 시 `/login`으로 이동
- 인증 만료 시 로그아웃 및 재로그인 유도

## 화면별 acceptance criteria

- 대시보드: 남은 예산, 총지출, 주요 카테고리 노출
- 지출 내역: 신규 입력 후 리스트 즉시 갱신
- 예산 설정: 저장 성공 시 대시보드 반영
- 인사이트: 이번 주 추천 문장 3개 표시
