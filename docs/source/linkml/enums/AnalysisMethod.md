---
search:
  boost: 2.0
---


# Enum: AnalysisMethod




_Methods used to analyse simulation outputs._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/AnalysisMethod](https://CCPBioSim.ac.uk/biosim-schema/AnalysisMethod)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| RMSD | None | Calculate the root mean square deviation (RMSD) between distance pairs within... |
| DSSP | None | Calculate the secondary structure content using the Define Secondary Structur... |
| GIST | None | Perform the grid inhomogenous solvation theory (GIST), a method for analyzing... |
| Hydrogen Bonds | None | Calculate hydrogen bonds using geometric criteria |
| Connolly surface | None | Calculate the Connolly surface area of specified atoms |
| Radius of Gyration | None | Calculate the radius of gyration for specified atoms |
| BAR/PBSA | None | BAR/PBSA is a method developed to address inability of alchemical simulations... |




## Slots

| Name | Description |
| ---  | --- |
| [analysis_method](../slots/analysis_method.md) | Name of the method used to analyse simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: AnalysisMethod
description: Methods used to analyse simulation outputs.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  RMSD:
    text: RMSD
    description: Calculate the root mean square deviation (RMSD) between distance
      pairs within selected points, perform best of fit of coordinates to a reference
      first.
    aliases:
    - RMSD
    - root_mean_square_deviation
  DSSP:
    text: DSSP
    description: Calculate the secondary structure content using the Define Secondary
      Structure of Proteins (DSSP) algorithm.
    aliases:
    - DSSP
    - define_secondary_structure_of_proteins
  GIST:
    text: GIST
    description: Perform the grid inhomogenous solvation theory (GIST), a method for
      analyzing the strutre and dyanmics of solvent in the vicinity of a solute molecule.
    aliases:
    - GIST
    - grid_inhomogenous_solvation_theory
  Hydrogen Bonds:
    text: Hydrogen Bonds
    description: Calculate hydrogen bonds using geometric criteria.
    aliases:
    - Hydrogen Bonds
    - hydrogen_bonds
  Connolly surface:
    text: Connolly surface
    description: Calculate the Connolly surface area of specified atoms.
    aliases:
    - Connolly surface
    - connolly_surface
  Radius of Gyration:
    text: Radius of Gyration
    description: Calculate the radius of gyration for specified atoms.
    aliases:
    - Radius of Gyration
    - radius_of_gyration
  BAR/PBSA:
    text: BAR/PBSA
    description: BAR/PBSA is a method developed to address inability of alchemical
      simulations to handle elecronic polarization effects upon ligand transfer from
      water to the protein interior. Used to post-process alchemical simulation trajectories
      to incorporate the polarization effects in a continuum manner.
    aliases:
    - BAR/PBSA
    - bar_pbsa

```
</details>

</div>
