---
search:
  boost: 5.0
---

# Slot: temperature_time_constant


_Time constant for coupling the system temperature in seconds units, given as a list (e.g. 300, 300)._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/temperature_time_constant](https://CCPBioSim.ac.uk/biosim-schema/temperature_time_constant)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thermostat](../classes/Thermostat.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VectorTimeQuantity](../classes/VectorTimeQuantity.md) |
| Domain Of | [Thermostat](../classes/Thermostat.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'tau-t', 'unit': 'ps'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/temperature_time_constant |
| native | https://CCPBioSim.ac.uk/biosim-schema/temperature_time_constant |




## LinkML Source

<details>
```yaml
name: temperature_time_constant
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: tau-t
      unit: ps
description: Time constant for coupling the system temperature in seconds units, given
  as a list (e.g. 300, 300).
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Thermostat
range: VectorTimeQuantity

```
</details></div>
