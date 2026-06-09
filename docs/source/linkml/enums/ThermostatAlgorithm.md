---
search:
  boost: 2.0
---


# Enum: ThermostatAlgorithm




_Thermostat algorithm used to set the temperature in a simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/ThermostatAlgorithm](https://CCPBioSim.ac.uk/biosim-schema/ThermostatAlgorithm)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Langevin | None | A Langevin thermostat is a molecular dynamics algorithm that maintains a cons... |
| Berendsen | None | Rescales particle velocities by a factor at each step to bring the system tow... |
| Andersen | None | Stochastic approach that periodically reassigns particle velocities from a Ma... |
| Nose-Hoover | None | A deterministic method that introduces a fictitious friction variable into th... |
| Bussi | None | The Bussi-Donadio-Parrinello (CSVR) is a stochastic velocity rescaling thermo... |




## Slots

| Name | Description |
| ---  | --- |
| [thermostat_algorithm](../slots/thermostat_algorithm.md) | List of thermostat algorithms used in the simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: ThermostatAlgorithm
description: Thermostat algorithm used to set the temperature in a simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Langevin:
    text: Langevin
    description: A Langevin thermostat is a molecular dynamics algorithm that maintains
      a constant temperature (canonical ensemble, NVT) by adding a viscous friction
      force and a random noise force to Newton's equations of motion. It simulates
      interaction with a heat bath, where the damping term removes energy and the
      random force inputs energy to reach equilibrium.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: ntt
          value: 3
  Berendsen:
    text: Berendsen
    description: Rescales particle velocities by a factor at each step to bring the
      system toward the target temperature.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: tcoupl
          value:
          - berendsen
          - v-rescale
        - engine: amber
          key: ntt
          value: 1
  Andersen:
    text: Andersen
    description: Stochastic approach that periodically reassigns particle velocities
      from a Maxwell-Boltzmann distribution, simulating collisions with a heat bath.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: tcoupl
          value:
          - andersen
          - andersen-massive
        - engine: amber
          key: ntt
          value: 2
  Nose-Hoover:
    text: Nose-Hoover
    description: A deterministic method that introduces a fictitious friction variable
      into the system's dynamics to achieve the desired temperature (NVT ensemble).
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: tcoupl
          value: nose-hoover
        - engine: amber
          key: ntt
          value:
          - 9
          - 10
    aliases:
    - Nose-Hoover
    - Nose_Hoover
  Bussi:
    text: Bussi
    description: The Bussi-Donadio-Parrinello (CSVR) is a stochastic velocity rescaling
      thermostat that corrects the pitfalls of the Berendsen thermostat, accurately
      sampling the canonical ensemble while maintaining correct dynamics.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: ntt
          value: 11
    aliases:
    - Bussi
    - Bussi-Donadio-Parrinello

```
</details>

</div>
