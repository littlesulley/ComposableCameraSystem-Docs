#!/usr/bin/env python3
"""Split moxygen's monolithic api.md into per-class files and build a category index."""

import os
import re
import shutil
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent.parent
SRC = Path(os.environ.get("API_MD", REPO / "api.md"))
DST = REPO / "docs" / "reference" / "api"

# Wipe & recreate
if DST.exists():
    shutil.rmtree(DST)
DST.mkdir(parents=True)

text = SRC.read_text(encoding="utf-8")

# Split into sections: everything from one `^## ` to the next (or EOF)
# Also capture the preamble (before first `^## `)
pattern = re.compile(r"^## (.+)$", re.MULTILINE)
matches = list(pattern.finditer(text))

def extend_back(start: int) -> int:
    """Walk backwards past blank lines and `{#anchor}` lines that belong to this header."""
    # Walk to previous non-blank line(s) and absorb any `{#...}` lines that sit just above
    i = start
    while i > 0 and text[i - 1] == "\n":
        i -= 1
    # Now at end of previous line. Walk back line-by-line, absorbing {#..} and blank lines.
    while True:
        # Find start of the previous line
        line_end = i
        line_start = text.rfind("\n", 0, line_end - 1) + 1 if line_end > 0 else 0
        prev_line = text[line_start:line_end]
        stripped = prev_line.strip()
        if stripped == "":
            i = line_start
            continue
        if stripped.startswith("{#") and stripped.endswith("}"):
            i = line_start
            continue
        break
    return i

preamble_end = extend_back(matches[0].start()) if matches else len(text)
preamble = text[:preamble_end]

sections = []
starts = [extend_back(m.start()) for m in matches]
for i, m in enumerate(matches):
    title = m.group(1).strip()
    start = starts[i]
    end = starts[i + 1] if i + 1 < len(starts) else len(text)
    body = text[start:end]
    sections.append((title, body))

# Category routing — order matters (first match wins)
def categorize(title: str) -> str:
    t = title
    # Non-class special sections
    if t == "Enumerations":
        return "enumerations"
    if t == "Functions":
        return "free-functions"
    # Strip template params for matching
    bare = re.sub(r"<.*>", "", t).strip()
    # Interfaces
    if bare.startswith("I") and bare[1:2].isupper():
        return "interfaces"
    # Actors
    if bare.startswith("A") and bare[1:2].isupper():
        return "actors"
    # UObject-derived routing by suffix
    if bare.startswith("U"):
        if "TypeAsset" in bare or "DataAsset" in bare or "ProjectSettings" in bare or "TransitionTable" in bare or "NodeModifierData" in bare:
            return "data-assets"
        if bare.endswith("Transition") or "Transition" in bare:
            # Must come after DataAsset above
            if "DataAsset" not in bare:
                return "transitions"
        if "Interpolator" in bare:
            return "interpolators"
        if "Modifier" in bare:
            return "modifiers"
        if bare.endswith("Action") or "Action" in bare:
            return "actions"
        if "Spline" in bare:
            return "splines"
        if bare.endswith("Node"):
            return "nodes"
        if "BlueprintLibrary" in bare or "BlueprintCameraNode" in bare:
            return "blueprint"
        if bare in ("UComposableCameraDirector", "UComposableCameraContextStack",
                    "UComposableCameraEvaluationTree", "UComposableCameraModifierManager"):
            return "core"
        if "CurveEvaluator" in bare:
            return "async-actions"
        return "uobjects-other"
    # Templates
    if bare.startswith("T") and bare[1:2].isupper():
        return "templates"
    # Structs
    if bare.startswith("F") and bare[1:2].isupper():
        return "structs"
    # Everything else (helper classes without UE prefix)
    return "helpers"

# Map sections to files
def slugify(title: str) -> str:
    # For filename — keep ASCII, replace template angle brackets/spaces
    s = re.sub(r"<.*>", "", title).strip()
    s = re.sub(r"[^A-Za-z0-9_\-]", "_", s)
    return s

# Deduplicate: moxygen sometimes emits multiple sections for the same class (template specializations).
# We concat them under one file per slug.
file_groups: dict[str, list[tuple[str, str]]] = defaultdict(list)
section_to_cat: dict[str, str] = {}

for title, body in sections:
    cat = categorize(title)
    slug = slugify(title)
    file_groups[slug].append((title, body))
    section_to_cat[slug] = cat

