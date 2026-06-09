---
search:
  boost: 2.0
---


# Enum: CarbohydratePotentialName




_Force fields used to parametrize carbohydrates in a simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/CarbohydratePotentialName](https://CCPBioSim.ac.uk/biosim-schema/CarbohydratePotentialName)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| GLYCAM06 | None | Parameter set for modeling carbohydrates and glycoconjugates |
| GLYCAM_06EP | None | GLYCAM-06EP parameter set for modeling carbohydrates and glycoconjugates |
| GLYCAM_06j-1 | None | An empirical biomolecular force field designed primarily for carbohydrates an... |




## Slots

| Name | Description |
| ---  | --- |
| [carbohydrate_potential_name](../slots/carbohydrate_potential_name.md) | Force field used to describe carbohydrate |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: CarbohydratePotentialName
description: Force fields used to parametrize carbohydrates in a simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  GLYCAM06:
    text: GLYCAM06
    description: Parameter set for modeling carbohydrates and glycoconjugates.
  GLYCAM_06EP:
    text: GLYCAM_06EP
    description: GLYCAM-06EP parameter set for modeling carbohydrates and glycoconjugates.
      Extends GLYCAM to simulations employing the TIP-5P water model, an additional
      set of carbohydrate parameters, GLYCAM-06EP.
  GLYCAM_06j-1:
    text: GLYCAM_06j-1
    description: An empirical biomolecular force field designed primarily for carbohydrates
      and complex glycans.

```
</details>

</div>
