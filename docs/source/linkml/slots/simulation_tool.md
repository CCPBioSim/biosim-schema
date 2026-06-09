---
search:
  boost: 5.0
---

# Slot: simulation_tool


_Tool used to perform simulation._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/simulation_tool](https://CCPBioSim.ac.uk/biosim-schema/simulation_tool)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Minimisation](../classes/Minimisation.md) |  |  no  |
| [Equilibration](../classes/Equilibration.md) |  |  no  |
| [Production](../classes/Production.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SimulationTool](../enums/SimulationTool.md) |
| Domain Of | [Minimisation](../classes/Minimisation.md), [Equilibration](../classes/Equilibration.md), [Production](../classes/Production.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/simulation_tool |
| native | https://CCPBioSim.ac.uk/biosim-schema/simulation_tool |




## LinkML Source

<details>
```yaml
name: simulation_tool
description: Tool used to perform simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Minimisation
- Equilibration
- Production
range: SimulationTool
multivalued: true

```
</details></div>
