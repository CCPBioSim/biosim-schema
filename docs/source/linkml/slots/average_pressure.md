---
search:
  boost: 5.0
---

# Slot: average_pressure


_Average pressure sampled from the simulation, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/average_pressure](https://CCPBioSim.ac.uk/biosim-schema/average_pressure)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SimulationAverages](../classes/SimulationAverages.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PressureQuantity](../classes/PressureQuantity.md) |
| Domain Of | [SimulationAverages](../classes/SimulationAverages.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'Pressure (bar)', 'unit': 'bar'}, {'engine': 'amber', 'key': 'PRESS', 'unit': 'bar'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/average_pressure |
| native | https://CCPBioSim.ac.uk/biosim-schema/average_pressure |




## LinkML Source

<details>
```yaml
name: average_pressure
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: Pressure (bar)
      unit: bar
    - engine: amber
      key: PRESS
      unit: bar
description: Average pressure sampled from the simulation, given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- SimulationAverages
range: PressureQuantity

```
</details></div>
