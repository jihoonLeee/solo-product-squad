# DB 마이그레이션 계획

## 마이그레이션 순서

1. users 생성
2. monthly_budgets 생성
3. expenses 생성
4. expenses 인덱스 추가 (`userId`, `spentAt`)

## 시드 계획

- 기본 카테고리 8종
- 데모 사용자용 샘플 지출 5건

## 롤백 전략

- 신규 테이블은 reverse migration 제공
- 잘못된 인사이트 계산은 데이터 손상 없이 재생성 가능
