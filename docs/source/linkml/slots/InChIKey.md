---
search:
  boost: 5.0
---

# Slot: InChIKey


_The condensed, 27 character InChIKey, which is a hashed version of the full InChI (using the SHA-256 algorithm), designed to allow for easy web searches of chemical compounds._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/InChIKey](https://CCPBioSim.ac.uk/biosim-schema/InChIKey)

## Inheritance

* [identifier](../slots/identifier.md)
    * **InChIKey**






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
| Regex Pattern | `^[A-Z]{14}-[A-Z]{10}(-[A-Z])?$` |









## Aliases


* InChIKey



## Examples

| Value |
| --- |
| RYYVLZVUVIJVGH-UHFFFAOYSA-N |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| database | IUPAC |
| prefix | inchikey |
| base_uri | https://identifiers.org/inchikey: |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'InChIKey'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/InChIKey |
| native | https://CCPBioSim.ac.uk/biosim-schema/InChIKey |




## LinkML Source

<details>
```yaml
name: InChIKey
annotations:
  database:
    tag: database
    value: IUPAC
  prefix:
    tag: prefix
    value: inchikey
  base_uri:
    tag: base_uri
    value: 'https://identifiers.org/inchikey:'
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: InChIKey
description: The condensed, 27 character InChIKey, which is a hashed version of the
  full InChI (using the SHA-256 algorithm), designed to allow for easy web searches
  of chemical compounds.
examples:
- value: RYYVLZVUVIJVGH-UHFFFAOYSA-N
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
aliases:
- InChIKey
rank: 1000
is_a: identifier
domain_of:
- MoleculeID
range: string
pattern: ^[A-Z]{14}-[A-Z]{10}(-[A-Z])?$

```
</details></div>
