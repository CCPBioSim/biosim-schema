---
search:
  boost: 5.0
---

# Slot: bonds


_Are bond parameters present in the topology?_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/bonds](https://CCPBioSim.ac.uk/biosim-schema/bonds)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Connectivity](../classes/Connectivity.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [boolean](../types/boolean.md) |
| Domain Of | [Connectivity](../classes/Connectivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'bonds'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/bonds |
| native | https://CCPBioSim.ac.uk/biosim-schema/bonds |




## LinkML Source

<details>
```yaml
name: bonds
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: bonds
description: Are bond parameters present in the topology?
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Connectivity
range: boolean

```
</details></div>
