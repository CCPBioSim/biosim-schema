---
search:
  boost: 5.0
---

# Slot: total_atom_count


_Total number of atoms in the simulation._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/total_atom_count](https://CCPBioSim.ac.uk/biosim-schema/total_atom_count)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SystemCounts](../classes/SystemCounts.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](../types/integer.md) |
| Domain Of | [SystemCounts](../classes/SystemCounts.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |











## Examples

| Value |
| --- |
| 1 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'total_atom_count'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/total_atom_count |
| native | https://CCPBioSim.ac.uk/biosim-schema/total_atom_count |




## LinkML Source

<details>
```yaml
name: total_atom_count
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: total_atom_count
description: Total number of atoms in the simulation.
examples:
- value: '1'
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- SystemCounts
range: integer
minimum_value: 0

```
</details></div>
