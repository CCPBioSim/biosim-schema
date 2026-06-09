---
search:
  boost: 5.0
---

# Slot: box_dimensions


_The lengths/dimensions of the box used to simulate the system._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/box_dimensions](https://CCPBioSim.ac.uk/biosim-schema/box_dimensions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SimulationBox](../classes/SimulationBox.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VectorLengthQuantity](../classes/VectorLengthQuantity.md) |
| Domain Of | [SimulationBox](../classes/SimulationBox.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| [10, 10, 10] |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'box_dimensions', 'unit': 'Ang'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/box_dimensions |
| native | https://CCPBioSim.ac.uk/biosim-schema/box_dimensions |




## LinkML Source

<details>
```yaml
name: box_dimensions
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: box_dimensions
      unit: Ang
description: The lengths/dimensions of the box used to simulate the system.
examples:
- value: '[10, 10, 10]'
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- SimulationBox
range: VectorLengthQuantity

```
</details></div>
