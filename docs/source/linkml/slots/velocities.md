---
search:
  boost: 5.0
---

# Slot: velocities


_Are per-frame velocities included in the trajectory?_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/velocities](https://CCPBioSim.ac.uk/biosim-schema/velocities)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Trajectories](../classes/Trajectories.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [boolean](../types/boolean.md) |
| Domain Of | [Trajectories](../classes/Trajectories.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'velocities'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/velocities |
| native | https://CCPBioSim.ac.uk/biosim-schema/velocities |




## LinkML Source

<details>
```yaml
name: velocities
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: velocities
description: Are per-frame velocities included in the trajectory?
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Trajectories
range: boolean

```
</details></div>
