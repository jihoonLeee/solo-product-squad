#!/usr/bin/env python3
"""Lint consistency between agents/INDEX.md and agent metadata files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"
INDEX_FILE = AGENTS_DIR / "INDEX.md"
TABLE_ROW_RE = re.compile(r"^\|(.+)\|$")
SPECIAL_HANDOFFS = {"next iteration"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lint solo-product-squad agent metadata.")
    return parser.parse_args()


def clean_items(value: str) -> list[str]:
    cleaned = value.replace("`", "").strip()
    if not cleaned:
        return []
    return [item.strip() for item in cleaned.split(",") if item.strip()]


def parse_registry(index_path: Path) -> dict[str, dict[str, object]]:
    lines = index_path.read_text(encoding="utf-8-sig").splitlines()
    in_registry = False
    records: dict[str, dict[str, object]] = {}

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
        records[agent] = {
            "stage": stage,
            "inputs": clean_items(read_first),
            "outputs": clean_items(produces),
            "handoffs": clean_items(handoff),
        }

    return records


def parse_quick_index(agent_md_path: Path) -> dict[str, object]:
    text = agent_md_path.read_text(encoding="utf-8-sig")
    stage_match = re.search(r"^- Stage owner: `([^`]+)`", text, re.MULTILINE)
    inputs_match = re.search(r"^- Read first: (.+)$", text, re.MULTILINE)
    outputs_match = re.search(r"^- Produces: (.+)$", text, re.MULTILINE)
    handoffs_match = re.search(r"^- Hands off to: (.+)$", text, re.MULTILINE)
    return {
        "has_quick_index": "## Quick Index" in text,
        "stage": stage_match.group(1) if stage_match else None,
        "inputs": clean_items(inputs_match.group(1)) if inputs_match else [],
        "outputs": clean_items(outputs_match.group(1)) if outputs_match else [],
        "handoffs": clean_items(handoffs_match.group(1)) if handoffs_match else [],
    }


def parse_agentcard(agentcard_path: Path) -> tuple[str | None, list[str]]:
    lines = agentcard_path.read_text(encoding="utf-8-sig").splitlines()
    name: str | None = None
    handoff_targets: list[str] = []
    in_handoff = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("name:") and name is None:
            name = stripped.split(":", 1)[1].strip().strip('"')
            continue
        if stripped == "handoff:":
            in_handoff = True
            continue
        if in_handoff and stripped and not line.startswith("  "):
            in_handoff = False
        if in_handoff and stripped.startswith("- target:"):
            handoff_targets.append(stripped.split(":", 1)[1].strip().strip('"'))

    return name, handoff_targets


def parse_tool_names(tools_path: Path) -> list[str]:
    lines = tools_path.read_text(encoding="utf-8-sig").splitlines()
    return [line.strip().split(":", 1)[1].strip().strip('"') for line in lines if line.strip().startswith("- name:")]


def main() -> int:
    parse_args()
    errors: list[str] = []

    if not INDEX_FILE.exists():
        print(f"missing index file: {INDEX_FILE}")
        return 1

    registry = parse_registry(INDEX_FILE)
    agent_dirs = sorted([path for path in AGENTS_DIR.iterdir() if path.is_dir()])
    agent_names = {path.name for path in agent_dirs}

    for agent_name in sorted(registry):
        if agent_name not in agent_names:
            errors.append(f"index references missing agent directory: {agent_name}")

    for agent_dir in agent_dirs:
        agent_name = agent_dir.name
        if agent_name not in registry:
            errors.append(f"agent missing from index: {agent_name}")
            continue

        agent_md = agent_dir / "AGENT.md"
        agentcard = agent_dir / "agentcard.yaml"
        tools = agent_dir / "tools.yaml"
        for required in (agent_md, agentcard, tools):
            if not required.exists():
                errors.append(f"missing required file for {agent_name}: {required.name}")

        if not agent_md.exists() or not agentcard.exists() or not tools.exists():
            continue

        quick_index = parse_quick_index(agent_md)
        if not quick_index["has_quick_index"]:
            errors.append(f"{agent_name}: AGENT.md missing Quick Index section")
        if quick_index["stage"] != registry[agent_name]["stage"]:
            errors.append(f"{agent_name}: Quick Index stage '{quick_index['stage']}' does not match INDEX stage '{registry[agent_name]['stage']}'")
        for key in ("inputs", "outputs", "handoffs"):
            if not quick_index[key]:
                errors.append(f"{agent_name}: Quick Index missing {key}")

        card_name, card_handoffs = parse_agentcard(agentcard)
        if card_name != agent_name:
            errors.append(f"{agent_name}: agentcard name '{card_name}' does not match directory name")

        for target in registry[agent_name]["handoffs"]:
            if target in SPECIAL_HANDOFFS:
                continue
            if target not in agent_names:
                errors.append(f"{agent_name}: INDEX handoff target does not exist as agent: {target}")
            if target not in card_handoffs:
                errors.append(f"{agent_name}: INDEX handoff target missing from agentcard: {target}")

        tool_names = parse_tool_names(tools)
        if "file_read" not in tool_names:
            errors.append(f"{agent_name}: tools.yaml missing file_read")
        if "file_write" not in tool_names:
            errors.append(f"{agent_name}: tools.yaml missing file_write")

    if errors:
        print("agent index lint failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"agent index lint passed ({len(agent_dirs)} agents)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
