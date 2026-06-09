---
search:
  boost: 5.0
---

# Slot: minimisation


_Minimisation stage of a simulation._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/minimisation](https://CCPBioSim.ac.uk/biosim-schema/minimisation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SimulationStages](../classes/SimulationStages.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Minimisation](../classes/Minimisation.md) |
| Domain Of | [SimulationStages](../classes/SimulationStages.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'amber', 'key': 'imin', 'value': 1}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/minimisation |
| native | https://CCPBioSim.ac.uk/biosim-schema/minimisation |




## LinkML Source

<details>
```yaml
name: minimisation
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: amber
      key: imin
      value: 1
description: Minimisation stage of a simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- SimulationStages
range: Minimisation

```
</details></div>
