---
search:
  boost: 2.0
---


# Enum: LengthUnit



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/LengthUnit](https://CCPBioSim.ac.uk/biosim-schema/LengthUnit)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Å | qudt:ANGSTROM | Length units in Angstrom |
| nm | qudt:NanoM | Length units in nanometers |













## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: LengthUnit
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Å:
    text: Å
    description: Length units in Angstrom.
    meaning: qudt:ANGSTROM
    annotations:
      ucum_code:
        tag: ucum_code
        value: Angstrom
    aliases:
    - Å
    - Ang
    - Angstrom
  nm:
    text: nm
    description: Length units in nanometers.
    meaning: qudt:NanoM
    annotations:
      ucum_code:
        tag: ucum_code
        value: nm
    aliases:
    - nm

```
</details>

</div>
