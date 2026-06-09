---
search:
  boost: 2.0
---


# Enum: PressureCouplingType




_Coupling type for adjusting box vectors._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/PressureCouplingType](https://CCPBioSim.ac.uk/biosim-schema/PressureCouplingType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| isotropic | None | Standard for liquids; adjusts all box vectors equally |
| semi-isotropic | None | Used for membrane simulations to allow different scaling for and axes |
| anisotropic | None | Allows individual box vector scaling, often needed for solids |
| surface tension | None | Surface tension coupling for surfaces parallel to the xy-plane |




## Slots

| Name | Description |
| ---  | --- |
| [pressure_coupling_type](../slots/pressure_coupling_type.md) | List of coupling types for adjusting box vectors |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: PressureCouplingType
description: Coupling type for adjusting box vectors.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  isotropic:
    text: isotropic
    description: Standard for liquids; adjusts all box vectors equally.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pcoupltype
          value: isotropic
        - engine: amber
          key: ntp
          value: 1
  semi-isotropic:
    text: semi-isotropic
    description: Used for membrane simulations to allow different scaling for and
      axes.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pcoupltype
          value: semiisotropic
        - engine: amber
          key: ntp
          value: 3
    aliases:
    - semi-isotropic
    - semi_isotropic
  anisotropic:
    text: anisotropic
    description: Allows individual box vector scaling, often needed for solids.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pcoupltype
          value: anisotropic
        - engine: amber
          key: ntp
          value: 2
  surface tension:
    text: surface tension
    description: Surface tension coupling for surfaces parallel to the xy-plane.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pcoupltype
          value: surface-tension
    aliases:
    - surface tension
    - surface_tension

```
</details>

</div>
