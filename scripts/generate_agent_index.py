#!/usr/bin/env python3
"""Generate agents/INDEX.md from each agent's Quick Index."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"
INDEX_FILE = AGENTS_DIR / "INDEX.md"

STAGE_ORDER = [
    "validate",
    "plan",
    "design",
    "architect",
    "build-frontend",
    "build-backend",
    "test",
    "review",
    "operate",
]


@dataclass
class AgentRecord:
    name: str
    stage: str
    inputs: list[str]
    outputs: list[str]
    handoffs: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate agents/INDEX.md from agent Quick Index sections.")
    parser.add_argument("--check", action="store_true", help="Fail if INDEX.md is out of date.")
    parser.add_argument("--stdout", action="store_true", help="Print the generated content instead of writing it.")
    return parser.parse_args()


def split_items(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_quick_index(agent_dir: Path) -> AgentRecord:
    agent_md = agent_dir / "AGENT.md"
    text = agent_md.read_text(encoding="utf-8")

    stage_match = re.search(r"^- Stage owner: `([^`]+)`", text, re.MULTILINE)
    inputs_match = re.search(r"^- Read first: (.+)$", text, re.MULTILINE)
    outputs_match = re.search(r"^- Produces: (.+)$", text, re.MULTILINE)
    handoffs_match = re.search(r"^- Hands off to: (.+)$", text, re.MULTILINE)

    if "## Quick Index" not in text:
        raise ValueError(f"{agent_dir.name}: missing Quick Index section")
    if not stage_match:
        raise ValueError(f"{agent_dir.name}: missing Stage owner line")
    if not inputs_match:
        raise ValueError(f"{agent_dir.name}: missing Read first line")
    if not outputs_match:
        raise ValueError(f"{agent_dir.name}: missing Produces line")
    if not handoffs_match:
        raise ValueError(f"{agent_dir.name}: missing Hands off to line")

    return AgentRecord(
        name=agent_dir.name,
        stage=stage_match.group(1).strip(),
        inputs=split_items(inputs_match.group(1).replace("`", "")),
        outputs=split_items(outputs_match.group(1).replace("`", "")),
        handoffs=split_items(handoffs_match.group(1).replace("`", "")),
    )


def sort_key(record: AgentRecord) -> tuple[int, str]:
    try:
        return (STAGE_ORDER.index(record.stage), record.name)
    except ValueError:
        return (len(STAGE_ORDER), record.name)


def build_index(records: list[AgentRecord]) -> str:
    lines = [
        "# Agent Index",
        "",
        "## Purpose",
        "",
        "Use this file as the compact registry for agent discovery.",
        "Read this file first, then open only the target agent's `AGENT.md`, `agentcard.yaml`, and `tools.yaml`.",
        "",
        "## Read Order",
        "",
        "1. `agents/INDEX.md`",
        "2. Target agent `AGENT.md`",
        "3. Target agent `agentcard.yaml`",
        "4. Target agent `tools.yaml`",
        "",
        "## Registry",
        "",
        "| Agent | Stage | Read First | Produces | Handoff |",
        "|------|------|------------|----------|---------|",
    ]

    for record in sorted(records, key=sort_key):
        lines.append(
            "| {agent} | {stage} | `{inputs}` | `{outputs}` | `{handoffs}` |".format(
                agent=record.name,
                stage=record.stage,
                inputs="`, `".join(record.inputs),
                outputs="`, `".join(record.outputs),
                handoffs="`, `".join(record.handoffs),
            )
        )

    lines.extend(
        [
            "",
            "## Rules",
            "",
            "- Keep `agents/INDEX.md` generated from each agent's Quick Index.",
            "- Keep each `AGENT.md` Quick Index to 5 lines or fewer.",
            "- Use `python scripts/generate_agent_index.py` after editing agent metadata.",
            "- Use `python scripts/agent_index_lint.py` to verify index and handoff consistency.",
            "",
        ]
    )
    return "\n".join(lines)


def load_records() -> list[AgentRecord]:
    records: list[AgentRecord] = []
    for path in sorted(AGENTS_DIR.iterdir()):
        if not path.is_dir():
            continue
        records.append(parse_quick_index(path))
    return records


def main() -> int:
    args = parse_args()
    try:
        generated = build_index(load_records())
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.stdout:
        sys.stdout.write(generated)
        return 0

    current = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""
    if args.check:
        if current != generated:
            print("agents/INDEX.md is out of date")
            return 1
        print("agents/INDEX.md is up to date")
        return 0

    INDEX_FILE.write_text(generated, encoding="utf-8")
    print(f"generated {INDEX_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())