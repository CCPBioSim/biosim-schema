---
search:
  boost: 5.0
---

# Slot: friction_coefficient


_Usually used in the Langevin thermostat, the friction coefficient determines the strength of coupling between a system and a heat bath, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/friction_coefficient](https://CCPBioSim.ac.uk/biosim-schema/friction_coefficient)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thermostat](../classes/Thermostat.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FrictionCoefficientQuantity](../classes/FrictionCoefficientQuantity.md) |
| Domain Of | [Thermostat](../classes/Thermostat.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'bd-fric', 'unit': 'a/ps'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/friction_coefficient |
| native | https://CCPBioSim.ac.uk/biosim-schema/friction_coefficient |




## LinkML Source

<details>
```yaml
name: friction_coefficient
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: bd-fric
      unit: a/ps
description: Usually used in the Langevin thermostat, the friction coefficient determines
  the strength of coupling between a system and a heat bath, given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Thermostat
range: FrictionCoefficientQuantity

```
</details></div>
