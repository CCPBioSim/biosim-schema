---
search:
  boost: 5.0
---

# Slot: energy_tolerance


_Tolerance energy for when minimization stops, this is when the maximum force on any atom is less than this value (default is often 1000 kJ/mol/nm or 10−4kcal), given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/energy_tolerance](https://CCPBioSim.ac.uk/biosim-schema/energy_tolerance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Minimisation](../classes/Minimisation.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ForceQuantity](../classes/ForceQuantity.md) |
| Domain Of | [Minimisation](../classes/Minimisation.md) |

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
| engine_mapping | [{'engine': 'gromacs', 'key': 'emtol', 'unit': 'kJ/mol/nm'}, {'engine': 'amber', 'key': 'drms', 'unit': '10−4 kcal/mol/Å'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/energy_tolerance |
| native | https://CCPBioSim.ac.uk/biosim-schema/energy_tolerance |




## LinkML Source

<details>
```yaml
name: energy_tolerance
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: emtol
      unit: kJ/mol/nm
    - engine: amber
      key: drms
      unit: 10−4 kcal/mol/Å
description: Tolerance energy for when minimization stops, this is when the maximum
  force on any atom is less than this value (default is often 1000 kJ/mol/nm or 10−4kcal),
  given as a float.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Minimisation
range: ForceQuantity
minimum_value: 0

```
</details></div>
