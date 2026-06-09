---
search:
  boost: 5.0
---

# Slot: frame_count


_Total number of snapshots that make up a trajectory._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/frame_count](https://CCPBioSim.ac.uk/biosim-schema/frame_count)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Trajectories](../classes/Trajectories.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](../types/integer.md) |
| Domain Of | [Trajectories](../classes/Trajectories.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |











## Examples

| Value |
| --- |
| 1 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'frame_count'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/frame_count |
| native | https://CCPBioSim.ac.uk/biosim-schema/frame_count |




## LinkML Source

<details>
```yaml
name: frame_count
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: frame_count
description: Total number of snapshots that make up a trajectory.
examples:
- value: '1'
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Trajectories
range: integer
minimum_value: 0

```
</details></div>
