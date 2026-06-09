---
search:
  boost: 5.0
---

# Slot: minimisation_distance_step_size


_The distance the algorithm moves in a single step, controls how large a step the optimizer takes during the initial phase of minimizing the potential energy of a structure, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/minimisation_distance_step_size](https://CCPBioSim.ac.uk/biosim-schema/minimisation_distance_step_size)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Minimisation](../classes/Minimisation.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LengthQuantity](../classes/LengthQuantity.md) |
| Domain Of | [Minimisation](../classes/Minimisation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'amber', 'key': 'dx0', 'unit': 'Å'}, {'engine': 'gromacs', 'key': 'emstep', 'unit': 'nm'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/minimisation_distance_step_size |
| native | https://CCPBioSim.ac.uk/biosim-schema/minimisation_distance_step_size |




## LinkML Source

<details>
```yaml
name: minimisation_distance_step_size
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: amber
      key: dx0
      unit: Å
    - engine: gromacs
      key: emstep
      unit: nm
description: The distance the algorithm moves in a single step, controls how large
  a step the optimizer takes during the initial phase of minimizing the potential
  energy of a structure, given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Minimisation
range: LengthQuantity
minimum_value: 0

```
</details></div>
