---
search:
  boost: 5.0
---

# Slot: system_charge


_Total electrostatic charge of the system given by the elementary charge (e)._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/system_charge](https://CCPBioSim.ac.uk/biosim-schema/system_charge)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Particles](../classes/Particles.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChargeQuantity](../classes/ChargeQuantity.md) |
| Domain Of | [Particles](../classes/Particles.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[+-]?\d+(\.\d+)?$` |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| engine_mapping | [{'engine': 'toptrajparser', 'key': 'system_charge', 'unit': 'e'}] |




### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/system_charge |
| native | https://CCPBioSim.ac.uk/biosim-schema/system_charge |




## LinkML Source

<details>
```yaml
name: system_charge
annotations:
  engine_mapping:
    tag: engine_mapping
    value:
    - engine: toptrajparser
      key: system_charge
      unit: e
description: Total electrostatic charge of the system given by the elementary charge
  (e).
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- Particles
range: ChargeQuantity
pattern: ^[+-]?\d+(\.\d+)?$

```
</details></div>
