---
search:
  boost: 2.0
---


# Enum: MachineLearnedPotentialName




_Machine learned potentials._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/MachineLearnedPotentialName](https://CCPBioSim.ac.uk/biosim-schema/MachineLearnedPotentialName)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| MACE | None | Utilizes high-body-order expansions and provides exceptional force accuracy, ... |
| ANI | None | Neural network potentials specifically parameterized for organic and small-mo... |
| NequIP | None | E(3)-equivariant network that models local atomic environments as tensors |
| UMA | None | Large-scale framework spanning half a billion atomic structures, and generali... |
| AceFF | None | Specifically optimized for small molecule drug discovery |




## Slots

| Name | Description |
| ---  | --- |
| [machine_learned_potential_name](../slots/machine_learned_potential_name.md) | ML force field used to describe molecules |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: MachineLearnedPotentialName
description: Machine learned potentials.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  MACE:
    text: MACE
    description: Utilizes high-body-order expansions and provides exceptional force
      accuracy, excelling at capturing anharmonic dynamics in organic and macromolecular
      systems.
    aliases:
    - MACE
    - Multi-Atomic Cluster Expansion
  ANI:
    text: ANI
    description: Neural network potentials specifically parameterized for organic
      and small-molecule drug-like spaces (covering H, C, N, O).
    aliases:
    - ANI
    - Accurate Neural net Interaction
  NequIP:
    text: NequIP
    description: E(3)-equivariant network that models local atomic environments as
      tensors.
    aliases:
    - NequIP
    - Neural Equivariant Interatomic Potential
  UMA:
    text: UMA
    description: Large-scale framework spanning half a billion atomic structures,
      and generalizes across different chemical environments.
    aliases:
    - UMA
    - Universal Model for Atoms
  AceFF:
    text: AceFF
    description: Specifically optimized for small molecule drug discovery
    aliases:
    - AceFF

```
</details>

</div>
