---
search:
  boost: 2.0
---


# Enum: BarostatAlgorithm




_Barostat algorithm used to set the pressure in a simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/BarostatAlgorithm](https://CCPBioSim.ac.uk/biosim-schema/BarostatAlgorithm)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Berendsen | None | Rescales the system volume and (optionally) the atoms coordinates within the ... |
| Andersen | None | Includes an additional degree of freedom, the volume of a simulation cell |
| Parrinello-Rahman | None | Extension of the Andersen method allowing changes in the shape of the simulat... |
| Nose-Hoover | None | Couples the system to a virtual "pressure bath" to control the simulation vol... |
| Monte Carlo | None | Maintain constant pressure by periodically attempting to scale the simulation... |
| Martyna-Tuckerman-Tobias-Klein | None | The MTTK barostat is an extension of the Nose-Hoover and Nose-Hoover chain th... |




## Slots

| Name | Description |
| ---  | --- |
| [barostat_algorithm](../slots/barostat_algorithm.md) | List of barostat algorithms used in the simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: BarostatAlgorithm
description: Barostat algorithm used to set the pressure in a simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Berendsen:
    text: Berendsen
    description: Rescales the system volume and (optionally) the atoms coordinates
      within the simulation box every timestep via weak coupling between the internal
      pressure and pressure.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pcoupl
          value:
          - Berendsen
          - C-rescale
        - engine: gromacs
          key: barostat
          value: 1
  Andersen:
    text: Andersen
    description: Includes an additional degree of freedom, the volume of a simulation
      cell. Volume adjusts itself to equalize the internal and external pressure.
  Parrinello-Rahman:
    text: Parrinello-Rahman
    description: Extension of the Andersen method allowing changes in the shape of
      the simulation cell.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pcoupl
          value: Parrinello-Rahman
    aliases:
    - Parrinello-Rahman
    - Parrinello_Rahman
  Nose-Hoover:
    text: Nose-Hoover
    description: Couples the system to a virtual "pressure bath" to control the simulation
      volume using extended Lagrangian dynamics.
    aliases:
    - Nose-Hoover
    - Nose_Hoover
  Monte Carlo:
    text: Monte Carlo
    description: Maintain constant pressure by periodically attempting to scale the
      simulation box size using random numbers.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: barostat
          value: 2
    aliases:
    - Monte Carlo
    - Monte_Carlo
  Martyna-Tuckerman-Tobias-Klein:
    text: Martyna-Tuckerman-Tobias-Klein
    description: The MTTK barostat is an extension of the Nose-Hoover and Nose-Hoover
      chain thermostat, acting as a modified Andersen barostat to control pressure
      by coupling the system to a virtual volume bath.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: pcoupl
          value: MTTK
    aliases:
    - Martyna-Tuckerman-Tobias-Klein
    - Martyna_Tuckerman_Tobias_Klein

```
</details>

</div>
