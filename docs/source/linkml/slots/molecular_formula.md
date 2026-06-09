---
search:
  boost: 5.0
---

# Slot: molecular_formula


_The molecular formula of a molecule\_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/molecular_formula](https://CCPBioSim.ac.uk/biosim-schema/molecular_formula)
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
| Regex Pattern | `^([A-Z][a-z]?\d*)+$` |











## Examples

| Value |
| --- |
| C8H10N4O2 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'molecular_formula'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/molecular_formula |
| native | https://CCPBioSim.ac.uk/biosim-schema/molecular_formula |




## LinkML Source

<details>
```yaml
name: molecular_formula
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: molecular_formula
description: The molecular formula of a molecule\
examples:
- value: C8H10N4O2
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- MoleculeID
range: string
pattern: ^([A-Z][a-z]?\d*)+$

```
</details></div>
