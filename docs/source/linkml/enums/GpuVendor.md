---
search:
  boost: 2.0
---


# Enum: GpuVendor




_Vendor of the GPU used in the compute nodes._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/GpuVendor](https://CCPBioSim.ac.uk/biosim-schema/GpuVendor)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Nvidia | None | Nvidia GPU |
| AMD | None | AMD GPU |
| Intel | None | Intel GPU |
| None | None | No GPU present |




## Slots

| Name | Description |
| ---  | --- |
| [GPU_vendor](../slots/GPU_vendor.md) | GPU vendor used by the compute nodes, if applicable |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: GpuVendor
description: Vendor of the GPU used in the compute nodes.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Nvidia:
    text: Nvidia
    description: Nvidia GPU.
  AMD:
    text: AMD
    description: AMD GPU.
  Intel:
    text: Intel
    description: Intel GPU.
  None:
    text: None
    description: No GPU present.

```
</details>

</div>
