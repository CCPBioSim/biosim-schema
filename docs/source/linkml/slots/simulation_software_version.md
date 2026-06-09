---
search:
  boost: 5.0
---

# Slot: simulation_software_version


_Version of software used to perform simulation step._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/simulation_software_version](https://CCPBioSim.ac.uk/biosim-schema/simulation_software_version)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Production](../classes/Production.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](../types/string.md) |
| Domain Of | [Production](../classes/Production.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| extracted_only | True |
| ui_readonly | True |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/simulation_software_version |
| native | https://CCPBioSim.ac.uk/biosim-schema/simulation_software_version |




## LinkML Source

<details>
```yaml
name: simulation_software_version
annotations:
  extracted_only:
    tag: extracted_only
    value: true
  ui_readonly:
    tag: ui_readonly
    value: true
description: Version of software used to perform simulation step.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Production
range: string

```
</details></div>
