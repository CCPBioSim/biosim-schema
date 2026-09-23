from importlib import resources


def schema_yaml_path() -> str:
    return str(resources.files("biosim_schema.schema") / "biosim_schema.yaml")


def engine_mappings_path() -> str:
    return str(
        resources.files("biosim_schema.schema.generated") / "schema_enginemappings.json"
    )
