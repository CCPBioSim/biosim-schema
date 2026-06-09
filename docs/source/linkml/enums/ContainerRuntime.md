---
search:
  boost: 2.0
---


# Enum: ContainerRuntime




_Container runtime used to package and run software._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/ContainerRuntime](https://CCPBioSim.ac.uk/biosim-schema/ContainerRuntime)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Apptainer | None | Apptainer/Singularity runtime common on HPC systems |
| Docker | None | Docker container runtime |
| Podman | None | Podman container runtime |
| None | None | No container runtime used |




## Slots

| Name | Description |
| ---  | --- |
| [container_runtime](../slots/container_runtime.md) | Container runtime used to execute the simulation environment, if any |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: ContainerRuntime
description: Container runtime used to package and run software.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Apptainer:
    text: Apptainer
    description: Apptainer/Singularity runtime common on HPC systems.
  Docker:
    text: Docker
    description: Docker container runtime.
  Podman:
    text: Podman
    description: Podman container runtime.
  None:
    text: None
    description: No container runtime used.

```
</details>

</div>