# Build set of all slugs for link rewriting
# moxygen anchors look like {#lowercase} — we need to map each anchor to its file.
# Collect anchor -> slug map
anchor_to_slug: dict[str, str] = {}
anchor_re = re.compile(r"\{#([a-z0-9_\-]+)\}")
for slug, items in file_groups.items():
    for _title, body in items:
        for m in anchor_re.finditer(body):
            anchor = m.group(1)
            # Only assign if not already assigned (first wins, which is the class-level anchor)
            anchor_to_slug.setdefault(anchor, slug)

# Also preamble anchors
for m in anchor_re.finditer(preamble):
    anchor_to_slug.setdefault(m.group(1), "index")

def rewrite_links(content: str, current_slug: str) -> str:
    """Rewrite [text](#anchor) -> [text](<file>.md#anchor) or keep local if same file."""
    def repl(m: re.Match) -> str:
        text = m.group(1)
        anchor = m.group(2)
        target_slug = anchor_to_slug.get(anchor)
        if target_slug is None:
            # Unknown anchor — leave as-is (will be a broken link, but at least visible)
            return m.group(0)
        if target_slug == current_slug:
            return f"[{text}](#{anchor})"
        # Cross-file: from <cat>/<slug>.md to <cat2>/<target>.md
        cur_cat = section_to_cat.get(current_slug, "")
        tgt_cat = section_to_cat.get(target_slug, "")
        if target_slug == "index":
            return f"[{text}](../index.md#{anchor})"
        if cur_cat == tgt_cat:
            return f"[{text}]({target_slug}.md#{anchor})"
        return f"[{text}](../{tgt_cat}/{target_slug}.md#{anchor})"

    return re.sub(r"\[([^\]]+)\]\(#([a-z0-9_\-]+)\)", repl, content)

# Write each file
cat_to_files: dict[str, list[tuple[str, str]]] = defaultdict(list)  # cat -> [(title, slug)]

for slug, items in file_groups.items():
    cat = section_to_cat[slug]
    cat_dir = DST / cat
    cat_dir.mkdir(parents=True, exist_ok=True)
    # Concat bodies (for template specialization aggregations)
    primary_title = items[0][0]
    body_parts = [b for _t, b in items]
    # Demote the first `## ` to `# ` for the single-page layout, leave subsequent `## ` as-is for continuations
    combined = body_parts[0]
    # Demote the first `## Title` line to `# Title` so MkDocs renders it as page H1.
    # The anchor `{#...}` may sit above it — walk past that.
    combined = re.sub(r"^(## )", "# ", combined, count=1, flags=re.MULTILINE)
    for extra in body_parts[1:]:
        # For continuations (shouldn't normally happen after slugify), keep their `## ` heading
        combined += "\n\n" + extra
    combined = rewrite_links(combined, slug)
    # Merge moxygen's `{#anchor}` lines into their following heading so mkdocs' attr_list picks them up.
    # Pattern: {#id}\n\n#### Heading   ->   #### Heading { #id }
    combined = re.sub(
        r"\{#([A-Za-z0-9_\-]+)\}\n+(#+ [^\n]+)",
        lambda m: f"{m.group(2)} {{ #{m.group(1)} }}",
        combined,
    )
    # Same for the page-level `# Title` that absorbed the preceding `{#...}`
    combined = re.sub(
        r"\{#([A-Za-z0-9_\-]+)\}\n+(# [^\n]+)",
        lambda m: f"{m.group(2)} {{ #{m.group(1)} }}",
        combined,
    )
    # Demote moxygen's per-method `#### Parameters` and `#### Returns` subheadings
    # to bold labels — they share the `####` level with method names, which causes
    # them to interleave in the page TOC. Bolding keeps the visual affordance but
    # removes the noise from the TOC. Also force surrounding blank lines: heading
    # syntax doesn't need them, bold text does, otherwise the label collapses into
    # the previous paragraph.
    combined = re.sub(
        r"^#### (Parameters|Returns)[ \t]*\n",
        r"\n**\1**\n\n",
        combined,
        flags=re.MULTILINE,
    )
    # ── Post-processing: fix doxygen paragraph-collapse artefacts ────────────
    #
    # Doxygen treats blank-line-separated doc-comment paragraphs correctly, but
    # it collapses *within* a paragraph — so a C++ comment written as:
    #
    #   * Section title
    #   * ─────────────
    #   * Body text here...
    #
    # produces a single <para> whose text is:
    #   "Section title ─────────────── Body text here..."
    #
    # Fix 1 — ASCII-underline headings.
    # Pattern: "Title words ─{5,} rest of paragraph"
    # Convert to: "**Title words**\n\nrest of paragraph"
    combined = re.sub(
        r"([^─\n]+?) ─{5,}\s*",
        lambda m: f"**{m.group(1).rstrip()}**\n\n",
        combined,
    )
    #
    # Fix 2 — Spurious [UE](#ue) namespace links.
    # Doxygen resolves "UE" in prose as a ref to namespace UE, producing
    # [UE](#ue) in the moxygen output. The anchor is never defined in our
    # per-page files, so it renders as a broken in-page link. Strip it to
    # plain text.
    combined = re.sub(r"\[UE\]\(#ue\)", "UE", combined)
    # ──────────────────────────────────────────────────────────────────────────
    # Collapse any runs of 3+ newlines we just introduced back to 2.
    combined = re.sub(r"\n{3,}", "\n\n", combined)
    out_path = cat_dir / f"{slug}.md"
    out_path.write_text(combined, encoding="utf-8")
    cat_to_files[cat].append((primary_title, slug))

