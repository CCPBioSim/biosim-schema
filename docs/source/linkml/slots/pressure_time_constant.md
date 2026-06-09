---
search:
  boost: 5.0
---

# Slot: pressure_time_constant


_Time constant/step (relaxation time of pressure) used for coupling the system pressure, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/pressure_time_constant](https://CCPBioSim.ac.uk/biosim-schema/pressure_time_constant)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Barostat](../classes/Barostat.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeQuantity](../classes/TimeQuantity.md) |
| Domain Of | [Barostat](../classes/Barostat.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1.0 ps |
| 5.0 ps |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'tau-p', 'unit': 'ps'}, {'engine': 'amber', 'key': 'taup', 'unit': 'ps'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/pressure_time_constant |
| native | https://CCPBioSim.ac.uk/biosim-schema/pressure_time_constant |




## LinkML Source

<details>
```yaml
name: pressure_time_constant
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: tau-p
      unit: ps
    - engine: amber
      key: taup
      unit: ps
description: Time constant/step (relaxation time of pressure) used for coupling the
  system pressure, given as a float.
examples:
- value: 1.0 ps
- value: 5.0 ps
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Barostat
range: TimeQuantity

```
</details></div>
