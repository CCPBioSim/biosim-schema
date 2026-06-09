---
search:
  boost: 2.0
---


# Enum: CpuArchitecture




_CPU architecture used by the compute nodes._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/CpuArchitecture](https://CCPBioSim.ac.uk/biosim-schema/CpuArchitecture)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| x86 | None | x86 architecture |
| ARM | None | ARM architecture |




## Slots

| Name | Description |
| ---  | --- |
| [CPU_architecture](../slots/CPU_architecture.md) | CPU instruction-set architecture of the compute nodes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: CpuArchitecture
description: CPU architecture used by the compute nodes.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  x86:
    text: x86
    description: x86 architecture.
  ARM:
    text: ARM
    description: ARM architecture.

```
</details>

</div>
