---
search:
  boost: 5.0
---

# Slot: UNIPROT_ID


_UniProt accession ID_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/UNIPROT_ID](https://CCPBioSim.ac.uk/biosim-schema/UNIPROT_ID)

## Inheritance

* [identifier](../slots/identifier.md)
    * **UNIPROT_ID**






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
| Regex Pattern | `^[A-Z0-9]{6,10}$` |









## Aliases


* UNIPROT ID



## Examples

| Value |
| --- |
| P0DP23 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| database | UNIPROT |
| prefix | uniprot |
| base_uri | https://identifiers.org/uniprot: |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/UNIPROT_ID |
| native | https://CCPBioSim.ac.uk/biosim-schema/UNIPROT_ID |




## LinkML Source

<details>
```yaml
name: UNIPROT_ID
annotations:
  database:
    tag: database
    value: UNIPROT
  prefix:
    tag: prefix
    value: uniprot
  base_uri:
    tag: base_uri
    value: 'https://identifiers.org/uniprot:'
description: UniProt accession ID
examples:
- value: P0DP23
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
aliases:
- UNIPROT ID
rank: 1000
is_a: identifier
domain_of:
- MoleculeID
range: string
pattern: ^[A-Z0-9]{6,10}$

```
</details></div>
