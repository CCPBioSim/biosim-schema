---
search:
  boost: 5.0
---

# Slot: compressibility


_Compressibility of the simulated system, given as a float._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/compressibility](https://CCPBioSim.ac.uk/biosim-schema/compressibility)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Barostat](../classes/Barostat.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MatrixCompressibilityQuantity](../classes/MatrixCompressibilityQuantity.md) |
| Domain Of | [Barostat](../classes/Barostat.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 44.6 1e10-6 1/bar |
| 4.5e-5 1/bar |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'gromacs', 'key': 'compressibility', 'unit': '1/bar'}, {'engine': 'amber', 'key': 'comp', 'unit': '1e10-6 1/bar'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/compressibility |
| native | https://CCPBioSim.ac.uk/biosim-schema/compressibility |




## LinkML Source

<details>
```yaml
name: compressibility
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: gromacs
      key: compressibility
      unit: 1/bar
    - engine: amber
      key: comp
      unit: 1e10-6 1/bar
description: Compressibility of the simulated system, given as a float.
examples:
- value: 44.6 1e10-6 1/bar
- value: 4.5e-5 1/bar
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Barostat
range: MatrixCompressibilityQuantity

```
</details></div>
