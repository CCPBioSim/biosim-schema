"""Generate Invenio-compatible Marshmallow schemas + ES mappings from LinkML.

LinkML YAML -> SchemaView -> Marshmallow schema classes + FIELDS/MAPPING dicts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

HEADER = '''"""Generated from BioSimDB LinkML schema. DO NOT EDIT MANUALLY."""

from marshmallow import Schema, fields
from marshmallow.validate import OneOf
from marshmallow_utils.fields import SanitizedUnicode

COMMUNITY = "BioSimDB"
'''

PRIMITIVE_FIELD = {
    "string": "SanitizedUnicode()",
    "integer": "fields.Integer()",
    "float": "fields.Float()",
    "double": "fields.Float()",
    "boolean": "fields.Boolean()",
    "date": "fields.Date()",
    "datetime": "fields.DateTime()",
}

PRIMITIVE_MAPPING = {
    "string": "text",
    "integer": "integer",
    "float": "double",
    "double": "double",
    "boolean": "boolean",
    "date": "date",
    "datetime": "date",
}


def schema_class_name(linkml_class_name: str) -> str:
    return f"{linkml_class_name}Schema"


@dataclass
class ClassBuild:
    """Accumulated Marshmallow field lines + ES mapping dict for one class."""

    name: str
    field_lines: list[str] = field(default_factory=list)
    mapping: dict = field(default_factory=dict)
    depends_on: list[str] = field(default_factory=list)


class MarshmallowGenerator:
    def __init__(self, schema_path: str | Path):
        self.view = SchemaView(str(schema_path))
        self.builds: dict[str, ClassBuild] = {}

    # -- slot -> field/mapping -------------------------------------------------

    def _field_and_mapping_for_slot(self, cls_name: str, slot_name: str):
        slot = self.view.induced_slot(slot_name, cls_name)
        range_name = slot.range or "string"

        enum_def = self.view.get_enum(range_name)
        class_def = self.view.get_class(range_name)

        if class_def is not None:
            nested_name = schema_class_name(range_name)
            base_field = f"fields.Nested({nested_name})"
            base_mapping = {"type": "object", "properties": {}}  # filled in later
            depends = {range_name}
        elif enum_def is not None:
            values = list(enum_def.permissible_values.keys())
            base_field = f"fields.String(validate=OneOf({values!r}))"
            base_mapping = {"type": "keyword"}
            depends = set()
        else:
            base_field = PRIMITIVE_FIELD.get(range_name, "SanitizedUnicode()")
            base_mapping = {"type": PRIMITIVE_MAPPING.get(range_name, "text")}
            depends = set()

        if slot.multivalued:
            base_field = f"fields.List({base_field})"
            # ES: list of objects/scalars uses the same mapping as a single item

        kwargs = []
        if slot.required:
            kwargs.append("required=True")
        else:
            kwargs.append("allow_none=True")
        if kwargs:
            if base_field.endswith("()"):
                base_field = base_field[:-1] + ", ".join(kwargs) + ")"
            else:
                base_field = base_field[:-1] + ", " + ", ".join(kwargs) + ")"

        return (
            slot_name,
            base_field,
            base_mapping,
            depends,
            class_def is not None,
            range_name,
        )

    # -- one class ---------------------------------------------------------

    def _build_class(self, cls_name: str) -> ClassBuild:
        build = ClassBuild(name=cls_name)
        for slot_name in self.view.class_slots(cls_name):
            name, field_expr, mapping, depends, is_nested, range_name = (
                self._field_and_mapping_for_slot(cls_name, slot_name)
            )
            build.field_lines.append(f"    {name} = {field_expr}")
            build.mapping[name] = mapping
            for dep in depends:
                if dep not in build.depends_on:
                    build.depends_on.append(dep)
            if is_nested:
                # remember which nested class produced this mapping, filled later
                build.mapping[name]["_nested_class"] = range_name
        return build

    def build_all(self) -> None:
        for cls_name in self.view.all_classes(imports=True):
            self.builds[cls_name] = self._build_class(cls_name)
        self._resolve_nested_mappings()

    def _resolve_nested_mappings(self) -> None:
        """Backfill nested ES `properties` once all classes are built (handles recursion)."""

        def resolve(mapping: dict, seen: frozenset[str]) -> dict:
            resolved = {}
            for key, val in mapping.items():
                if not isinstance(val, dict):
                    continue
                nested_cls = val.pop("_nested_class", None)
                if nested_cls:
                    if nested_cls in seen:
                        resolved[key] = {"type": "object"}  # break recursive cycle
                    else:
                        nested_mapping = resolve(
                            self.builds[nested_cls].mapping, seen | {nested_cls}
                        )
                        resolved[key] = {"type": "object", "properties": nested_mapping}
                else:
                    resolved[key] = val
            return resolved

        for build in self.builds.values():
            build.mapping = resolve(build.mapping, frozenset({build.name}))

    # -- ordering + rendering ------------------------------------------------

    def _topo_order(self) -> list[str]:
        visited: set[str] = set()
        order: list[str] = []

        def visit(name: str, stack: tuple[str, ...]):
            if name in visited or name not in self.builds:
                return
            if name in stack:
                return  # recursive reference, break cycle
            visited.add(name)
            for dep in self.builds[name].depends_on:
                visit(dep, stack + (name,))
            order.append(name)

        for name in self.builds:
            visit(name, ())
        return order

    def render_schemas(self) -> str:
        parts = []
        for cls_name in self._topo_order():
            build = self.builds[cls_name]
            body = "\n".join(build.field_lines) or "    pass"
            parts.append(f"class {schema_class_name(cls_name)}(Schema):\n{body}\n")
        return "\n\n".join(parts)

    def render_root(self, root_class: str | None = None) -> str:
        root = root_class or self._find_tree_root()
        build = self.builds[root]

        fields_lines = []
        for slot_name in self.view.class_slots(root):
            slot = self.view.induced_slot(slot_name, root)
            if self.view.get_class(slot.range) is not None:
                nested = schema_class_name(slot.range)
                fields_lines.append(
                    f'    "{slot_name}": fields.Nested({nested}, allow_none=True),'
                )
            else:
                _, field_expr, _, _, _, _ = self._field_and_mapping_for_slot(
                    root, slot_name
                )
                fields_lines.append(f'    "{slot_name}": {field_expr},')

        fields_block = "FIELDS = {\n" + "\n".join(fields_lines) + "\n}\n"

        import json

        mapping_block = "MAPPING = " + json.dumps(build.mapping, indent=4) + "\n"
        mapping_block = mapping_block.replace(
            '"type"', '"type"'
        )  # keep as valid python dict via json (double quotes are valid py)

        return fields_block + "\n" + mapping_block

    def _find_tree_root(self) -> str:
        for cls_name, cls in self.view.all_classes(imports=True).items():
            if getattr(cls, "tree_root", False):
                return cls_name
        raise ValueError("No tree_root class found in schema")

    def generate(self, root_class: str | None = None) -> str:
        self.build_all()
        return (
            HEADER
            + "\n\n"
            + self.render_schemas()
            + "\n\n"
            + self.render_root(root_class)
        )


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schema", help="Path to root LinkML schema YAML")
    parser.add_argument("-o", "--output", required=True, help="Output .py file")
    parser.add_argument("--root-class", default=None)
    args = parser.parse_args()

    generator = MarshmallowGenerator(args.schema)
    code = generator.generate(root_class=args.root_class)
    Path(args.output).write_text(code, encoding="utf-8")


if __name__ == "__main__":
    main()
