---
search:
  boost: 5.0
---

# Slot: average_temperature


_Average temperature sampled from the simulation, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/average_temperature](https://CCPBioSim.ac.uk/biosim-schema/average_temperature)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SimulationAverages](../classes/SimulationAverages.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TemperatureQuantity](../classes/TemperatureQuantity.md) |
| Domain Of | [SimulationAverages](../classes/SimulationAverages.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'Temperature', 'unit': 'K'}, {'engine': 'amber', 'key': 'TEMP(K)', 'unit': 'K'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/average_temperature |
| native | https://CCPBioSim.ac.uk/biosim-schema/average_temperature |




## LinkML Source

<details>
```yaml
name: average_temperature
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: Temperature
      unit: K
    - engine: amber
      key: TEMP(K)
      unit: K
description: Average temperature sampled from the simulation, given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- SimulationAverages
range: TemperatureQuantity

```
</details></div>