# Sort each category
for cat in cat_to_files:
    cat_to_files[cat].sort(key=lambda x: x[0])

# Generate index.md
CAT_ORDER = [
    ("core",           "Core Runtime",    "Context stack, evaluation tree, director, modifier manager."),
    ("actors",         "Actors",          "`AActor`-derived classes shipped with the plugin."),
    ("nodes",          "Camera Nodes",    "Every `UComposableCamera*Node` — the building blocks of composed cameras."),
    ("transitions",    "Transitions",     "Pose-blending transitions (`UComposableCamera*Transition`)."),
    ("modifiers",      "Modifiers",       "Player-camera-level modifiers applied after evaluation."),
    ("interpolators",  "Interpolators",   "Spring, damper, and IIR interpolator primitives."),
    ("splines",        "Splines",         "Spline types used by spline-guided nodes and transitions."),
    ("actions",        "Actions",         "Scheduled camera actions (async / latent)."),
    ("async-actions",  "Async Curve Evaluators", "Async Blueprint-latent curve evaluators."),
    ("data-assets",    "Data Assets",     "Type assets, transition tables, project settings, node modifier data."),
    ("blueprint",      "Blueprint API",   "Blueprint function library and Blueprint-authorable camera node base."),
    ("interfaces",     "Interfaces",      "`UINTERFACE` / `IInterface` contract types."),
    ("templates",      "Templates",       "Template helpers and typed interpolator wrappers."),
    ("structs",        "Structs",         "USTRUCTs — init params, pose records, parameter blocks, etc."),
    ("uobjects-other", "Other UObjects",  "UObject-derived types that don't fit a more specific category."),
    ("helpers",        "Helpers",         "Non-reflected helper classes and inertializer primitives."),
    ("enumerations",   "Enumerations",    "All `enum class` types."),
    ("free-functions", "Free Functions",  "Top-level macros and non-member functions."),
]

index_lines = [
    "# API Reference",
    "",
    "Auto-generated C++ reference for the ComposableCameraSystem plugin runtime module.",
    "",
    "!!! info \"Regeneration\"",
    "    This section is regenerated from the plugin headers via Doxygen + moxygen. The source of truth is the code; this page mirrors it.",
    "",
]

for cat, heading, blurb in CAT_ORDER:
    if cat not in cat_to_files:
        continue
    index_lines.append(f"## {heading}")
    index_lines.append("")
    index_lines.append(blurb)
    index_lines.append("")
    for title, slug in cat_to_files[cat]:
        index_lines.append(f"- [`{title}`]({cat}/{slug}.md)")
    index_lines.append("")

(DST / "index.md").write_text("\n".join(index_lines), encoding="utf-8")

# Report
total = sum(len(v) for v in cat_to_files.values())
print(f"Wrote {total} API pages to {DST}")
for cat, _h, _b in CAT_ORDER:
    if cat in cat_to_files:
        print(f"  {cat:20s} {len(cat_to_files[cat]):4d}")
