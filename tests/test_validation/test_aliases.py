from pathlib import Path

import pytest
import yaml

SCHEMA_DIR = Path(__file__).parents[2] / "biosim_schema" / "schema"


def _alias_cases():
    """Yield schema enum values and aliases for parametrized tests."""
    for path in sorted(SCHEMA_DIR.rglob("*.yaml")):
        schema = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for enum_name, enum in (schema.get("enums") or {}).items():
            for value, spec in ((enum or {}).get("permissible_values") or {}).items():
                aliases = (spec or {}).get("aliases")
                if aliases:
                    yield pytest.param(
                        str(value),
                        aliases,
                        id=f"{path.name}::{enum_name}::{value}",
                    )


@pytest.mark.parametrize("value, aliases", _alias_cases())
def test_first_alias_matches_permissible_value(value, aliases):
    """Check that each enum's first alias matches its permissible value."""
    assert str(aliases[0]) == value, (
        f"first alias is {aliases[0]!r}, expected {value!r}"
    )
