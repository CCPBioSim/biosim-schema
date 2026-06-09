---
search:
  boost: 2.0
---


# Enum: PolymerPotentialName




_Force fields used to parametrize polymers in a simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/PolymerPotentialName](https://CCPBioSim.ac.uk/biosim-schema/PolymerPotentialName)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| LignAmb25 | None | Force field that includes parameters for all common monolignol units and thei... |




## Slots

| Name | Description |
| ---  | --- |
| [polymer_potential_name](../slots/polymer_potential_name.md) | Force field used to describe polymers (excluding proteins and nucleic acids) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: PolymerPotentialName
description: Force fields used to parametrize polymers in a simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  LignAmb25:
    text: LignAmb25
    description: Force field that includes parameters for all common monolignol units
      and their associated linkages along with less commonly encountered units.

```
</details>

</div>
