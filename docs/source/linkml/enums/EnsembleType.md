---
search:
  boost: 2.0
---


# Enum: EnsembleType




_Ensemble used in a simulation_



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/EnsembleType](https://CCPBioSim.ac.uk/biosim-schema/EnsembleType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| NPT | None | Isothermal-isothermic ensemble (NPT) with a constant number of particles, pre... |
| NVT | None | Canonical ensemble (NVT) with a constant number of particles, volume and temp... |
| NVE | None | Microcanonical ensemble (NVE) with a constant number of particles, volume and... |
| μVT | None | Grand canonical ensemble (μVT) with constant chemical potential, volume and t... |




## Slots

| Name | Description |
| ---  | --- |
| [ensemble_type](../slots/ensemble_type.md) | List of ensemble types used in the simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: EnsembleType
description: Ensemble used in a simulation
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  NPT:
    text: NPT
    description: Isothermal-isothermic ensemble (NPT) with a constant number of particles,
      pressure and temperature.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: ntb
          value: 2
        - engine: gromacs
          key: pcoupl
          value:
          - Berendsen
          - Parrinello-Rahman
    aliases:
    - NPT
    - isothermal_isothermic_ensemble
  NVT:
    text: NVT
    description: Canonical ensemble (NVT) with a constant number of particles, volume
      and temperature.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: ntb
          value: 1
        - engine: gromacs
          key: pcoupl
          value: false
    aliases:
    - NVT
    - canonical_ensemble
  NVE:
    text: NVE
    description: Microcanonical ensemble (NVE) with a constant number of particles,
      volume and energy.
    aliases:
    - NVE
    - microcanonical_ensemble
  μVT:
    text: μVT
    description: Grand canonical ensemble (μVT) with constant chemical potential,
      volume and temperature.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: ntb
          value: 0
        - engine: amber
          key: ntt
          value: 0
        - engine: amber
          key: ntp
          value: 0
        - engine: gromacs
          key: pcoupl
          value: false
        - engine: gromacs
          key: tcoupl
          value: false
    aliases:
    - μVT
    - grand_canonical_ensemble

```
</details>

</div>
