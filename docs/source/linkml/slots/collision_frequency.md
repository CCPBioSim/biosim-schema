---
search:
  boost: 5.0
---

# Slot: collision_frequency


_Collision frequency for the integrator, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/collision_frequency](https://CCPBioSim.ac.uk/biosim-schema/collision_frequency)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thermostat](../classes/Thermostat.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FrequencyQuantity](../classes/FrequencyQuantity.md) |
| Domain Of | [Thermostat](../classes/Thermostat.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'amber', 'key': 'gamma_ln', 'unit': '1/ps'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/collision_frequency |
| native | https://CCPBioSim.ac.uk/biosim-schema/collision_frequency |




## LinkML Source

<details>
```yaml
name: collision_frequency
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: amber
      key: gamma_ln
      unit: 1/ps
description: Collision frequency for the integrator, given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Thermostat
range: FrequencyQuantity

```
</details></div>
