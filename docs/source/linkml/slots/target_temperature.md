---
search:
  boost: 5.0
---

# Slot: target_temperature


_Target/reference temperature set to reach in the simulation, given as a list (e.g. 300, 300)._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/target_temperature](https://CCPBioSim.ac.uk/biosim-schema/target_temperature)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thermostat](../classes/Thermostat.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VectorTemperatureQuantity](../classes/VectorTemperatureQuantity.md) |
| Domain Of | [Thermostat](../classes/Thermostat.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'amber', 'key': 'temp0', 'unit': 'K'}, {'engine': 'gromacs', 'key': 'ref-t', 'unit': 'K'}, {'engine': 'lammps', 'key': 'temp', 'unit': 'K'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/target_temperature |
| native | https://CCPBioSim.ac.uk/biosim-schema/target_temperature |




## LinkML Source

<details>
```yaml
name: target_temperature
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: amber
      key: temp0
      unit: K
    - engine: gromacs
      key: ref-t
      unit: K
    - engine: lammps
      key: temp
      unit: K
description: Target/reference temperature set to reach in the simulation, given as
  a list (e.g. 300, 300).
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Thermostat
range: VectorTemperatureQuantity

```
</details></div>
