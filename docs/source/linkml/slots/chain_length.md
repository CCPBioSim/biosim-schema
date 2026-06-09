---
search:
  boost: 5.0
---

# Slot: chain_length


_Usually required in the Nosé-Hoover thermostat, the chain length (e.g., nh-chain-length in GROMACS) is used to maintain canonical distribution, given as an integer._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/chain_length](https://CCPBioSim.ac.uk/biosim-schema/chain_length)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thermostat](../classes/Thermostat.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](../types/integer.md) |
| Domain Of | [Thermostat](../classes/Thermostat.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'amber', 'key': 'nhc_chain_length'}, {'engine': 'gromacs', 'key': 'nh-chain-length'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/chain_length |
| native | https://CCPBioSim.ac.uk/biosim-schema/chain_length |




## LinkML Source

<details>
```yaml
name: chain_length
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: amber
      key: nhc_chain_length
    - engine: gromacs
      key: nh-chain-length
description: Usually required in the Nosé-Hoover thermostat, the chain length (e.g.,
  nh-chain-length in GROMACS) is used to maintain canonical distribution, given as
  an integer.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Thermostat
range: integer
minimum_value: 0

```
</details></div>
