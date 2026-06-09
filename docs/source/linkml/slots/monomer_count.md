---
search:
  boost: 5.0
---

# Slot: monomer_count


_Number of monomeric units in a polymer(e.g. protein or nucleic acid)._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/monomer_count](https://CCPBioSim.ac.uk/biosim-schema/monomer_count)
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
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'monomer_count'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/monomer_count |
| native | https://CCPBioSim.ac.uk/biosim-schema/monomer_count |




## LinkML Source

<details>
```yaml
name: monomer_count
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: monomer_count
description: Number of monomeric units in a polymer(e.g. protein or nucleic acid).
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
