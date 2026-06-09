---
search:
  boost: 5.0
---

# Slot: nucleic_sequence


_One letter sequence for nucleic acid nucleotides._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/nucleic_sequence](https://CCPBioSim.ac.uk/biosim-schema/nucleic_sequence)
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
| Regex Pattern | `^[ACGTURYSWKMBDHVN]+$` |











## Examples

| Value |
| --- |
| ATGCATCGATCGATCGATCG |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| textarea | True |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'nucleic_sequence'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/nucleic_sequence |
| native | https://CCPBioSim.ac.uk/biosim-schema/nucleic_sequence |




## LinkML Source

<details>
```yaml
name: nucleic_sequence
annotations:
  textarea:
    tag: textarea
    value: true
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: nucleic_sequence
description: One letter sequence for nucleic acid nucleotides.
examples:
- value: ATGCATCGATCGATCGATCG
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- MoleculeID
range: string
pattern: ^[ACGTURYSWKMBDHVN]+$

```
</details></div>
