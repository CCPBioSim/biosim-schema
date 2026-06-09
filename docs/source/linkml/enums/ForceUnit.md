---
search:
  boost: 2.0
---


# Enum: ForceUnit



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/ForceUnit](https://CCPBioSim.ac.uk/biosim-schema/ForceUnit)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| kJ/mol/nm | qudt:KiloJoulePerMoleNanometer | kilojoules per mole per nanometer |
| kcal/mol/Å | qudt:KiloCAL-PER-MOL-ANGSTROM | kilocalories per mole per angstrom |













## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: ForceUnit
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  kJ/mol/nm:
    text: kJ/mol/nm
    description: kilojoules per mole per nanometer
    meaning: qudt:KiloJoulePerMoleNanometer
    unit:
      ucum_code: kJ/mol/nm
    aliases:
    - kJ/mol/nm
    - kJ_per_mol_nm
  kcal/mol/Å:
    text: kcal/mol/Å
    description: kilocalories per mole per angstrom
    meaning: qudt:KiloCAL-PER-MOL-ANGSTROM
    unit:
      ucum_code: kcal/mol/Angstrom
    aliases:
    - kcal/mol/Å
    - kcal/mol/Ang
    - kcal/mol/Angstrom
    - kcal_per_mol_Ang

```
</details>

</div>
