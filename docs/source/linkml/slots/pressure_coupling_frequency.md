---
search:
  boost: 5.0
---

# Slot: pressure_coupling_frequency


_Step frequency to apply the barostat, given as an integer._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/pressure_coupling_frequency](https://CCPBioSim.ac.uk/biosim-schema/pressure_coupling_frequency)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Barostat](../classes/Barostat.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](../types/integer.md) |
| Domain Of | [Barostat](../classes/Barostat.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'nstpcouple'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/pressure_coupling_frequency |
| native | https://CCPBioSim.ac.uk/biosim-schema/pressure_coupling_frequency |




## LinkML Source

<details>
```yaml
name: pressure_coupling_frequency
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: nstpcouple
description: Step frequency to apply the barostat, given as an integer.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Barostat
range: integer

```
</details></div>
