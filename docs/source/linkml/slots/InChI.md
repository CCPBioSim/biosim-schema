---
search:
  boost: 5.0
---

# Slot: InChI


_The International Chemical Identifier (InChi) is a textual identifier for chemical substances, designed to provide a standard way to encode molecular information_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/InChI](https://CCPBioSim.ac.uk/biosim-schema/InChI)
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
| Regex Pattern | `^InChI=1S?/[A-Za-z0-9.+\-]+(/[a-z][^/]*)*$` |









## Aliases


* InChI



## Examples

| Value |
| --- |
| InChI=1S/C8H10N4O2/c1-10-4-9-6-5(10)7(13)12(3)8(14)11(6)2/h4H,1-3H3 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'InChI'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/InChI |
| native | https://CCPBioSim.ac.uk/biosim-schema/InChI |




## LinkML Source

<details>
```yaml
name: InChI
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: InChI
description: The International Chemical Identifier (InChi) is a textual identifier
  for chemical substances, designed to provide a standard way to encode molecular
  information
examples:
- value: InChI=1S/C8H10N4O2/c1-10-4-9-6-5(10)7(13)12(3)8(14)11(6)2/h4H,1-3H3
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
aliases:
- InChI
rank: 1000
domain_of:
- MoleculeID
range: string
pattern: ^InChI=1S?/[A-Za-z0-9.+\-]+(/[a-z][^/]*)*$

```
</details></div>
