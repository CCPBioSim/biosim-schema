---
search:
  boost: 5.0
---

# Slot: average_volume_vector


_Average volume sampled from the simulation, given as a list, (e.g. 10, 10, 10)._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/average_volume_vector](https://CCPBioSim.ac.uk/biosim-schema/average_volume_vector)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SimulationAverages](../classes/SimulationAverages.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VectorVolumeQuantity](../classes/VectorVolumeQuantity.md) |
| Domain Of | [SimulationAverages](../classes/SimulationAverages.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': ['Box-X', 'Box-Y', 'Box-Z'], 'unit': 'nm'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/average_volume_vector |
| native | https://CCPBioSim.ac.uk/biosim-schema/average_volume_vector |




## LinkML Source

<details>
```yaml
name: average_volume_vector
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key:
      - Box-X
      - Box-Y
      - Box-Z
      unit: nm
description: Average volume sampled from the simulation, given as a list, (e.g. 10,
  10, 10).
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- SimulationAverages
range: VectorVolumeQuantity

```
</details></div>
