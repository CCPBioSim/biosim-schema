---
search:
  boost: 2.0
---


# Enum: CpuVendor




_Vendor of the CPU used in the compute nodes._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/CpuVendor](https://CCPBioSim.ac.uk/biosim-schema/CpuVendor)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| AMD | None | AMD processor |
| Intel | None | Intel processor |
| ARM | None | ARM-based processor |
| Other | None | Other CPU vendor |




## Slots

| Name | Description |
| ---  | --- |
| [CPU_vendor](../slots/CPU_vendor.md) | CPU vendor used in the compute nodes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: CpuVendor
description: Vendor of the CPU used in the compute nodes.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  AMD:
    text: AMD
    description: AMD processor.
  Intel:
    text: Intel
    description: Intel processor.
  ARM:
    text: ARM
    description: ARM-based processor.
  Other:
    text: Other
    description: Other CPU vendor.

```
</details>

</div>
