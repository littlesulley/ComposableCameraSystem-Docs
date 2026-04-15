#!/usr/bin/env python3
"""Emit the `C++ API Reference:` sub-nav YAML for mkdocs.yml, scanning docs/reference/api/."""

from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
API = REPO / "docs" / "reference" / "api"

CAT_ORDER = [
    ("core",           "Core Runtime"),
    ("actors",         "Actors"),
    ("nodes",          "Camera Nodes"),
    ("transitions",    "Transitions"),
    ("modifiers",      "Modifiers"),
    ("interpolators",  "Interpolators"),
    ("splines",        "Splines"),
    ("actions",        "Actions"),
    ("async-actions",  "Async Curve Evaluators"),
    ("data-assets",    "Data Assets"),
    ("blueprint",      "Blueprint API"),
    ("interfaces",     "Interfaces"),
    ("templates",      "Templates"),
    ("structs",        "Structs"),
    ("uobjects-other", "Other UObjects"),
    ("helpers",        "Helpers"),
    ("enumerations",   "Enumerations"),
    ("free-functions", "Free Functions"),
]

indent = "              "  # 14 spaces — matches position under `- C++ API Reference:` inside `Reference:` under `nav:`
lines = []
lines.append("          - 'C++ API Reference':")
lines.append(f"{indent}- 'Overview': reference/api/index.md")
for cat, heading in CAT_ORDER:
    cat_dir = API / cat
    if not cat_dir.is_dir():
        continue
    files = sorted(p for p in cat_dir.glob("*.md"))
    if not files:
        continue
    lines.append(f"{indent}- '{heading}':")
    for f in files:
        title = f.stem
        rel = f"reference/api/{cat}/{f.name}"
        lines.append(f"{indent}  - '{title}': {rel}")

print("\n".join(lines))
