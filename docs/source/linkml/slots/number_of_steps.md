---
search:
  boost: 5.0
---

# Slot: number_of_steps


_Number of integration steps performed in the simulation, given as an integer._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/number_of_steps](https://CCPBioSim.ac.uk/biosim-schema/number_of_steps)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Integrator](../classes/Integrator.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](../types/integer.md) |
| Domain Of | [Integrator](../classes/Integrator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'amber', 'key': 'nstlim'}, {'engine': 'gromacs', 'key': 'nsteps'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/number_of_steps |
| native | https://CCPBioSim.ac.uk/biosim-schema/number_of_steps |




## LinkML Source

<details>
```yaml
name: number_of_steps
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: amber
      key: nstlim
    - engine: gromacs
      key: nsteps
description: Number of integration steps performed in the simulation, given as an
  integer.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Integrator
range: integer

```
</details></div>
