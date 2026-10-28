from pathlib import Path

import pytest
import yaml

SCHEMA_DIR = Path(__file__).parents[2] / "biosim_schema" / "schema"


def _unit_attribute_cases():
    """Yield each class attribute named ``value_unit`` whose range is an enum."""
    for path in sorted(SCHEMA_DIR.rglob("*.yaml")):
        schema = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        enums = set(schema.get("enums") or {})
        for class_name, cls in (schema.get("classes") or {}).items():
            attr = ((cls or {}).get("attributes") or {}).get("value_unit")
            if attr is None:
                continue
            yield pytest.param(attr, enums, id=f"{path.name}::{class_name}")


@pytest.mark.parametrize("attr, enums", _unit_attribute_cases())
def test_quantity_unit_is_required(attr, enums):
    """Check that every quantity's ``value_unit`` is a required slot with an enum
    range."""
    assert attr.get("range") in enums, f"value_unit has no unit enum range: {attr}"
    assert attr.get("required") is True, "value_unit must set `required: true`"
