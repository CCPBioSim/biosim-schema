---
search:
  boost: 5.0
---

# Slot: molecule_charge


_Electrostatic charge of a molecule._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/molecule_charge](https://CCPBioSim.ac.uk/biosim-schema/molecule_charge)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MoleculeID](../classes/MoleculeID.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChargeQuantity](../classes/ChargeQuantity.md) |
| Domain Of | [MoleculeID](../classes/MoleculeID.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[+-]?\d+(\.\d+)?$` |











## Examples

| Value |
| --- |
| -1.0 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'molecule_charge', 'unit': 'e'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/molecule_charge |
| native | https://CCPBioSim.ac.uk/biosim-schema/molecule_charge |




## LinkML Source

<details>
```yaml
name: molecule_charge
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: molecule_charge
      unit: e
description: Electrostatic charge of a molecule.
examples:
- value: '-1.0'
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- MoleculeID
range: ChargeQuantity
pattern: ^[+-]?\d+(\.\d+)?$

```
</details></div>
