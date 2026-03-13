# 권한 규격

## 역할(Role) 정의

| 역할 | 설명 |
|------|------|
| user | 일반 사용자 |
| admin | 운영 관리자 |

## 인증 플로우

1. 이메일/비밀번호로 로그인
2. Access Token 발급
3. API 요청 시 Bearer 토큰 전달
4. 토큰 만료 시 재로그인

## 리소스별 권한 매트릭스

| 리소스 | 액션 | admin | user |
|--------|------|:-----:|:----:|
| Expense | read | O | 본인만 |
| Expense | create | O | O |
| Expense | update | O | 본인만 |
| Expense | delete | O | 본인만 |
| MonthlyBudget | read | O | 본인만 |
| MonthlyBudget | create | O | O |
| CoachInsight | read | O | 본인만 |
