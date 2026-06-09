---
search:
  boost: 5.0
---

# Slot: box_angles


_The angles of the box used to simulate the system._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/box_angles](https://CCPBioSim.ac.uk/biosim-schema/box_angles)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SimulationBox](../classes/SimulationBox.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VectorAngleQuantity](../classes/VectorAngleQuantity.md) |
| Domain Of | [SimulationBox](../classes/SimulationBox.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| [90, 90, 90] |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'box_angles', 'unit': 'degrees'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/box_angles |
| native | https://CCPBioSim.ac.uk/biosim-schema/box_angles |




## LinkML Source

<details>
```yaml
name: box_angles
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: box_angles
      unit: degrees
description: The angles of the box used to simulate the system.
examples:
- value: '[90, 90, 90]'
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- SimulationBox
range: VectorAngleQuantity

```
</details></div>
