#!/usr/bin/env python3
"""Print a compact digest for solo-product-squad agents."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

INDEX_FILE = Path(__file__).resolve().parent.parent / "agents" / "INDEX.md"
TABLE_ROW_RE = re.compile(r"^\|(.+)\|$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a compact digest for solo-product-squad agents.")
    parser.add_argument("--agent", help="Agent name to filter. Omit to print every agent.")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    parser.add_argument("--limit-inputs", type=int, default=3, help="Maximum number of inputs to show")
    parser.add_argument("--limit-outputs", type=int, default=3, help="Maximum number of outputs to show")
    parser.add_argument("--limit-handoffs", type=int, default=2, help="Maximum number of handoffs to show")
    return parser.parse_args()


def clean_items(value: str) -> list[str]:
    cleaned = value.replace("`", "").strip()
    if not cleaned:
        return []
    return [item.strip() for item in cleaned.split(",") if item.strip()]


def parse_registry(index_path: Path) -> list[dict[str, object]]:
    lines = index_path.read_text(encoding="utf-8").splitlines()
    in_registry = False
    records: list[dict[str, object]] = []

    for line in lines:
        if line.strip() == "## Registry":
            in_registry = True
            continue
        if in_registry and line.startswith("## "):
            break
        if not in_registry:
            continue

        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if stripped.startswith("| Agent ") or stripped.startswith("|------"):
            continue

        match = TABLE_ROW_RE.match(stripped)
        if not match:
            continue

        cells = [cell.strip() for cell in match.group(1).split("|")]
        if len(cells) != 5:
            continue

        agent, stage, read_first, produces, handoff = cells
        records.append(
            {
                "agent": agent,
                "stage": stage,
                "inputs": clean_items(read_first),
                "outputs": clean_items(produces),
                "handoffs": clean_items(handoff),
            }
        )

    return records


def limit_record(record: dict[str, object], limit_inputs: int, limit_outputs: int, limit_handoffs: int) -> dict[str, object]:
    return {
        "agent": record["agent"],
        "stage": record["stage"],
        "inputs": list(record["inputs"][:limit_inputs]),
        "outputs": list(record["outputs"][:limit_outputs]),
        "handoffs": list(record["handoffs"][:limit_handoffs]),
    }


def print_text(records: list[dict[str, object]]) -> None:
    for index, record in enumerate(records):
        if index:
            print()
        print(f"agent: {record['agent']}")
        print(f"stage: {record['stage']}")
        print("inputs:")
        for item in record["inputs"]:
            print(f"- {item}")
        print("outputs:")
        for item in record["outputs"]:
            print(f"- {item}")
        print("handoffs:")
        for item in record["handoffs"]:
            print(f"- {item}")


def main() -> int:
    args = parse_args()
    if not INDEX_FILE.exists():
        print(f"missing index file: {INDEX_FILE}", file=sys.stderr)
        return 1

    records = parse_registry(INDEX_FILE)
    if args.agent:
        records = [record for record in records if record["agent"] == args.agent]

    if not records:
        print("no agents matched", file=sys.stderr)
        return 1

    limited = [limit_record(record, args.limit_inputs, args.limit_outputs, args.limit_handoffs) for record in records]

    if args.format == "json":
        json.dump(limited, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0

    print_text(limited)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())