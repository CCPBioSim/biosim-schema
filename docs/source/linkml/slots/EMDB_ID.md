---
search:
  boost: 5.0
---

# Slot: EMDB_ID


_Electron Microscopy Data Bank ID_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/EMDB_ID](https://CCPBioSim.ac.uk/biosim-schema/EMDB_ID)

## Inheritance

* [identifier](../slots/identifier.md)
    * **EMDB_ID**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](../types/string.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^EMD-\d{4,5}$` |









## Aliases


* EMDB ID



## Examples

| Value |
| --- |
| EMD-1001 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| database | EMDB |
| prefix | emdb |
| base_uri | https://identifiers.org/emdb: |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/EMDB_ID |
| native | https://CCPBioSim.ac.uk/biosim-schema/EMDB_ID |




## LinkML Source

<details>
```yaml
name: EMDB_ID
annotations:
  database:
    tag: database
    value: EMDB
  prefix:
    tag: prefix
    value: emdb
  base_uri:
    tag: base_uri
    value: 'https://identifiers.org/emdb:'
description: Electron Microscopy Data Bank ID
examples:
- value: EMD-1001
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
aliases:
- EMDB ID
rank: 1000
is_a: identifier
range: string
pattern: ^EMD-\d{4,5}$

```
</details></div>
