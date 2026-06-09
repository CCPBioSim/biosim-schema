---
search:
  boost: 2.0
---


# Enum: MolarEnergyUnit




_Units for molar energy._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/MolarEnergyUnit](https://CCPBioSim.ac.uk/biosim-schema/MolarEnergyUnit)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| kcal/mol | qudt:KiloCAL-PER-MOL | kcal/mol |
| kJ/mol | qudt:KiloJ-PER-MOL | kJ/mol |













## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: MolarEnergyUnit
description: Units for molar energy.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  kcal/mol:
    text: kcal/mol
    description: kcal/mol
    meaning: qudt:KiloCAL-PER-MOL
    annotations:
      ucum_code:
        tag: ucum_code
        value: KiloCAL-PER-MOL
      has_quantity_kind:
        tag: has_quantity_kind
        value: MolarEnergy
    aliases:
    - kcal/mol
    - kcal_per_mol
  kJ/mol:
    text: kJ/mol
    description: kJ/mol
    meaning: qudt:KiloJ-PER-MOL
    unit:
      ucum_code: KiloJ-PER-MOL
      has_quantity_kind: MolarEnergy
    aliases:
    - kJ/mol
    - kJ_per_mol

```
</details>

</div>
