---
search:
  boost: 5.0
---

# Slot: electrostatic_cutoff_distance


_Distance in Angstrom at which a electrostatic interaction is turned off and a long-range non-bonded method is turned on, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/electrostatic_cutoff_distance](https://CCPBioSim.ac.uk/biosim-schema/electrostatic_cutoff_distance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Interactions](../classes/Interactions.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LengthQuantity](../classes/LengthQuantity.md) |
| Domain Of | [Interactions](../classes/Interactions.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 10 Å |
| 1.2 nm |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'rcoulomb', 'unit': 'nm'}, {'engine': 'amber', 'key': 'cut', 'unit': 'Å'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/electrostatic_cutoff_distance |
| native | https://CCPBioSim.ac.uk/biosim-schema/electrostatic_cutoff_distance |




## LinkML Source

<details>
```yaml
name: electrostatic_cutoff_distance
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: rcoulomb
      unit: nm
    - engine: amber
      key: cut
      unit: Å
description: Distance in Angstrom at which a electrostatic interaction is turned off
  and a long-range non-bonded method is turned on, given as a float.
examples:
- value: 10 Å
- value: 1.2 nm
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Interactions
range: LengthQuantity

```
</details></div>
