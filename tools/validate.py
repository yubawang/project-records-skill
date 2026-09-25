#!/usr/bin/env python3
"""Validate the structural contract for a project-records workspace."""

from __future__ import annotations

import argparse
import re
import tempfile
from pathlib import Path

STATUS_HEADINGS = (
    "Overall Status",
    "Latest Known State",
    "Risks/Blockers",
    "Next Best Starting Point",
)
INDEX_PATH = re.compile(r"^\s*-\s*Path:\s*`([^`/]+)/`\s*$", re.MULTILINE)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    index = root / "README.md"
    if not index.is_file():
        return [f"missing canonical index: {index}"]

    paths = INDEX_PATH.findall(index.read_text(encoding="utf-8"))
    for relative in paths:
        project = root / relative
        readme = project / "README.md"
        status = project / "PROJECT_STATUS.md"
        if not project.is_dir():
            errors.append(f"index path does not exist: {relative}/")
            continue
        if not readme.is_file():
            errors.append(f"missing project README: {relative}/README.md")
        if not status.is_file():
            errors.append(f"missing project status: {relative}/PROJECT_STATUS.md")
            continue
        text = status.read_text(encoding="utf-8")
        for heading in STATUS_HEADINGS:
            if not re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE):
                errors.append(f"missing status heading: {relative}/PROJECT_STATUS.md: {heading}")
    return errors


def self_test() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "README.md").write_text("- Path: `example/`\n", encoding="utf-8")
        project = root / "example"
        project.mkdir()
        (project / "README.md").write_text("# Example\n", encoding="utf-8")
        (project / "PROJECT_STATUS.md").write_text(
            "\n".join(f"## {heading}" for heading in STATUS_HEADINGS), encoding="utf-8"
        )
        assert validate(root) == []
        (project / "PROJECT_STATUS.md").write_text("## Overall Status\n", encoding="utf-8")
        assert len(validate(root)) == len(STATUS_HEADINGS) - 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("self-check passed")
        return 0
    if args.root is None:
        parser.error("root is required unless --self-test is used")

    errors = validate(args.root)
    if errors:
        print("validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
