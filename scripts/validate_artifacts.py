#!/usr/bin/env python3
"""Validate solo-product-squad artifact files for required sections."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def md_checks(*patterns: str) -> list[str]:
    return list(patterns)


COMMON_REQUIRED: list[tuple[str, list[str]]] = [
    (
        "output/context-index.md",
        md_checks("## Read Order", "## Stage Map", "## Source Of Truth"),
    ),
    (
        "output/project-state.md",
        md_checks("## 현재 단계", "## 승인 상태", "## 핵심 결정", "## 열린 질문", "## 다음 단계"),
    ),
    (
        "output/stage-handoff.md",
        md_checks(
            "## 직전 단계 요약",
            "## 다음 단계 필수 읽기",
            "## 잠긴 결정",
            "## 주의할 리스크",
            "## 다음 에이전트에 대한 요청",
        ),
    ),
]


STAGES: dict[str, list[tuple[str, list[str]]]] = {
    "validate": [
        ("output/idea-brief.md", md_checks("## 아이디어 한 줄 요약", "## 타깃 고객", "## 수익 모델", "## 핵심 가정")),
        ("output/validation-plan.md", md_checks("## 검증 목표", "## 실험 목록", "## KPI 정의", "## 다음 단계 트리거")),
    ],
    "plan": [
        ("output/mvp-scope.md", md_checks("## MVP 목표", "## In-Scope", "## Out-of-Scope", "## 기술 스택 결정", "## 마일스톤 일정")),
    ],
    "design": [
        ("output/ux/ia.md", md_checks("사이트맵", "주요 사용자 흐름", "페이지별 역할")),
        ("output/ux/wireframes.md", md_checks("모바일", "데스크톱")),
        ("output/ux/design-tokens.md", md_checks("## Colors", "## Typography", "## Spacing")),
    ],
    "frontend-design": [
        ("output/ux/visual-direction.md", md_checks("## 제품 인상", "## Aesthetic Direction", "## Typography Strategy", "## Color Strategy")),
    ],
    "architect": [
        ("contracts/openapi.yaml", ["openapi:", "paths:", "components:"]),
        ("contracts/domain-model.md", md_checks("## 핵심 엔티티", "## 엔티티 관계", "## 불변 조건")),
        ("contracts/error-codes.md", md_checks("## 에러 코드 목록")),
        ("contracts/authz.md", md_checks("## 역할", "## 리소스별 권한 매트릭스")),
    ],
    "build-frontend": [
        ("output/frontend/structure.md", md_checks("디렉토리", "상태 관리", "API")),
        ("output/frontend/pages.md", md_checks("라우트", "API", "인증")),
        ("output/frontend/approval.md", md_checks("## 승인 상태", "## 승인 기준", "## 승인 기록")),
    ],
    "build-backend": [
        ("output/backend/plan.md", md_checks("기술 스택", "서비스", "인증", "비즈니스 로직")),
        ("output/backend/migrations.md", md_checks("마이그레이션", "시드", "롤백")),
        ("output/backend/approval.md", md_checks("## 승인 상태", "## 승인 기준", "## 승인 기록")),
    ],
    "test": [
        ("output/qa/test-plan.md", md_checks("테스트 전략", "단위", "통합", "E2E")),
        ("output/qa/test-cases.md", md_checks("Happy Path", "예외", "회귀")),
        ("output/qa/execution-evidence.md", md_checks("## 실행한 검증", "## 결과 요약", "## 남은 리스크")),
        ("output/qa/release-checklist.md", md_checks("READY", "BLOCKED", "실행 증거")),
    ],
    "review": [
        (
            "output/review/findings.md",
            md_checks(
                "## 무엇을 발견했는가",
                "## 무엇을 수정했는가",
                "## 왜 그렇게 판단했는가",
                "## 남은 리스크",
                "## 다음 작업",
            ),
        ),
    ],
    "operate": [
        ("output/ops/runbook.md", md_checks("배포 절차", "롤백", "장애")),
        ("output/ops/alerts.yml", ["threshold", "channel"]),
        ("output/ops/release-run.md", md_checks("스모크 테스트", "모니터링")),
    ],
}


def validate_file(root: Path, rel_path: str, patterns: list[str], allow_missing: bool) -> list[str]:
    errors: list[str] = []
    file_path = root / rel_path
    if not file_path.exists():
        if not allow_missing:
            errors.append(f"missing: {rel_path}")
        return errors

    text = file_path.read_text(encoding="utf-8")
    lowered = text.lower()
    for pattern in patterns:
        if pattern.lower() not in lowered:
            errors.append(f"missing pattern in {rel_path}: {pattern}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate solo-product-squad artifacts.")
    parser.add_argument("--root", default=".", help="Workspace root to validate")
    parser.add_argument(
        "--stage",
        default="all",
        choices=["all", *STAGES.keys()],
        help="Validate a single stage or all stages",
    )
    parser.add_argument(
        "--allow-missing",
        action="store_true",
        help="Do not fail on missing files; only validate files that exist",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    stages = STAGES.keys() if args.stage == "all" else [args.stage]
    errors: list[str] = []

    for stage in stages:
        for rel_path, patterns in COMMON_REQUIRED:
            errors.extend(validate_file(root, rel_path, patterns, args.allow_missing))
        for rel_path, patterns in STAGES[stage]:
            errors.extend(validate_file(root, rel_path, patterns, args.allow_missing))

    if errors:
        print("artifact validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("artifact validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
