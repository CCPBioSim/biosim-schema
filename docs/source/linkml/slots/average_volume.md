---
search:
  boost: 5.0
---

# Slot: average_volume


_Average volume sampled from the simulation, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/average_volume](https://CCPBioSim.ac.uk/biosim-schema/average_volume)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SimulationAverages](../classes/SimulationAverages.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VolumeQuantity](../classes/VolumeQuantity.md) |
| Domain Of | [SimulationAverages](../classes/SimulationAverages.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'amber', 'key': 'VOLUME', 'unit': 'A^3'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/average_volume |
| native | https://CCPBioSim.ac.uk/biosim-schema/average_volume |




## LinkML Source

<details>
```yaml
name: average_volume
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: amber
      key: VOLUME
      unit: A^3
description: Average volume sampled from the simulation, given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- SimulationAverages
range: VolumeQuantity

```
</details></div>
