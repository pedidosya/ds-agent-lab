#!/usr/bin/env python3

"""
Render structured dataset documentation JSON into simple Google-Doc-friendly text.

Usage:
    python render_doc.py docs/dataset_documentation.json docs/dataset_documentation.txt
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


SECTION_EMOJIS = {
    "Executive summary": "📌",
    "Dataset purpose": "🎯",
    "Final output": "🧱",
    "Model objective": "🤖",
    "Target definition": "🧪",
    "SQL pipeline overview": "🔁",
    "Source tables": "📚",
    "Features": "📊",
    "Filters and joins": "🔗",
    "Assumptions and risks": "⚠️",
    "Recommended checks": "✅",
    "Owner notes": "📝",
}


def as_text(value: Any, default: str = "Not detected") -> str:
    if value is None:
        return default
    value = str(value).strip()
    return value if value else default


def clean(value: Any) -> str:
    """Normalize whitespace and remove manual line breaks."""
    return " ".join(as_text(value, "").split())


def heading(title: str) -> str:
    emoji = SECTION_EMOJIS.get(title, "")
    return f"{emoji} {title}".strip()


def doc_title(value: Any) -> str:
    return f"📄 {as_text(value, 'Dataset Documentation')}"


def kv(label: str, value: Any) -> str:
    return f"• {label}: {as_text(value)}"


def bullet(value: Any) -> str:
    return f"• {clean(value)}"


def render_final_output(data: dict[str, Any]) -> str:
    final_output = data.get("final_output", {}) or {}
    return "\n".join([
        heading("Final output"),
        kv("Final table", final_output.get("final_table")),
        kv("Output type", final_output.get("output_type")),
        kv("Dataset grain", final_output.get("dataset_grain")),
        kv("Partitioning", final_output.get("partitioning")),
        kv("Clustering", final_output.get("clustering")),
    ])


def render_target_definition(data: dict[str, Any]) -> str:
    target = data.get("target_definition", {}) or {}

    if not target:
        return "\n".join([
            heading("Target definition"),
            "No explicit target column was detected in the SQL.",
        ])

    return "\n".join([
        heading("Target definition"),
        kv("Target column", target.get("target_column")),
        kv("Target type", target.get("target_type")),
        kv("Positive class", target.get("positive_class")),
        kv("Aggregation level", target.get("aggregation_level")),
        kv("Caveats", target.get("caveats")),
    ])


def render_pipeline(data: dict[str, Any]) -> str:
    items = data.get("sql_pipeline_overview", []) or []
    lines = [heading("SQL pipeline overview")]

    if not items:
        lines.append("No SQL pipeline blocks were detected.")
        return "\n".join(lines)

    for idx, item in enumerate(items, start=1):
        block_name = as_text(item.get("block_name"), f"Block {idx}")
        purpose = clean(item.get("purpose"))
        contribution = clean(item.get("contribution"))

        text_parts = []
        if purpose:
            text_parts.append(f"Purpose: {purpose}")
        if contribution:
            text_parts.append(f"Contribution: {contribution}")

        description = " ".join(text_parts)
        if description:
            lines.append(f"{idx}. {block_name}: {description}")
        else:
            lines.append(f"{idx}. {block_name}")

    return "\n".join(lines)


def render_source_tables(data: dict[str, Any]) -> str:
    tables = data.get("source_tables", []) or []
    lines = [heading("Source tables")]

    if not tables:
        lines.append("No source tables were detected.")
        return "\n".join(lines)

    for table in tables:
        table_name = as_text(table.get("table_name"))
        role = clean(table.get("role"))
        fields_used = clean(table.get("fields_used"))

        text = table_name
        if role:
            text += f": {role}"
        if fields_used:
            text += f" Fields used: {fields_used}"

        lines.append(f"• {text}")

    return "\n".join(lines)


def render_features(data: dict[str, Any]) -> str:
    groups = data.get("features", []) or []
    lines = [heading("Features")]

    if not groups:
        lines.append("No explicit feature groups were detected.")
        return "\n".join(lines)

    for group in groups:
        category = as_text(group.get("category"), "Feature group")
        lines.append("")
        lines.append(f"{category}:")

        items = group.get("items", []) or []
        if not items:
            lines.append("• No features listed.")
            continue

        for feature in items:
            name = as_text(feature.get("name"), "feature_name")
            meaning = clean(feature.get("meaning"))
            why = clean(feature.get("why_it_matters"))

            if meaning and why:
                lines.append(f"• {name}: {meaning} Why it matters: {why}")
            elif meaning:
                lines.append(f"• {name}: {meaning}")
            else:
                lines.append(f"• {name}")

    return "\n".join(lines)


def render_list_section(title: str, items: list[Any], empty_text: str) -> str:
    lines = [heading(title)]

    if not items:
        lines.append(empty_text)
        return "\n".join(lines)

    for item in items:
        lines.append(bullet(item))

    return "\n".join(lines)


def render_document(data: dict[str, Any]) -> str:
    sections = [
        doc_title(data.get("title")),
        "",
        heading("Executive summary"),
        clean(data.get("executive_summary")),
        "",
        heading("Dataset purpose"),
        clean(data.get("dataset_purpose")),
        "",
        render_final_output(data),
        "",
        heading("Model objective"),
        clean(data.get("model_objective")),
        "",
        render_target_definition(data),
        "",
        render_pipeline(data),
        "",
        render_source_tables(data),
        "",
        render_features(data),
        "",
        render_list_section(
            "Filters and joins",
            data.get("filters_and_joins", []) or [],
            "No filters or joins were documented.",
        ),
        "",
        render_list_section(
            "Assumptions and risks",
            data.get("assumptions_and_risks", []) or [],
            "No assumptions or risks were documented.",
        ),
        "",
        render_list_section(
            "Recommended checks",
            data.get("recommended_checks", []) or [],
            "No recommended checks were documented.",
        ),
        "",
        render_list_section(
            "Owner notes",
            data.get("owner_notes", []) or [],
            "No owner notes were documented.",
        ),
    ]

    rendered = "\n".join(str(part).rstrip() for part in sections if part is not None)

    while "\n\n\n" in rendered:
        rendered = rendered.replace("\n\n\n", "\n\n")

    return rendered.strip() + "\n"


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "Usage: python render_doc.py <input_json_path> <output_text_path>",
            file=sys.stderr,
        )
        return 1

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Input JSON file not found: {input_path}", file=sys.stderr)
        return 1

    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    rendered_text = render_document(data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered_text, encoding="utf-8")

    print(f"Rendered documentation written to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())