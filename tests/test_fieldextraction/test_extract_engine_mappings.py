import json

from biosim_schema.fieldextraction.extract_engine_mappings import MappingsExtractor


def _write_json(tmp_path, payload):
    path = tmp_path / "schema.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_extract_empty_schema_returns_empty_maps(tmp_path):
    schema = {"classes": [], "slots": [], "enums": []}
    path = _write_json(tmp_path, schema)

    result = MappingsExtractor(str(path)).extract(root_class="SimulationMetadata")

    assert result == {"forward": {}, "reverse": {}}


def test_extract_slot_engine_mapping(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["simulation_time"]}],
        "slots": [
            {
                "name": "simulation_time",
                "range": "float",
                "annotations": [
                    {
                        "tag": "engine_mapping",
                        "value": [{"engine": "gromacs", "key": "dt", "value": "0.002"}],
                    }
                ],
            }
        ],
        "enums": [],
    }
    path = _write_json(tmp_path, schema)

    result = MappingsExtractor(str(path)).extract()

    assert result["forward"]["gromacs"]["SimulationMetadata.simulation_time"] == [
        {"key": "dt", "value": "0.002"}
    ]
    assert (
        result["reverse"]["gromacs"]["dt"]["by_path"][
            "SimulationMetadata.simulation_time"
        ]
        == {}
    )


def test_extract_enum_value_mappings(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["ensemble_type"]}],
        "slots": [
            {"name": "ensemble_type", "range": "EnsembleType", "annotations": []}
        ],
        "enums": [
            {
                "name": "EnsembleType",
                "permissible_values": [
                    {
                        "text": "NVT",
                        "annotations": [
                            {
                                "tag": "engine_mapping",
                                "value": [
                                    {
                                        "engine": "gromacs",
                                        "key": "ensemble",
                                        "value": "nvt",
                                    }
                                ],
                            }
                        ],
                    },
                    {
                        "text": "NPT",
                        "annotations": [
                            {
                                "tag": "engine_mapping",
                                "value": [
                                    {
                                        "engine": "gromacs",
                                        "key": "ensemble",
                                        "value": "npt",
                                    }
                                ],
                            }
                        ],
                    },
                ],
            }
        ],
    }
    path = _write_json(tmp_path, schema)

    result = MappingsExtractor(str(path)).extract()

    path_key = "SimulationMetadata.ensemble_type"
    assert "NVT" in result["forward"]["gromacs"][path_key]
    assert "NPT" in result["forward"]["gromacs"][path_key]
    assert result["reverse"]["gromacs"]["ensemble"]["by_path"][path_key]["nvt"] == [
        "NVT"
    ]
    assert result["reverse"]["gromacs"]["ensemble"]["by_path"][path_key]["npt"] == [
        "NPT"
    ]


def _write_json(tmp_path, payload):
    path = tmp_path / "schema.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_ignores_slots_without_engine_mapping(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["a"]}],
        "slots": [{"name": "a", "range": "float", "annotations": []}],
        "enums": [],
    }
    result = MappingsExtractor(str(_write_json(tmp_path, schema))).extract()
    assert result == {"forward": {}, "reverse": {}}


def test_supports_multiple_keys_in_one_mapping(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["t"]}],
        "slots": [
            {
                "name": "t",
                "range": "float",
                "annotations": [
                    {
                        "tag": "engine_mapping",
                        "value": [
                            {
                                "engine": "gromacs",
                                "key": ["dt", "time_step"],
                                "value": "0.002",
                            }
                        ],
                    }
                ],
            }
        ],
        "enums": [],
    }
    result = MappingsExtractor(str(_write_json(tmp_path, schema))).extract()
    path_key = "SimulationMetadata.t"
    assert result["forward"]["gromacs"][path_key] == [
        {"key": "dt", "value": "0.002"},
        {"key": "time_step", "value": "0.002"},
    ]


def test_preserves_unit_in_forward_map(tmp_path):
    schema = {
        "classes": [{"name": "SimulationMetadata", "slots": ["p"]}],
        "slots": [
            {
                "name": "p",
                "range": "float",
                "annotations": [
                    {
                        "tag": "engine_mapping",
                        "value": [
                            {
                                "engine": "gromacs",
                                "key": "pcoupl",
                                "value": "berendsen",
                                "unit": "bar",
                            }
                        ],
                    }
                ],
            }
        ],
        "enums": [],
    }
    result = MappingsExtractor(str(_write_json(tmp_path, schema))).extract()
    assert result["forward"]["gromacs"]["SimulationMetadata.p"] == [
        {"key": "pcoupl", "value": "berendsen", "unit": "bar"}
    ]


def test_walks_nested_class_paths(tmp_path):
    schema = {
        "classes": [
            {"name": "SimulationMetadata", "slots": ["settings"]},
            {"name": "SimulationSettings", "slots": ["seed"]},
        ],
        "slots": [
            {"name": "settings", "range": "SimulationSettings", "annotations": []},
            {
                "name": "seed",
                "range": "integer",
                "annotations": [
                    {
                        "tag": "engine_mapping",
                        "value": [
                            {"engine": "gromacs", "key": "ld-seed", "value": "42"}
                        ],
                    }
                ],
            },
        ],
        "enums": [],
    }
    result = MappingsExtractor(str(_write_json(tmp_path, schema))).extract()
    assert result["forward"]["gromacs"]["SimulationMetadata.settings.seed"] == [
        {"key": "ld-seed", "value": "42"}
    ]
