---
search:
  boost: 5.0
---

# Slot: molecule_count


_Number of instances of a given molecule, defined as bonded atoms or beads._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/molecule_count](https://CCPBioSim.ac.uk/biosim-schema/molecule_count)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MoleculeID](../classes/MoleculeID.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](../types/integer.md) |
| Domain Of | [MoleculeID](../classes/MoleculeID.md) |

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
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'molecule_count'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/molecule_count |
| native | https://CCPBioSim.ac.uk/biosim-schema/molecule_count |




## LinkML Source

<details>
```yaml
name: molecule_count
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: molecule_count
description: Number of instances of a given molecule, defined as bonded atoms or beads.
examples:
- value: '1'
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- MoleculeID
range: integer
minimum_value: 0

```
</details></div>
