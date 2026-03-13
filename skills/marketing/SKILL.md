---
name: marketing
description: 시장 분석·경쟁사 조사·GTM 전략·마케팅 채널 계획 수립 (output/marketing/ 생성)
type: orchestrator
user-invocable: true
agent: marketing-analyst
---

# Marketing

[marketing 활성화 — 시장 분석 및 마케팅 전략 단계]

## 목표

타겟 시장 분석, 경쟁사 비교, Go-To-Market 전략, 채널별 마케팅 계획을 수립하고
`output/marketing/` 하위에 산출물을 생성함.

## 활성화 조건

- validate 또는 plan 완료 후 시장 검증이 필요할 때
- GTM 전략 수립이 필요할 때
- 수익화 경로를 구체화해야 할 때
- 출시 전 마케팅 채널 계획이 필요할 때

## 컨텍스트 로드 순서

1. `output/project-state.md`
2. `output/stage-handoff.md`
3. `output/idea-brief.md` (아이디어 요약)
4. `output/mvp-scope.md` (MVP 범위 확인)
5. 프로젝트의 `CLAUDE.md` (프로젝트별 시장 규칙)

## 워크플로우

### Step 1: 시장 분석 → Agent: marketing-analyst

**시장 규모 및 성장성**
- TAM / SAM / SOM 추정
- 시장 성장률 및 트렌드
- 주요 시장 리스크

**경쟁사 분석**
- 직접 경쟁사 3~5개 비교 (강점/약점/포지셔닝)
- 간접 경쟁사 (대체재) 분석
- 차별화 포인트 도출

### Step 2: 사용자 인사이트

**페르소나 정의**
- 주요 페르소나 2~3개 (인구통계, 행동패턴, pain point, 가치 기준)
- 사용자 여정 핵심 접점

**가치 제안 (Value Proposition)**
- "누가 / 왜 / 어떤 상황에서 쓰는가"
- 경쟁 대비 핵심 메시지

### Step 3: GTM 전략

**채널 전략**
- Acquisition 채널 우선순위 (SEO / SNS / 커뮤니티 / 광고 / 파트너십)
- 채널별 예상 비용 및 효과
- 런치 시퀀스 (소프트 런치 → 공개 런치)

**수익화 경로**
- 단기 (0~6개월): 트래픽 확보 우선
- 중기 (6~18개월): 전환 모델 실험
- 장기 (18개월+): 수익 구조 고도화

### Step 4: 산출물 생성

`output/marketing/strategy.md` — 전략 요약
`output/marketing/competitor-analysis.md` — 경쟁사 비교표
`output/marketing/gtm-plan.md` — 채널별 실행 계획

### Step 5: 상태 문서 갱신
- `output/project-state.md` 시장 인사이트 섹션 갱신
- `output/stage-handoff.md` 마케팅 판단 기록

## 품질 게이트

- 페르소나는 실제 사용자 행동 기반이어야 함 (가정 최소화)
- 경쟁사 분석은 직접 경쟁사 최소 3개 포함
- GTM 채널은 예산/시간 현실성 평가 포함
- 수익화 경로는 트래픽 전제조건 명시
