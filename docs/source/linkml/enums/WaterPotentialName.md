---
search:
  boost: 2.0
---


# Enum: WaterPotentialName




_Force fields used to parametrize water molecules in a simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/WaterPotentialName](https://CCPBioSim.ac.uk/biosim-schema/WaterPotentialName)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| OPC | None | Parameters for a water model |
| OPC3 | None | Parameters for a water model |
| OPC3POL | None | Parameters for a water model |
| POL3 | None | Parameters for a water model |
| TIP3P | None | Parameters for the force balance 3-point water model |
| TIP3PFB | None | Parameters for a water model |
| TIP4PFB | None | Parameters for a water model |
| TIP4P | None | Parameters for a water model |
| TIP5P | None | Parameters for a water model |
| TIP4PEW | None | Parameters for a water model |
| SPCE | None | Parameters for a water model |
| SPCEB | None | Parameters for a water model |
| SPC/Fw | None | SPC/Fw parameters for flexible water models, for classical dynamics |
| q-SPC/Fw | None | qSPC/Fw parameters for flexible water models, for path-integral MD |




## Slots

| Name | Description |
| ---  | --- |
| [water_potential_name](../slots/water_potential_name.md) | Force field used to describe water molecules |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: WaterPotentialName
description: Force fields used to parametrize water molecules in a simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  OPC:
    text: OPC
    description: Parameters for a water model. It is a non-polarizable, 4-point, 3-charge
      rigid water model.
  OPC3:
    text: OPC3
    description: Parameters for a water model. It is a 3-point rigid non-polarizable
      water model – as of Amber24, is the latest addition to the OPC family, constructed
      using the same philosophy as OPC.
  OPC3POL:
    text: OPC3POL
    description: Parameters for a water model. It is a new classical 3-point water
      model that explicitly accounts for electronic polarizability with minimal impact
      on computational efficiency.
  POL3:
    text: POL3
    description: Parameters for a water model.
  TIP3P:
    text: TIP3P
    description: Parameters for the force balance 3-point water model.
  TIP3PFB:
    text: TIP3PFB
    description: Parameters for a water model.
  TIP4PFB:
    text: TIP4PFB
    description: Parameters for a water model.
  TIP4P:
    text: TIP4P
    description: Parameters for a water model.
  TIP5P:
    text: TIP5P
    description: Parameters for a water model.
  TIP4PEW:
    text: TIP4PEW
    description: Parameters for a water model.
  SPCE:
    text: SPCE
    description: Parameters for a water model.
  SPCEB:
    text: SPCEB
    description: Parameters for a water model.
  SPC/Fw:
    text: SPC/Fw
    description: SPC/Fw parameters for flexible water models, for classical dynamics.
      Also known as SPF.
  q-SPC/Fw:
    text: q-SPC/Fw
    description: qSPC/Fw parameters for flexible water models, for path-integral MD.
      Also know as SPG

```
</details>

</div>
