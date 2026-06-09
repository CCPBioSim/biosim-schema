---
search:
  boost: 2.0
---


# Enum: GeneralPotentialName




_Force fields used to parametrize molecules in a simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/GeneralPotentialName](https://CCPBioSim.ac.uk/biosim-schema/GeneralPotentialName)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| gem.pmemd | None | The Amoeba force field in a multiploar/polarizable force field with parameter... |
| GAFF | None | Provides parameters for small molecules and drug-like ligands that are fully ... |
| GAFF2 | None | The second generation of GAFF for small molecules and drug-like ligands |
| OPLS | None | OPLS (Optimized Potential for Liquid Simulations) is a set of force fields de... |
| GROMOS | None | GROMOS is is a general-purpose molecular dynamics computer simulation package... |
| CHARMM | None | CHARMM (Chemistry at HARvard Macromolecular Mechanics) is a both a set of for... |




## Slots

| Name | Description |
| ---  | --- |
| [general_potential_name](../slots/general_potential_name.md) | Force field used to describe molecules |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: GeneralPotentialName
description: Force fields used to parametrize molecules in a simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  gem.pmemd:
    text: gem.pmemd
    description: The Amoeba force field in a multiploar/polarizable force field with
      parameters for water, univalent ions, small organic molecules, proteins, nucliec
      acids and ionic liquids.
  GAFF:
    text: GAFF
    description: Provides parameters for small molecules and drug-like ligands that
      are fully compatible with standard macromolecular AMBER force fields used for
      proteins and nucleic acids.
  GAFF2:
    text: GAFF2
    description: The second generation of GAFF for small molecules and drug-like ligands.
  OPLS:
    text: OPLS
    description: OPLS (Optimized Potential for Liquid Simulations) is a set of force
      fields developed by Prof. William L. Jorgensen for condensed phase simulations.
  GROMOS:
    text: GROMOS
    description: GROMOS is is a general-purpose molecular dynamics computer simulation
      package for the study of biomolecular systems. It also incorporates its own
      force field covering proteins, nucleotides, sugars etc. and can be applied to
      chemical and physical systems ranging from glasses and liquid crystals, to polymers
      and crystals and solutions of biomolecules.
  CHARMM:
    text: CHARMM
    description: CHARMM (Chemistry at HARvard Macromolecular Mechanics) is a both
      a set of force fields and a software package for molecular dynamics simulations
      and analysis. Includes united atom (CHARMM19) and all atom (CHARMM22, CHARMM27,
      CHARMM36) force fields.

```
</details>

</div>
