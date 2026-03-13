# 도메인 모델

## 핵심 엔티티

### User
| 속성 | 타입 | 필수 | 설명 |
|------|------|:----:|------|
| id | UUID | O | 사용자 식별자 |
| email | string | O | 로그인 이메일 |
| plan | enum | O | free, pro |
| createdAt | datetime | O | 가입 일시 |

### Expense
| 속성 | 타입 | 필수 | 설명 |
|------|------|:----:|------|
| id | UUID | O | 지출 식별자 |
| userId | UUID | O | 소유 사용자 |
| category | enum | O | 식비, 교통, 업무, 구독 등 |
| amount | decimal | O | 지출 금액 |
| spentAt | date | O | 지출 일자 |
| note | string | X | 메모 |

### MonthlyBudget
| 속성 | 타입 | 필수 | 설명 |
|------|------|:----:|------|
| id | UUID | O | 예산 식별자 |
| userId | UUID | O | 소유 사용자 |
| month | string | O | YYYY-MM |
| limitAmount | decimal | O | 월 예산 한도 |

## 엔티티 관계

`User 1:N Expense`

`User 1:N MonthlyBudget`

## 불변 조건

- Expense는 본인 계정으로만 생성/수정/삭제 가능
- MonthlyBudget는 사용자별 월 단위로 1개만 존재
- 삭제된 Expense는 월간 잔액 계산에서 즉시 제외
