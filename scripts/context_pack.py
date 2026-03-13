#!/usr/bin/env python3
"""Print the minimum context pack for a solo-product-squad stage."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FALLBACK_STAGE_MAP: dict[str, list[str]] = {
    "validate": ["output/project-state.md"],
    "plan": ["output/idea-brief.md", "output/validation-plan.md"],
    "design": ["output/mvp-scope.md"],
    "frontend-design": [
        "output/mvp-scope.md",
        "output/ux/ia.md",
        "output/ux/wireframes.md",
        "output/ux/design-tokens.md",
    ],
    "architect": ["output/mvp-scope.md", "output/ux/ia.md", "output/ux/wireframes.md"],
    "build-frontend": [
        "contracts/openapi.yaml",
        "output/ux/ia.md",
        "output/ux/wireframes.md",
        "output/mvp-scope.md",
        "output/frontend/approval.md",
    ],
    "build-backend": [
        "contracts/openapi.yaml",
        "contracts/domain-model.md",
        "output/mvp-scope.md",
        "output/backend/approval.md",
    ],
    "test": ["contracts/openapi.yaml", "output/frontend/pages.md", "output/backend/plan.md"],
    "review": ["output/qa/release-checklist.md", "output/qa/execution-evidence.md", "output/review/findings.md"],
    "operate": ["output/qa/release-checklist.md", "output/review/findings.md", "output/backend/plan.md"],
}

COMMON_FILES = ["output/project-state.md", "output/stage-handoff.md"]
STAGE_RE = re.compile(r"^- ([a-z-]+): (.+)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print the minimal context pack for a stage.")
    parser.add_argument("--root", default=".", help="Workspace root")
    parser.add_argument("--stage", required=True, choices=sorted(FALLBACK_STAGE_MAP.keys()))
    parser.add_argument("--format", default="text", choices=["text", "json"], help="Output format")
    return parser.parse_args()


def parse_stage_map(context_index_path: Path) -> dict[str, list[str]]:
    if not context_index_path.exists():
        return FALLBACK_STAGE_MAP

    lines = context_index_path.read_text(encoding="utf-8").splitlines()
    stage_map: dict[str, list[str]] = {}
    in_stage_map = False

    for line in lines:
        if line.strip() == "## Stage Map":
            in_stage_map = True
            continue
        if in_stage_map and line.startswith("## "):
            break

        match = STAGE_RE.match(line.strip())
        if not match:
            continue

        stage = match.group(1)
        parts = [part.strip() for part in match.group(2).split(",")]
        files = [part for part in parts if "`" in part]
        cleaned = [item.replace("`", "") for item in files]
        if cleaned:
            stage_map[stage] = cleaned

    return {**FALLBACK_STAGE_MAP, **stage_map}


def extract_section(text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    result: list[str] = []
    collecting = False

    for line in lines:
        if line.strip() == heading:
            collecting = True
            continue
        if collecting and line.startswith("## "):
            break
        if collecting:
            result.append(line)

    return [line for line in result if line.strip()]


def build_payload(root: Path, stage: str) -> dict[str, object]:
    context_index_path = root / "output/context-index.md"
    stage_handoff_path = root / "output/stage-handoff.md"
    project_state_path = root / "output/project-state.md"

    stage_map = parse_stage_map(context_index_path)
    stage_files = COMMON_FILES + stage_map.get(stage, [])

    payload = {
        "stage": stage,
        "files": [],
        "missing": [],
        "current_stage": "",
        "locked_decisions": [],
        "risks": [],
    }

    seen: set[str] = set()
    for rel_path in stage_files:
        if rel_path in seen:
            continue
        seen.add(rel_path)
        path = root / rel_path
        if path.exists():
            payload["files"].append(rel_path)
        else:
            payload["missing"].append(rel_path)

    if project_state_path.exists():
        project_state = project_state_path.read_text(encoding="utf-8")
        current = extract_section(project_state, "## 현재 단계")
        if current:
            payload["current_stage"] = current[0]

    if stage_handoff_path.exists():
        handoff = stage_handoff_path.read_text(encoding="utf-8")
        payload["locked_decisions"] = extract_section(handoff, "## 잠긴 결정")
        payload["risks"] = extract_section(handoff, "## 주의할 리스크")

    return payload


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    payload = build_payload(root, args.stage)

    if args.format == "json":
        json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0

    print(f"stage: {payload['stage']}")
    if payload["current_stage"]:
        print(f"current: {payload['current_stage']}")

    print("files:")
    for rel_path in payload["files"]:
        print(f"- {rel_path}")

    if payload["locked_decisions"]:
        print("locked_decisions:")
        for item in payload["locked_decisions"]:
            print(f"- {item.lstrip('- ').strip()}")

    if payload["risks"]:
        print("risks:")
        for item in payload["risks"]:
            print(f"- {item.lstrip('- ').strip()}")

    if payload["missing"]:
        print("missing:")
        for rel_path in payload["missing"]:
            print(f"- {rel_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())