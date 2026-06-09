---
search:
  boost: 2.0
---


# Enum: ExecutionPlatform




_Type of platform used to run the simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/ExecutionPlatform](https://CCPBioSim.ac.uk/biosim-schema/ExecutionPlatform)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HPC Cluster | None | Shared high-performance computing cluster |
| Cloud VM | None | Cloud-hosted virtual machine |
| Local | None | Local desktop, laptop or portable workstation |




## Slots

| Name | Description |
| ---  | --- |
| [execution_platform](../slots/execution_platform.md) | Broad type of system used to run the simulation workload |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: ExecutionPlatform
description: Type of platform used to run the simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  HPC Cluster:
    text: HPC Cluster
    description: Shared high-performance computing cluster.
  Cloud VM:
    text: Cloud VM
    description: Cloud-hosted virtual machine.
  Local:
    text: Local
    description: Local desktop, laptop or portable workstation.

```
</details>

</div>
