import csv
import json

from biosim_schema.fieldextraction import extract_summary as mod


def _write_json(tmp_path, payload):
    path = tmp_path / "schema_webformfields.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_extract_summary_keeps_select_as_string(tmp_path):
    payload = {
        "analysis_method": {
            "type": "select",
            "label": "Analysis Method",
            "hint": "Pick one",
            "options": ["RMSD", "PCA"],
        }
    }
    json_path = _write_json(tmp_path, payload)

    summary = mod.extract_summary(str(json_path))

    assert summary["analysis_method"]["typehint"] == "string"
    assert summary["analysis_method"]["label"] == "Analysis Method"


def test_write_summary_csv_flattens_leaf_without_field_duplication(tmp_path):
    summary = {
        "composition": {
            "fields": {
                "molecule_ID": {
                    "fields": {
                        "InChI": {
                            "label": "InChI",
                            "hint": "Identifier",
                            "typehint": "string",
                        }
                    }
                }
            }
        }
    }
    csv_path = tmp_path / "summary.csv"

    mod.write_summary_csv(summary, str(csv_path))

    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 1
    row = rows[0]
    assert row["section"] == "composition"
    assert row["subsection_1"] == "molecule_ID"
    assert row["field"] == "InChI"


def test_main_writes_yaml_and_csv_next_to_yaml_output(tmp_path, monkeypatch):
    payload = {
        "sim_time": {
            "label": "Simulation Time",
            "hint": "Total sampled time",
            "typehint": "float",
        }
    }
    json_path = _write_json(tmp_path, payload)
    yaml_path = tmp_path / "schema_summary.yaml"

    monkeypatch.setattr(
        mod,
        "parse_args",
        lambda: type(
            "Args", (), {"webschema": str(json_path), "yamloutput": str(yaml_path)}
        )(),
    )

    mod.main()

    assert yaml_path.exists()
    assert yaml_path.with_suffix(".csv").exists()


def test_extract_summary_hoists_value_typehint(tmp_path):
    payload = {
        "simulation_time": {
            "fields": {
                "value": {"typehint": "float"},
                "value_unit": {"type": "select", "default": "ps"},
            }
        }
    }
    summary = mod.extract_summary(str(_write_json(tmp_path, payload)))

    assert summary["simulation_time"]["typehint"] == "float"
    assert summary["simulation_time"]["default_unit"] == "ps"
    assert "fields" not in summary["simulation_time"]


def test_extract_summary_vector_value_becomes_list(tmp_path):
    payload = {
        "box_angles": {
            "fields": {
                "vector_value": {"typehint": "float"},
                "value_unit": {"type": "select"},
            }
        }
    }
    summary = mod.extract_summary(str(_write_json(tmp_path, payload)))

    assert summary["box_angles"]["typehint"] == "list"


def test_write_summary_csv_top_level_leaf_has_empty_subsection(tmp_path):
    summary = {
        "analysis_method": {
            "label": "Analysis Method",
            "hint": "Pick one",
            "typehint": "string",
        }
    }
    csv_path = tmp_path / "summary.csv"

    mod.write_summary_csv(summary, str(csv_path))

    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 1
    assert rows[0]["section"] == "analysis_method"
    assert rows[0]["subsection_1"] == ""
    assert rows[0]["field"] == "analysis_method"
