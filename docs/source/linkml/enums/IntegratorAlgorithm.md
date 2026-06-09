---
search:
  boost: 2.0
---


# Enum: IntegratorAlgorithm




_Algorithm used to integrate the simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/IntegratorAlgorithm](https://CCPBioSim.ac.uk/biosim-schema/IntegratorAlgorithm)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Velocity-Verlet | None | Directly computes positions, velocities, and accelerations at the same time, ... |
| Leap-frog | None | Updates velocities at half-integer time steps and positions at integer time s... |
| Verlet | None | A simple, stable algorithm that uses positions at a timestep and the previous... |
| Euler | None | An Euler integrator for Brownian or position Langevin dynamics |




## Slots

| Name | Description |
| ---  | --- |
| [integrator_algorithm](../slots/integrator_algorithm.md) | List of integrator algorithms used to integrate the simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: IntegratorAlgorithm
description: Algorithm used to integrate the simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Velocity-Verlet:
    text: Velocity-Verlet
    description: Directly computes positions, velocities, and accelerations at the
      same time, facilitating kinetic energy calculation.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: integrator
          value:
          - md-vv
          - md-vv-avek
    aliases:
    - Velocity-Verlet
    - Velocity_Verlet
  Leap-frog:
    text: Leap-frog
    description: Updates velocities at half-integer time steps and positions at integer
      time steps, equivalent to Verlet but with better velocity management.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: integrator
          value:
          - md
          - sd
    aliases:
    - Leap-frog
    - Leapfrog
  Verlet:
    text: Verlet
    description: A simple, stable algorithm that uses positions at a timestep and
      the previous timestep to calculate the next position.
  Euler:
    text: Euler
    description: An Euler integrator for Brownian or position Langevin dynamics.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: integrator
          value: bd

```
</details>

</div>
