import json

from biosim_schema.fieldextraction.extract_webform_fields import WebFormFieldExtractor


def _write_json(tmp_path, payload):
    path = tmp_path / "schema.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_extract_primitive_slot_with_ui_annotations(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["simulation_notes"]}],
        "slots": [
            {
                "name": "simulation_notes",
                "range": "string",
                "description": "Free-text notes",
                "annotations": [
                    {"tag": "textarea", "value": True},
                    {"tag": "base_uri", "value": "https://example.org/note"},
                    {"tag": "extracted_only", "value": True},
                    {"tag": "ui_readonly", "value": True},
                    {"tag": "source", "value": "md.log"},
                ],
            }
        ],
        "enums": [],
    }
    path = _write_json(tmp_path, schema)

    result = WebFormFieldExtractor(str(path)).extract()

    field = result["simulation_notes"]
    assert field["type"] == "textarea"
    assert field["typehint"] == "string"
    assert field["hint"] == "Free-text notes"
    assert field["base_uri"] == "https://example.org/note"
    assert field["extracted_only"] is True
    assert field["readonly"] is True
    assert field["source"] == "md.log"


def test_extract_enum_slot_with_multivalue(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["analysis_method"]}],
        "slots": [
            {"name": "analysis_method", "range": "AnalysisMethod", "multivalued": True}
        ],
        "enums": [
            {
                "name": "AnalysisMethod",
                "description": "Analysis methods",
                "permissible_values": [
                    {"text": "RMSD"},
                    {"text": "PCA"},
                ],
            }
        ],
    }
    path = _write_json(tmp_path, schema)

    result = WebFormFieldExtractor(str(path)).extract()

    field = result["analysis_method"]
    assert field["type"] == "select"
    assert field["multiple"] is True
    assert field["options"] == ["RMSD", "PCA"]
    assert field["hint"] == "Analysis methods"


def test_extract_nested_class_fields(tmp_path):
    schema = {
        "classes": [
            {"name": "SimulationMetadata", "slots": ["settings"]},
            {"name": "SimulationSettings", "slots": ["random_seed"]},
        ],
        "slots": [
            {
                "name": "settings",
                "range": "SimulationSettings",
                "description": "Simulation settings",
            },
            {"name": "random_seed", "range": "integer", "description": "Seed"},
        ],
        "enums": [],
    }
    path = _write_json(tmp_path, schema)

    result = WebFormFieldExtractor(str(path)).extract()

    settings = result["settings"]
    assert settings["type"] == "class"
    assert "random_seed" in settings["fields"]
    assert settings["fields"]["random_seed"]["typehint"] == "integer"


def test_extract_quantity_sets_vector_placeholder(tmp_path):
    schema = {
        "classes": [
            {"name": "SimulationMetadata", "slots": ["box_angles"]},
            {"name": "VectorAngleQuantity", "slots": ["vector_value", "value_unit"]},
        ],
        "slots": [
            {
                "name": "box_angles",
                "range": "VectorAngleQuantity",
                "examples": [{"value": "[90, 90, 90]", "value_unit": "degrees"}],
            },
            {"name": "vector_value", "range": "float"},
            {"name": "value_unit", "range": "AngleUnit"},
        ],
        "enums": [{"name": "AngleUnit", "permissible_values": [{"text": "degree"}]}],
    }
    path = _write_json(tmp_path, schema)

    result = WebFormFieldExtractor(str(path)).extract()

    field = result["box_angles"]["fields"]["vector_value"]
    assert field["placeholder"] == "90, 90, 90"


def test_ifabsent_default_is_unwrapped(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["simulation_software"]}],
        "slots": [
            {
                "name": "simulation_software",
                "range": "string",
                "ifabsent": "string(GROMACS)",
            }
        ],
        "enums": [],
    }
    path = _write_json(tmp_path, schema)

    result = WebFormFieldExtractor(str(path)).extract()

    assert result["simulation_software"]["default"] == "GROMACS"


def test_boolean_slot_becomes_checkbox(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["replica"]}],
        "slots": [
            {"name": "replica", "range": "boolean", "description": "Replica run"}
        ],
        "enums": [],
    }
    path = _write_json(tmp_path, schema)

    result = WebFormFieldExtractor(str(path)).extract()

    assert result["replica"]["type"] == "checkbox"
    assert result["replica"]["typehint"] == "boolean"


def test_unknown_range_returns_unknown_type(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["mystery"]}],
        "slots": [{"name": "mystery", "range": "NotAType"}],
        "enums": [],
    }
    path = _write_json(tmp_path, schema)

    result = WebFormFieldExtractor(str(path)).extract()

    assert result["mystery"]["type"] == "unknown"
