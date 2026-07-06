#!/usr/bin/env python3
"""Run lightweight workflow contract checks for OpenSmartRouting."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Result:
    name: str
    passed: bool
    detail: str


def load_spec(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def file_exists(root: Path, check: dict[str, Any]) -> Result:
    target = root / check["path"]
    return Result(check["name"], target.exists(), f"{check['path']} {'exists' if target.exists() else 'is missing'}")


def glob_min(root: Path, check: dict[str, Any]) -> Result:
    matches = list(root.glob(check["pattern"]))
    minimum = int(check["min"])
    passed = len(matches) >= minimum
    return Result(check["name"], passed, f"{len(matches)} matches for {check['pattern']} (min {minimum})")


CHECKS = {
    "file_exists": file_exists,
    "glob_min": glob_min,
}


def run(root: Path, spec: dict[str, Any]) -> list[Result]:
    results: list[Result] = []
    for check in spec["checks"]:
        results.append(CHECKS[check["type"]](root, check))
    return results


def write_markdown(path: Path, results: list[Result]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Workflow Eval Report",
        "",
        "| Check | Result | Detail |",
        "|---|---|---|",
    ]
    for result in results:
        lines.append(f"| {result.name} | {'PASS' if result.passed else 'FAIL'} | {result.detail} |")
    path.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--spec", required=True)
    parser.add_argument("--report", default="ai-evals/reports/workflow-report.md")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    spec = load_spec(root / args.spec)
    results = run(root, spec)
    write_markdown(root / args.report, results)
    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
