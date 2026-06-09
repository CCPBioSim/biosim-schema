---
search:
  boost: 5.0
---

# Slot: molecular_weight


_The molecular weight of a molecule._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/molecular_weight](https://CCPBioSim.ac.uk/biosim-schema/molecular_weight)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MoleculeID](../classes/MoleculeID.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassQuantity](../classes/MassQuantity.md) |
| Domain Of | [MoleculeID](../classes/MoleculeID.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 18.0 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'molecular_weight', 'unit': 'g/mol'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/molecular_weight |
| native | https://CCPBioSim.ac.uk/biosim-schema/molecular_weight |




## LinkML Source

<details>
```yaml
name: molecular_weight
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: molecular_weight
      unit: g/mol
description: The molecular weight of a molecule.
examples:
- value: '18.0'
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- MoleculeID
range: MassQuantity

```
</details></div>
