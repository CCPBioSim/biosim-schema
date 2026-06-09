"""
Build simplified schema summaries from schema_webformfields.json.

Outputs:
- YAML nested summary (default behavior)
- CSV flattened summary (one row per leaf field)

CSV hierarchy rules:
- section: top-level schema section
- subsection_1/subsection_2: intermediate hierarchy levels only
- field: leaf field key (never duplicated as a subsection column)
"""

import argparse
import csv
import json
from pathlib import Path

import yaml

METADATA_KEYS = ("label", "hint", "typehint", "placeholder", "units")
"""tuple[str, ...]: Field metadata keys copied from each webform node into the summary."""


def _summarise(node):
    """Recursively extract field metadata, skipping enum fields.

    Args:
        node: A field definition dict from schema_webformfields.json.

    Returns:
        dict or None: Summarised field metadata, or None if the field is skipped.
    """

    if node.get("type") == "select":
        result = {k: node[k] for k in METADATA_KEYS if node.get(k) is not None}
        # result["options"] = node.get("options", [])
        result["typehint"] = "string"  # set enums to strings by default
        return result

    result = {k: node[k] for k in METADATA_KEYS if node.get(k) is not None}

    if "fields" in node:
        value_unit = node["fields"].get("value_unit")
        if value_unit and value_unit.get("type") == "select":
            # result["units"] = value_unit["options"]
            if value_unit.get("default"):
                result["default_unit"] = value_unit["default"]

        # hoist value/vector_value typehint directly onto parent, drop fields wrapper
        data_field = node["fields"].get("value") or node["fields"].get("vector_value")
        other_fields = {
            k: v
            for k, v in node["fields"].items()
            if k not in ("value", "vector_value", "value_unit")
        }

        if data_field and not other_fields:
            if "typehint" in data_field:
                result["typehint"] = data_field["typehint"]
            if (
                node["fields"].get("vector_value")
                and data_field.get("typehint") == "float"
            ):
                result["typehint"] = "list"
        else:
            sub = {name: _summarise(child) for name, child in node["fields"].items()}
            sub = {k: v for k, v in sub.items() if v is not None}
            if sub:
                result["fields"] = sub

    return result or None


def extract_summary(webform_json_path):
    """Extract a simplified field summary from a schema_webformfields.json file.

    Args:
        webform_json_path: Path to the schema_webformfields.json file.

    Returns:
        dict: Nested summary keyed by section then field name.
    """
    with open(webform_json_path) as f:
        schema = json.load(f)

    return {name: s for name, node in schema.items() if (s := _summarise(node))}


def _flatten_rows(node, path):
    """Flatten nested summary nodes into CSV rows.

    Args:
        node (dict): A node from the simplified summary produced by _summarise.
        path (list[str]): Hierarchy path from section to current node.
            Example leaf path: ["composition", "molecule_ID", "InChI"].

    Returns:
        list[dict]: CSV-ready rows. Internal nodes recurse; leaf nodes emit one row.

    Notes:
        - subsection columns are intermediate levels only (path[1:-1]).
        - field is always the final path element (path[-1]).
        - This avoids duplicating leaf keys in subsection columns.
    """
    rows = []
    children = node.get("fields", {})
    if children:
        for child_name, child_node in children.items():
            rows.extend(_flatten_rows(child_node, path + [child_name]))
        return rows

    # leaf field row
    subsections = path[
        1:-1
    ]  # only intermediate levels, excludes section and field name

    row = {
        "section": path[0] if path else "",
        "subsection_1": subsections[0] if len(subsections) > 0 else "",
        # "subsection_2": subsections[1] if len(subsections) > 1 else "",
        "field": path[-1] if path else "",
        "field_name": node.get("label", ""),
        "help_text": node.get("hint", ""),
        "placeholder_text": node.get("placeholder", ""),
        "default_unit": node.get("default_unit", ""),
        "data_type": node.get("typehint", ""),
    }
    return [row]


def write_summary_csv(summary, output_path):
    """Write the flattened schema summary to CSV.

    Args:
        summary (dict): Nested summary from extract_summary().
        output_path (str): Destination CSV path.

    CSV columns:
        section, subsection_1, field,
        field_name, help_text, placeholder_text, default_unit, data_type
    """
    rows = []
    for section_name, section_node in summary.items():
        rows.extend(_flatten_rows(section_node, [section_name]))

    fieldnames = [
        "section",
        "subsection_1",
        "field",
        "field_name",
        "help_text",
        "placeholder_text",
        "default_unit",
        "data_type",
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# =========================
# ENTRY POINT
# =========================


def parse_args():
    """Parses CLI arguments for summary extraction.

    Returns:
        argparse.Namespace: Parsed arguments containing:
            webschema: Path to schema_webformfields.json.
            yamloutput: Optional YAML output path. Default is schema_summary.yaml
    """
    parser = argparse.ArgumentParser(
        description="Extract engine mappings from a webform fields schema."
    )
    parser.add_argument("webschema", help="Path to webform fields json schema file")
    parser.add_argument("--yamloutput", "-o", help="Yaml output file path")
    return parser.parse_args()


def main():
    """Runs summary extraction and writes YAML and CSV outputs.

    Side Effects:
        Writes a YAML summary to --yamloutput (or schema_summary.yaml).
        Writes a CSV summary next to the YAML output using a .csv suffix.
    """
    args = parse_args()

    # summary from the webform fields
    summary = extract_summary(args.webschema)

    # output as yaml
    yaml_path = (
        Path(args.yamloutput) if args.yamloutput else Path("schema_summary.yaml")
    )
    with open(yaml_path, "w") as f:
        yaml.dump(
            summary, f, default_flow_style=False, allow_unicode=True, sort_keys=True
        )

    # flatten and output as csv
    csv_path = yaml_path.with_suffix(".csv")
    write_summary_csv(summary, str(csv_path))


if __name__ == "__main__":
    main()
