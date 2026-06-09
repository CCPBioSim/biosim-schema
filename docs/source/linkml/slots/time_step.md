---
search:
  boost: 5.0
---

# Slot: time_step


_Time between integration steps in a simulation, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/time_step](https://CCPBioSim.ac.uk/biosim-schema/time_step)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Integrator](../classes/Integrator.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeQuantity](../classes/TimeQuantity.md) |
| Domain Of | [Integrator](../classes/Integrator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* Integration Step
* Time Step
* dT




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'amber', 'key': 'dt', 'unit': 'ps'}, {'engine': 'gromacs', 'key': 'dt', 'unit': 'ps'}, {'engine': 'lammps', 'key': 'timestep', 'unit': 'fs'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/time_step |
| native | https://CCPBioSim.ac.uk/biosim-schema/time_step |




## LinkML Source

<details>
```yaml
name: time_step
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: amber
      key: dt
      unit: ps
    - engine: gromacs
      key: dt
      unit: ps
    - engine: lammps
      key: timestep
      unit: fs
description: Time between integration steps in a simulation, given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
aliases:
- Integration Step
- Time Step
- dT
rank: 1000
domain_of:
- Integrator
range: TimeQuantity

```
</details></div>
