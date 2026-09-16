import sys
from types import SimpleNamespace

import pytest

from biosim_schema.fieldextraction import generate_marshmallow as mod


class View:
    def __init__(self):
        self.slots = {
            ("Root", "child"): SimpleNamespace(
                range="Child", multivalued=False, array=None, required=True
            ),
            ("Root", "tags"): SimpleNamespace(
                range="string",
                multivalued=True,
                array=SimpleNamespace(maximum_number_dimensions=2),
                required=False,
            ),
            ("Child", "kind"): SimpleNamespace(
                range="Kind", multivalued=False, array=None, required=False
            ),
            ("Child", "count"): SimpleNamespace(
                range="integer", multivalued=False, array=None, required=True
            ),
        }
        self.classes = {
            "Root": SimpleNamespace(tree_root=True),
            "Child": SimpleNamespace(tree_root=False),
        }
        self.enums = {
            "Kind": SimpleNamespace(permissible_values={"a": None, "b": None})
        }

    def induced_slot(self, name, cls):
        return self.slots[(cls, name)]

    def get_class(self, name):
        return self.classes.get(name)

    def get_enum(self, name):
        return self.enums.get(name)

    def class_slots(self, name):
        return [key[1] for key in self.slots if key[0] == name]

    def all_classes(self, imports=True):
        return self.classes


def generator():
    result = object.__new__(mod.MarshmallowGenerator)
    result.view = View()
    result.builds = {}
    return result


def test_field_rendering_covers_nested_enum_and_lists():
    """Renders nested, enum, primitive, required, and list fields."""
    gen = generator()

    nested = gen._field_and_mapping_for_slot("Root", "child")
    listed = gen._field_and_mapping_for_slot("Root", "tags")
    enum = gen._field_and_mapping_for_slot("Child", "kind")

    assert "Nested(ChildSchema" in nested[1]
    assert nested[3] == {"Child"}
    assert listed[1].count("fields.List") == 2
    assert "allow_none=True" in listed[1]
    assert "OneOf" in enum[1]
    assert enum[2] == {"type": "keyword"}


def test_generate_renders_nested_schema_and_mapping():
    """Generates schemas, mappings, and nested root fields."""
    gen = generator()

    code = gen.generate()

    assert "class ChildSchema(Schema)" in code
    assert "class RootSchema(Schema)" in code
    assert '"child": fields.Nested(ChildSchema, allow_none=True)' in code
    assert '"tags": fields.List(fields.List(SanitizedUnicode()' in code
    assert "FIELDS =" in code
    assert "MAPPING =" in code


def test_recursive_nested_mapping_breaks_cycle():
    """Stops recursive nested mappings."""
    gen = generator()
    gen.builds = {
        "Root": mod.ClassBuild(
            "Root",
            mapping={"child": {"type": "object", "_nested_class": "Child"}},
            depends_on=["Child"],
        ),
        "Child": mod.ClassBuild(
            "Child",
            mapping={"root": {"type": "object", "_nested_class": "Root"}},
            depends_on=["Root"],
        ),
    }

    gen._resolve_nested_mappings()

    assert gen.builds["Child"].mapping["root"] == {"type": "object"}


def test_ordering_and_root_errors():
    """Orders dependencies and rejects schemas without a root."""
    gen = generator()
    gen.builds = {
        "Root": mod.ClassBuild("Root", depends_on=["Child"]),
        "Child": mod.ClassBuild("Child"),
    }

    assert gen._topo_order() == ["Child", "Root"]

    gen.view.classes = {"Other": SimpleNamespace(tree_root=False)}
    with pytest.raises(ValueError, match="tree_root"):
        gen._find_tree_root()


def test_main_writes_generated_code(monkeypatch, tmp_path):
    """CLI writes generated output to the requested file."""
    output = tmp_path / "generated.py"

    class FakeGenerator:
        def __init__(self, schema):
            assert schema == "schema.yaml"

        def generate(self, root_class=None):
            assert root_class == "Root"
            return "generated"

    monkeypatch.setattr(mod, "MarshmallowGenerator", FakeGenerator)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "generate_marshmallow",
            "schema.yaml",
            "-o",
            str(output),
            "--root-class",
            "Root",
        ],
    )

    mod.main()

    assert output.read_text() == "generated"
