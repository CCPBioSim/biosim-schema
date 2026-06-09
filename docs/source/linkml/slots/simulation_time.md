---
search:
  boost: 5.0
---

# Slot: simulation_time


_Total time molecular dynamics have been sampled in a simulation trajectory, often given by the number of integration steps multiplied by the simulation time step used by the integrator, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/simulation_time](https://CCPBioSim.ac.uk/biosim-schema/simulation_time)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Integrator](../classes/Integrator.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeQuantity](../classes/TimeQuantity.md) |
| Domain Of | [Integrator](../classes/Integrator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/simulation_time |
| native | https://CCPBioSim.ac.uk/biosim-schema/simulation_time |




## LinkML Source

<details>
```yaml
name: simulation_time
description: Total time molecular dynamics have been sampled in a simulation trajectory,
  often given by the number of integration steps multiplied by the simulation time
  step used by the integrator, given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Integrator
range: TimeQuantity

```
</details></div>
