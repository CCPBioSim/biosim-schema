---
search:
  boost: 5.0
---

# Slot: random_seed


_Random number used to set (a) distribution of velocities across particles at the start of a simulation and (b) pseudo-random values for dynamics/couplings, given as an integer._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/random_seed](https://CCPBioSim.ac.uk/biosim-schema/random_seed)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Ensemble](../classes/Ensemble.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](../types/integer.md) |
| Domain Of | [Ensemble](../classes/Ensemble.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'amber', 'key': 'ig'}, {'engine': 'gromacs', 'key': 'ld-seed'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/random_seed |
| native | https://CCPBioSim.ac.uk/biosim-schema/random_seed |




## LinkML Source

<details>
```yaml
name: random_seed
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: amber
      key: ig
    - engine: gromacs
      key: ld-seed
description: Random number used to set (a) distribution of velocities across particles
  at the start of a simulation and (b) pseudo-random values for dynamics/couplings,
  given as an integer.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Ensemble
range: integer

```
</details></div>
