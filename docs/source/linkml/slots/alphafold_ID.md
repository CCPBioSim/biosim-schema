---
search:
  boost: 5.0
---

# Slot: alphafold_ID


_AlphaFold predicted protein structure identifier (AlphaFold DB, EMBL-EBI)_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/alphafold_ID](https://CCPBioSim.ac.uk/biosim-schema/alphafold_ID)

## Inheritance

* [identifier](../slots/identifier.md)
    * **alphafold_ID**






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
| Regex Pattern | `^AF-[A-Z0-9]+-F1$` |









## Aliases


* AlphaFold ID



## Examples

| Value |
| --- |
| AF-P12345-F1 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| database | AlphaFoldDB |
| base_uri | https://alphafold.ebi.ac.uk/entry/ |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/alphafold_ID |
| native | https://CCPBioSim.ac.uk/biosim-schema/alphafold_ID |




## LinkML Source

<details>
```yaml
name: alphafold_ID
annotations:
  database:
    tag: database
    value: AlphaFoldDB
  base_uri:
    tag: base_uri
    value: https://alphafold.ebi.ac.uk/entry/
description: AlphaFold predicted protein structure identifier (AlphaFold DB, EMBL-EBI)
examples:
- value: AF-P12345-F1
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
aliases:
- AlphaFold ID
rank: 1000
is_a: identifier
domain_of:
- MoleculeID
range: string
pattern: ^AF-[A-Z0-9]+-F1$

```
</details></div>
