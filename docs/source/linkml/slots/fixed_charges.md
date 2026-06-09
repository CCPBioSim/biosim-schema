---
search:
  boost: 5.0
---

# Slot: fixed_charges


_Are fixed charges on atoms included in the topology?_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/fixed_charges](https://CCPBioSim.ac.uk/biosim-schema/fixed_charges)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Particles](../classes/Particles.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [boolean](../types/boolean.md) |
| Domain Of | [Particles](../classes/Particles.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'fixed_charges'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/fixed_charges |
| native | https://CCPBioSim.ac.uk/biosim-schema/fixed_charges |




## LinkML Source

<details>
```yaml
name: fixed_charges
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: fixed_charges
description: Are fixed charges on atoms included in the topology?
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Particles
range: boolean

```
</details></div>
