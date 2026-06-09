---
search:
  boost: 2.0
---


# Enum: LongRangeInteractionMethod




_Method used to implement long-range interactions of point charges in the simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/LongRangeInteractionMethod](https://CCPBioSim.ac.uk/biosim-schema/LongRangeInteractionMethod)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Cutoff | None | Plain cut-off used to implement electrostatics |
| Ewald | None | Classical Ewald sum electrostatics |
| PME | None | Particle Mesh Ewald (PME) accelerates the traditional Ewald sum by calculatin... |
| P3M | None | Particle-Particle Particle-Mesh (P3M) is faster, more flexible alternative to... |
| FMM | None | Fast Multipole (FMM) is a highly scalable, linear complexity method that grou... |
| RF | None | Reaction Field (RF) is simpler, faster approach that approximates the effect ... |




## Slots

| Name | Description |
| ---  | --- |
| [long_range_interaction_method](../slots/long_range_interaction_method.md) | Method used to describe long-range interactions between particles |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: LongRangeInteractionMethod
description: Method used to implement long-range interactions of point charges in
  the simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Cutoff:
    text: Cutoff
    description: Plain cut-off used to implement electrostatics.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: coulombtype
          value: Cut-off
        - engine: gromacs
          key: vdwtype
          value: Cut-off
  Ewald:
    text: Ewald
    description: Classical Ewald sum electrostatics. Ewald scales as O(N3/2) and is
      thus extremely slow for large systems. In most cases PME will perform much better.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: coulombtype
          value: Ewald
        - engine: amber
          key: ew_type
          value: 1
  PME:
    text: PME
    description: Particle Mesh Ewald (PME) accelerates the traditional Ewald sum by
      calculating reciprocal space sums on a mesh grid using fast Fourier transforms
      (FFTs), yielding complexity.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: coulombtype
          value: PME
        - engine: gromacs
          key: vdwtype
          value: PME
        - engine: amber
          key: ew_type
          value: 0
  P3M:
    text: P3M
    description: Particle-Particle Particle-Mesh (P3M) is faster, more flexible alternative
      to PME that uses a numerical particle mesh for long-range and direct summation
      for short-ranges.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: coulombtype
          value: P3M-AD
  FMM:
    text: FMM
    description: Fast Multipole (FMM) is a highly scalable, linear complexity method
      that groups distant particles together, allowing the approximation of their
      interactions via multipole expansions.
  RF:
    text: RF
    description: Reaction Field (RF) is simpler, faster approach that approximates
      the effect of the long-range environment by treating it as a continuous dielectric
      medium beyond a certain cutoff, suitable for homogeneous systems.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: coulombtype
          value: Reaction-Field

```
</details>

</div>
