#!/usr/bin/env python3
"""Check that the script inventory matches the repository's actual files.

This is *not* a Skript syntax validator or a runtime compatibility test.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {"Administration", "Configuration", "Cosmetics", "Economy",
              "Gameplay", "Integration", "Moderation", "Parkour"}


def validate_repository(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    manifest = root / "catalog.json"
    if not manifest.is_file():
        return ["catalog.json is missing"]

    try:
        doc = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot parse catalog.json: {exc}"]

    if not isinstance(doc, dict) or doc.get("schema_version") != 1:
        return ["catalog.json must be an object with schema_version = 1"]
    entries = doc.get("scripts")
    if not isinstance(entries, list):
        return ["catalog.json scripts must be a list"]

    recorded: set[str] = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"Entry #{index + 1} must be an object")
            continue
        path = entry.get("path")
        if not isinstance(path, str):
            errors.append(f"Entry #{index + 1} needs a string path")
            continue
        relative = Path(path)
        if (relative.is_absolute() or ".." in relative.parts or
                relative.as_posix() != path or
                len(relative.parts) != 2 or
                relative.parts[0] not in {"Misc", "Parkour"} or
                relative.suffix != ".sk"):
            errors.append(f"Invalid script path: {path!r}")
            continue
        if path in recorded:
            errors.append(f"Duplicate catalog path: {path}")
        recorded.add(path)
        if not (root / relative).is_file():
            errors.append(f"Missing script: {path}")
        for field in ("title", "summary"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                errors.append(f"Missing {field} for {path}")
        if entry.get("category") not in CATEGORIES:
            errors.append(f"Unknown category for {path}")
        if entry.get("status") != "legacy-example":
            errors.append(f"Unsupported status for {path}")
        deps = entry.get("dependencies")
        if (not isinstance(deps, list) or
                any(not isinstance(dep, str) or not dep.strip() for dep in deps)):
            errors.append(f"Invalid dependencies for {path}")

    actual = {
        p.relative_to(root).as_posix()
        for directory in ("Misc", "Parkour")
        for p in (root / directory).glob("*.sk")
    }
    for path in sorted(actual - recorded):
        errors.append(f"Script missing from catalog: {path}")
    for path in sorted(recorded - actual):
        errors.append(f"Catalog lists absent script: {path}")

    index_path = root / "docs" / "SCRIPTS.md"
    if not index_path.is_file():
        errors.append("docs/SCRIPTS.md is missing")
    else:
        index_text = index_path.read_text(encoding="utf-8")
        for path in sorted(recorded):
            if f"../{path}" not in index_text:
                errors.append(f"Script not linked in docs/SCRIPTS.md: {path}")
    return errors


if __name__ == "__main__":
    problems = validate_repository()
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        raise SystemExit(1)
    print("Catalog OK: all script files are indexed and documentation links are present.")
