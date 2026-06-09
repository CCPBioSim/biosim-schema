---
search:
  boost: 5.0
---

# Slot: PDB_ID


_Protein Data Bank identifier_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/PDB_ID](https://CCPBioSim.ac.uk/biosim-schema/PDB_ID)

## Inheritance

* [identifier](../slots/identifier.md)
    * **PDB_ID**






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
| Regex Pattern | `^[0-9A-Za-z]{4}$` |









## Aliases


* PDB ID



## Examples

| Value |
| --- |
| 2VB1 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| database | PDB |
| prefix | pdb |
| base_uri | https://identifiers.org/pdb: |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/PDB_ID |
| native | https://CCPBioSim.ac.uk/biosim-schema/PDB_ID |




## LinkML Source

<details>
```yaml
name: PDB_ID
annotations:
  database:
    tag: database
    value: PDB
  prefix:
    tag: prefix
    value: pdb
  base_uri:
    tag: base_uri
    value: 'https://identifiers.org/pdb:'
description: Protein Data Bank identifier
examples:
- value: 2VB1
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
aliases:
- PDB ID
rank: 1000
is_a: identifier
domain_of:
- MoleculeID
range: string
pattern: ^[0-9A-Za-z]{4}$

```
</details></div>
