import copy
import json
from pathlib import Path

from linkml.validator import validate


def _paths():
    repo = Path(__file__).resolve().parents[2]
    schema = repo / "biosim_schema" / "schema" / "biosim_schema.yaml"
    data = repo / "tests" / "test_validation" / "valid_data" / "test.json"
    return schema, data


def test_valid_instance_passes(monkeypatch):
    schema, data = _paths()
    monkeypatch.chdir(schema.parent)  # LinkML import resolution
    instance = json.loads(data.read_text(encoding="utf-8"))

    report = validate(instance, str(schema), "SimulationMetadata")

    assert not report.results


def test_invalid_instance_fails(monkeypatch):
    schema, data = _paths()
    monkeypatch.chdir(schema.parent)
    instance = json.loads(data.read_text(encoding="utf-8"))

    bad = copy.deepcopy(instance)
    bad["settings"]["integrator"]["number_of_steps"] = "not-an-integer"

    bad2 = copy.deepcopy(instance)
    bad2["settings"]["ensemble"]["ensemble_type"] = "NOT_A_REAL_ENUM"

    bad3 = copy.deepcopy(instance)
    bad3["settings"]["not_a_setting"] = None

    report = validate(bad, str(schema), "SimulationMetadata")
    report2 = validate(bad2, str(schema), "SimulationMetadata")
    report3 = validate(bad3, str(schema), "SimulationMetadata")

    assert report.results
    assert report2.results
    assert report3.results
