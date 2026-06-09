---
search:
  boost: 2.0
---


# Enum: MassUnit




_Units for mass/molecular weight_



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/MassUnit](https://CCPBioSim.ac.uk/biosim-schema/MassUnit)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| g/mol | qudt:GramPerMole | grams per mole |
| Da | qudt:Dalton | daltons |













## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: MassUnit
description: Units for mass/molecular weight
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  g/mol:
    text: g/mol
    description: grams per mole
    meaning: qudt:GramPerMole
    annotations:
      ucum_code:
        tag: ucum_code
        value: g/mol
    aliases:
    - g/mol
    - g_per_mol
  Da:
    text: Da
    description: daltons
    meaning: qudt:Dalton
    aliases:
    - Da
    - dalton

```
</details>

</div>
