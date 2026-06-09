---
search:
  boost: 5.0
---

# Slot: target_pressure


_Target/reference pressure set to reach in the simulation, given as a float or a list (e.g. 1, 1)._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/target_pressure](https://CCPBioSim.ac.uk/biosim-schema/target_pressure)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Barostat](../classes/Barostat.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MatrixPressureQuantity](../classes/MatrixPressureQuantity.md) |
| Domain Of | [Barostat](../classes/Barostat.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'ref-p', 'unit': 'bar'}, {'engine': 'amber', 'key': 'pres0', 'unit': 'bar'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/target_pressure |
| native | https://CCPBioSim.ac.uk/biosim-schema/target_pressure |




## LinkML Source

<details>
```yaml
name: target_pressure
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: ref-p
      unit: bar
    - engine: amber
      key: pres0
      unit: bar
description: Target/reference pressure set to reach in the simulation, given as a
  float or a list (e.g. 1, 1).
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Barostat
range: MatrixPressureQuantity

```
</details></div>
