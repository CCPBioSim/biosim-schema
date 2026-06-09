---
search:
  boost: 2.0
---


# Enum: NodeType




_Type of compute node used in the system._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/NodeType](https://CCPBioSim.ac.uk/biosim-schema/NodeType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| CPU only | None | Node with CPUs only |
| GPU Accelerated | None | Node with one or more GPUs available |
| Hybrid CPU GPU | None | Node combining CPU and GPU resources |




## Slots

| Name | Description |
| ---  | --- |
| [node_type](../slots/node_type.md) | Compute node profile used for the simulation run |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: NodeType
description: Type of compute node used in the system.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  CPU only:
    text: CPU only
    description: Node with CPUs only.
  GPU Accelerated:
    text: GPU Accelerated
    description: Node with one or more GPUs available.
  Hybrid CPU GPU:
    text: Hybrid CPU GPU
    description: Node combining CPU and GPU resources.

```
</details>

</div>
