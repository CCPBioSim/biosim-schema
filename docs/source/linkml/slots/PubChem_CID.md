---
search:
  boost: 5.0
---

# Slot: PubChem_CID


_PubChem CID of chemical molecules and their activities against biological assays._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/PubChem_CID](https://CCPBioSim.ac.uk/biosim-schema/PubChem_CID)

## Inheritance

* [identifier](../slots/identifier.md)
    * **PubChem_CID**






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
| Regex Pattern | `^\d+$` |









## Aliases


* PubChem CID



## Examples

| Value |
| --- |
| 100101 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| database | PubChem |
| prefix | pubchem.compound |
| base_uri | https://identifiers.org/pubchem.compound: |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/PubChem_CID |
| native | https://CCPBioSim.ac.uk/biosim-schema/PubChem_CID |




## LinkML Source

<details>
```yaml
name: PubChem_CID
annotations:
  database:
    tag: database
    value: PubChem
  prefix:
    tag: prefix
    value: pubchem.compound
  base_uri:
    tag: base_uri
    value: 'https://identifiers.org/pubchem.compound:'
description: PubChem CID of chemical molecules and their activities against biological
  assays.
examples:
- value: '100101'
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
aliases:
- PubChem CID
rank: 1000
is_a: identifier
domain_of:
- MoleculeID
range: string
pattern: ^\d+$

```
</details></div>
