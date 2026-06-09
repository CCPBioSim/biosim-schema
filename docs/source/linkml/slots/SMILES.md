---
search:
  boost: 5.0
---

# Slot: SMILES


_Simplified Molecular Input Line Entry System (SMILES) ASCII-based line notation used to describe chemical structures. It represents molecular graphs with atoms and bonds, allowing software to convert these short strings into 2D or 3D models._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/SMILES](https://CCPBioSim.ac.uk/biosim-schema/SMILES)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MoleculeID](../classes/MoleculeID.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](../types/string.md) |
| Domain Of | [MoleculeID](../classes/MoleculeID.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[A-Za-z0-9@+\-\[\]()=#$:./\\%*]+$` |









## Aliases


* SMILES



## Examples

| Value |
| --- |
| CN1C=NC2=C1C(=O)N(C(=O)N2C)C |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'SMILES'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/SMILES |
| native | https://CCPBioSim.ac.uk/biosim-schema/SMILES |




## LinkML Source

<details>
```yaml
name: SMILES
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: SMILES
description: Simplified Molecular Input Line Entry System (SMILES) ASCII-based line
  notation used to describe chemical structures. It represents molecular graphs with
  atoms and bonds, allowing software to convert these short strings into 2D or 3D
  models.
examples:
- value: CN1C=NC2=C1C(=O)N(C(=O)N2C)C
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
aliases:
- SMILES
rank: 1000
domain_of:
- MoleculeID
range: string
pattern: ^[A-Za-z0-9@+\-\[\]()=#$:./\\%*]+$

```
</details></div>
