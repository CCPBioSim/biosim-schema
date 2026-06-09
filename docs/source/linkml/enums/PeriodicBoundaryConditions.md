---
search:
  boost: 2.0
---


# Enum: PeriodicBoundaryConditions




_What directions in a simulation cell periodic boundaries are set if they are turned on._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/PeriodicBoundaryConditions](https://CCPBioSim.ac.uk/biosim-schema/PeriodicBoundaryConditions)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| None | None | No PBC |
| xyz | None | all axes |
| xy | None | only xy plane |
| xz | None | only xz plane |
| yz | None | only yz plane |




## Slots

| Name | Description |
| ---  | --- |
| [periodic_boundary_conditions](../slots/periodic_boundary_conditions.md) | What directions in a simulation cell periodic boundaries are set if they are ... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: PeriodicBoundaryConditions
description: What directions in a simulation cell periodic boundaries are set if they
  are turned on.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  None:
    text: None
    description: No PBC
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pbc
          value: false
  xyz:
    text: xyz
    description: all axes
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pbc
          value: xyz
  xy:
    text: xy
    description: only xy plane
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pbc
          value: xy
  xz:
    text: xz
    description: only xz plane
  yz:
    text: yz
    description: only yz plane

```
</details>

</div>
