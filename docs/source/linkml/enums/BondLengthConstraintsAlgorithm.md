---
search:
  boost: 2.0
---


# Enum: BondLengthConstraintsAlgorithm




_Fix specific molecular degrees of freedom—typically fast bond vibrations involving hydrogen atoms. By eliminating these high-frequency motions, constraints allow for larger integration time steps (e.g., 2 fs instead of 0.5 fs), significantly speeding up simulations without disrupting system dynamics._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/BondLengthConstraintsAlgorithm](https://CCPBioSim.ac.uk/biosim-schema/BondLengthConstraintsAlgorithm)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SHAKE | None | An iterative method that works with the Verlet algorithm to satisfy constrain... |
| RATTLE | None | A velocity-friendly version of SHAKE used to maintain constraints in velocity... |
| SETTLE | None | An analytical constraint algorithm used in molecular dynamics (specifically G... |
| LINCS | None | LINCS (Linear Constraint Solver) is a fast, stable algorithm that breaks cons... |
| CCMA | None | The Constant Constraint Matrix Approximation (CCMA) is a fast, stable algorit... |




## Slots

| Name | Description |
| ---  | --- |
| [bond_length_constraints_algorithm](../slots/bond_length_constraints_algorithm.md) | Constraints applied to bonds between two particles in the simulated system |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: BondLengthConstraintsAlgorithm
description: Fix specific molecular degrees of freedom—typically fast bond vibrations
  involving hydrogen atoms. By eliminating these high-frequency motions, constraints
  allow for larger integration time steps (e.g., 2 fs instead of 0.5 fs), significantly
  speeding up simulations without disrupting system dynamics.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  SHAKE:
    text: SHAKE
    description: An iterative method that works with the Verlet algorithm to satisfy
      constraints on bond lengths, ensuring the distance between mass points remains
      constant.
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: constraint-algorithm
          value: SHAKE
        - engine: amber
          key: ntc
          value:
          - 2
          - 3
    aliases:
    - SHAKE
    - shake
  RATTLE:
    text: RATTLE
    description: A velocity-friendly version of SHAKE used to maintain constraints
      in velocity Verlet integrators.
    aliases:
    - RATTLE
    - rattle
  SETTLE:
    text: SETTLE
    description: An analytical constraint algorithm used in molecular dynamics (specifically
      GROMACS) to maintain rigid water models (like TIP3P, TIP4P) by fixing bond lengths
      and angles. It is faster and more stable than iterative methods like SHAKE,
      operating in constant time without calculating centers of mass, reducing rounding
      errors.
    aliases:
    - SETTLE
    - settle
  LINCS:
    text: LINCS
    description: LINCS (Linear Constraint Solver) is a fast, stable algorithm that
      breaks constraints into two steps; removing projections of new bond lengths
      on old bonds and correcting for bond lengthening due to rotation
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: constraint-algorithm
          value: LINCS
    aliases:
    - LINCS
    - lincs
  CCMA:
    text: CCMA
    description: The Constant Constraint Matrix Approximation (CCMA) is a fast, stable
      algorithm designed to handle geometric constraints in molecular simulations,
      particularly effective for macromolecules like proteins.
    aliases:
    - CCMA
    - ccma

```
</details>

</div>
