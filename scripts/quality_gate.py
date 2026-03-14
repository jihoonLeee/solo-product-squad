#!/usr/bin/env python3
"""Run standard quality checks and persist QA evidence."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

EXECUTION_HEADING = "## 실행한 검증"
SUMMARY_HEADING = "## 결과 요약"
RISK_HEADING = "## 남은 리스크"
FINAL_DECISION_HEADING = "## 최종 결정"
FEATURE_HEADING = "## 기능 검증"
SECURITY_HEADING = "## 보안 검증"
OPS_HEADING = "## 운영 준비"
EVIDENCE_HEADING = "## 실행 증거"
BLOCKED_HEADING = "## BLOCKED 사유"


@dataclass
class Check:
    label: str
    command: str


@dataclass
class Result:
    label: str
    command: str
    status: str
    duration_seconds: float
    output_excerpt: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run quality gate checks and update QA artifacts.")
    parser.add_argument("--root", default=".", help="Workspace root that contains output/qa")
    parser.add_argument("--project-dir", required=True, help="Project directory to run checks in")
    parser.add_argument(
        "--only",
        nargs="*",
        choices=["lint", "typecheck", "build"],
        help="Run only the selected checks",
    )
    parser.add_argument("--max-output-lines", type=int, default=40, help="Maximum output lines per check")
    return parser.parse_args()


def discover_checks(project_dir: Path) -> list[Check]:
    package_json = project_dir / "package.json"
    package_data: dict[str, object] = {}
    if package_json.exists():
        package_data = json.loads(package_json.read_text(encoding="utf-8"))

    scripts = package_data.get("scripts", {}) if isinstance(package_data, dict) else {}
    checks: list[Check] = []
    if isinstance(scripts, dict) and "lint" in scripts:
        checks.append(Check("lint", "npm run lint"))
    if (project_dir / "tsconfig.json").exists():
        checks.append(Check("typecheck", "npx tsc --noEmit"))
    if isinstance(scripts, dict) and "build" in scripts:
        checks.append(Check("build", "npm run build"))
    return checks


def decode_output(raw: bytes | str | None) -> str:
    if raw is None:
        return ""
    if isinstance(raw, str):
        return raw
    for encoding in ("utf-8", "cp949", "euc-kr"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def trim_output(output: bytes | str | None, max_lines: int) -> str:
    cleaned = decode_output(output).replace("\x00", "").strip()
    if not cleaned:
        return "(no output)"

    lines = cleaned.splitlines()
    if len(lines) <= max_lines:
        return "\n".join(lines)

    omitted = len(lines) - max_lines
    return "\n".join([f"... ({omitted} lines omitted)", *lines[-max_lines:]])


def run_check(check: Check, project_dir: Path, max_output_lines: int) -> Result:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            check.command,
            cwd=project_dir,
            capture_output=True,
            text=False,
            shell=True,
            timeout=900,
        )
        duration = time.perf_counter() - started
        stdout_text = decode_output(completed.stdout)
        stderr_text = decode_output(completed.stderr)
        combined = stdout_text
        if stderr_text:
            combined = f"{stdout_text}\n[stderr]\n{stderr_text}".strip()

        status = "PASS" if completed.returncode == 0 else "FAIL"
        return Result(
            label=check.label,
            command=check.command,
            status=status,
            duration_seconds=duration,
            output_excerpt=trim_output(combined, max_output_lines),
        )
    except subprocess.TimeoutExpired as exc:
        duration = time.perf_counter() - started
        stdout_text = decode_output(exc.stdout)
        stderr_text = decode_output(exc.stderr)
        combined = f"Timed out after 900s\n{stdout_text}\n[stderr]\n{stderr_text}".strip()
        return Result(
            label=check.label,
            command=check.command,
            status="FAIL",
            duration_seconds=duration,
            output_excerpt=trim_output(combined, max_output_lines),
        )


def build_evidence_markdown(root: Path, project_dir: Path, results: list[Result]) -> tuple[str, str, list[str]]:
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    passed = [result.label for result in results if result.status == "PASS"]
    failed = [result.label for result in results if result.status != "PASS"]

    if failed:
        gate_signal = "BLOCKED"
        summary_reason = f"Automated checks failed: {', '.join(failed)}"
        risk_lines = [
            f"- Failed checks: {', '.join(failed)}",
            "- Fix the failing checks and rerun this script before handoff.",
        ]
    else:
        gate_signal = "CONDITIONAL PASS"
        summary_reason = "Automated checks passed, but manual UI/API validation is still missing."
        risk_lines = [
            "- Manual UI and API verification has not been recorded yet.",
            "- Release should remain blocked until execution logs and reviewer notes are updated.",
        ]

    lines = [
        "# Execution Evidence",
        "",
        EXECUTION_HEADING,
        f"- Run time: {timestamp}",
        f"- Workspace root: `{root}`",
        f"- Project directory: `{project_dir}`",
        f"- Automated gate signal: {gate_signal}",
        f"- Checks executed: {len(results)}",
        "",
    ]

    for result in results:
        lines.extend(
            [
                f"### {result.label}",
                f"- Status: {result.status}",
                f"- Command: `{result.command}`",
                f"- Duration: {result.duration_seconds:.1f}s",
                "- Output:",
                "```text",
                result.output_excerpt,
                "```",
                "",
            ]
        )

    lines.extend(
        [
            SUMMARY_HEADING,
            f"- Passed: {', '.join(passed) if passed else '(none)'}",
            f"- Failed: {', '.join(failed) if failed else '(none)'}",
            f"- Suggested gate signal: {gate_signal}",
            f"- Reason: {summary_reason}",
            "",
            RISK_HEADING,
            *risk_lines,
            "",
        ]
    )
    return "\n".join(lines), gate_signal, failed


def build_release_checklist(project_dir: Path, results: list[Result], gate_signal: str, failed: list[str]) -> str:
    lint_pass = any(result.label == "lint" and result.status == "PASS" for result in results)
    typecheck_pass = any(result.label == "typecheck" and result.status == "PASS" for result in results)
    build_pass = any(result.label == "build" and result.status == "PASS" for result in results)

    final_status = "BLOCKED"
    if failed:
        reason = f"Automated checks failed: {', '.join(failed)}"
        blocked_resolution = "Fix the failing checks, rerun quality_gate.py, and append new execution evidence."
    else:
        reason = "Automated checks passed, but manual UI/API/user-flow validation is still missing."
        blocked_resolution = "Record at least one manual validation pass in execution-evidence.md and update review findings before release."

    lines = [
        "# Release Checklist",
        "",
        FINAL_DECISION_HEADING,
        f"- READY / BLOCKED: {final_status}",
        f"- Reason: {reason}",
        f"- Automated gate: {gate_signal}",
        "",
        FEATURE_HEADING,
        "- [x] In-scope feature docs are present",
        f"- [{'x' if build_pass else ' '}] Production build completed",
        "- [ ] Manual UI and API flow validation recorded",
        "",
        SECURITY_HEADING,
        "- [ ] Auth and access-control checks recorded",
        "- [ ] Input validation and error handling reviewed",
        "- [x] No secrets were printed into release docs",
        "",
        OPS_HEADING,
        f"- [{'x' if build_pass else ' '}] Core pages compiled in production build",
        "- [ ] Monitoring and alerting expectations reviewed",
        "- [ ] Runbook or rollback notes updated",
        "",
        EVIDENCE_HEADING,
        f"- Test results: lint={'PASS' if lint_pass else 'FAIL'}, typecheck={'PASS' if typecheck_pass else 'FAIL'}",
        f"- Build result: {'PASS' if build_pass else 'FAIL'}",
        f"- Manual validation: pending ({project_dir})",
        "",
        BLOCKED_HEADING,
        f"- Reason 1: {reason}",
        f"- Resolution: {blocked_resolution}",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    project_dir = Path(args.project_dir).resolve()
    checks = discover_checks(project_dir)
    if args.only:
        requested = set(args.only)
        checks = [check for check in checks if check.label in requested]

    if not checks:
        print("No quality checks discovered.", file=sys.stderr)
        return 1

    results = [run_check(check, project_dir, args.max_output_lines) for check in checks]
    evidence_markdown, gate_signal, failed = build_evidence_markdown(root, project_dir, results)
    release_markdown = build_release_checklist(project_dir, results, gate_signal, failed)

    qa_dir = root / "output" / "qa"
    qa_dir.mkdir(parents=True, exist_ok=True)
    (qa_dir / "execution-evidence.md").write_text(evidence_markdown, encoding="utf-8")
    (qa_dir / "release-checklist.md").write_text(release_markdown, encoding="utf-8")

    for result in results:
        print(f"[{result.status}] {result.label}: {result.command}")

    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())

