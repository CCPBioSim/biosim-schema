---
search:
  boost: 2.0
---


# Enum: MinimisationAlgorithm




_Algorithm used to minimise particle interactions._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/MinimisationAlgorithm](https://CCPBioSim.ac.uk/biosim-schema/MinimisationAlgorithm)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Steepest Descent | None | Moves atoms in the opposite direction of the energy gradient (forces) |
| Conjugate Gradient | None | Uses both current gradient information and previous search directions to find... |
| L-BFGS | None | L-BFGS (Limited-memory Broyden–Fletcher–Goldfarb–Shanno) approximates the inv... |
| XMIN | None | Minimization algorithm used to relax molecular structures to their lowest pot... |
| LMOD | None | LMOD (Low-Mode) minimization is a specialized conformational search and energ... |




## Slots

| Name | Description |
| ---  | --- |
| [minimisation_algorithm](../slots/minimisation_algorithm.md) | Name of the method used to minimise the molecular system |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: MinimisationAlgorithm
description: Algorithm used to minimise particle interactions.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Steepest Descent:
    text: Steepest Descent
    description: Moves atoms in the opposite direction of the energy gradient (forces).
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: integrator
          value: steep
        - engine: amber
          key: ntmin
          value:
          - 1
          - 2
    aliases:
    - Steepest Descent
    - steepest_descent
  Conjugate Gradient:
    text: Conjugate Gradient
    description: Uses both current gradient information and previous search directions
      to find a more efficient path to the minimum.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: integrator
          value: cg
        - engine: amber
          key: ntmin
          value:
          - 0
          - 1
    aliases:
    - Conjugate Gradient
    - conjugate_gradient
  L-BFGS:
    text: L-BFGS
    description: L-BFGS (Limited-memory Broyden–Fletcher–Goldfarb–Shanno) approximates
      the inverse Hessian matrix (second derivatives) using a limited number of previous
      steps, making it memory-efficient.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: integrator
          value: l-bfgs
    aliases:
    - L-BFGS
  XMIN:
    text: XMIN
    description: Minimization algorithm used to relax molecular structures to their
      lowest potential energy state, particularly for finding very deep local minima.
      It is a quasi-Newton method that typically provides quadratically convergent
      minimization.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: ntmin
          value: 3
    aliases:
    - XMIN
    - xmin
  LMOD:
    text: LMOD
    description: LMOD (Low-Mode) minimization is a specialized conformational search
      and energy minimization method designed to efficiently find low-energy structures
      by navigating along the low-frequency vibrational modes of a system.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: ntmin
          value: 4
    aliases:
    - LMOD
    - lmod

```
</details>

</div>
