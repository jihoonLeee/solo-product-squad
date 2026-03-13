# Stage Handoff

## 직전 단계 요약
- 생산한 단계: review
- 한 줄 요약: 테스트 증거와 구현 산출물을 교차 검토했고 출시 가능한 수준으로 리스크를 정리했다.
- 완료 기준: approval, execution evidence, findings 문서가 모두 정리됨

## 다음 단계 필수 읽기
- must-read: `output/project-state.md`
- must-read: `output/qa/release-checklist.md`
- must-read: `output/review/findings.md`

## 잠긴 결정
- MVP 범위 밖의 예산 분석 기능은 출시 후 검토한다.
- 초기 출시에서는 이메일 인증만 지원한다.
- 운영 모니터링은 핵심 퍼널과 결제 실패율부터 본다.

## 주의할 리스크
- 카드사/은행 연동은 향후 확장 포인트라 이번 예시에는 포함되지 않는다.
- 실제 운영 임계값은 트래픽이 쌓이면 재조정이 필요하다.

## 다음 에이전트에 대한 요청
- operate 단계에서는 release checklist와 findings만 먼저 읽고, 세부 코드나 계약은 필요할 때만 확장한다.