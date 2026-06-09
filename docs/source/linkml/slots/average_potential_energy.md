---
search:
  boost: 5.0
---

# Slot: average_potential_energy


_Average potential energy sampled from the simulation, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/average_potential_energy](https://CCPBioSim.ac.uk/biosim-schema/average_potential_energy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SimulationAverages](../classes/SimulationAverages.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MolarEnergyQuantity](../classes/MolarEnergyQuantity.md) |
| Domain Of | [SimulationAverages](../classes/SimulationAverages.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'Potential', 'unit': 'kJ/mol'}, {'engine': 'amber', 'key': 'EPtot', 'unit': 'kcal/mol'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/average_potential_energy |
| native | https://CCPBioSim.ac.uk/biosim-schema/average_potential_energy |




## LinkML Source

<details>
```yaml
name: average_potential_energy
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: Potential
      unit: kJ/mol
    - engine: amber
      key: EPtot
      unit: kcal/mol
description: Average potential energy sampled from the simulation, given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- SimulationAverages
range: MolarEnergyQuantity

```
</details></div>
