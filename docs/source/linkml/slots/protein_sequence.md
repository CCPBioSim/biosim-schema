---
search:
  boost: 5.0
---

# Slot: protein_sequence


_One letter sequence for protein amino acids._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/protein_sequence](https://CCPBioSim.ac.uk/biosim-schema/protein_sequence)
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
| Regex Pattern | `^[ACDEFGHIKLMNPQRSTVWY]+$` |











## Examples

| Value |
| --- |
| DRVYIHPF |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| textarea | True |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'protein_sequence'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/protein_sequence |
| native | https://CCPBioSim.ac.uk/biosim-schema/protein_sequence |




## LinkML Source

<details>
```yaml
name: protein_sequence
annotations:
  textarea:
    tag: textarea
    value: true
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: protein_sequence
description: One letter sequence for protein amino acids.
examples:
- value: DRVYIHPF
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- MoleculeID
range: string
pattern: ^[ACDEFGHIKLMNPQRSTVWY]+$

```
</details></div>
