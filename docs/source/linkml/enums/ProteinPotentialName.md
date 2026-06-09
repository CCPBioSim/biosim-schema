---
search:
  boost: 2.0
---


# Enum: ProteinPotentialName




_Force fields used to parametrize amino acids in proteins in a simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/ProteinPotentialName](https://CCPBioSim.ac.uk/biosim-schema/ProteinPotentialName)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ff19SB | None | As of Amber24, ff19SB is the latest model of SB protein force fields and has ... |
| ff99SB | None | All-atom molecular mechanics force field specifically designed to simulate pr... |
| ff99SB-ILDN | None | Refined extension of the foundational Amber ff99SB model, specifically optimi... |
| ff99SB-disp | None | Optimized by D |
| ff14SB | None | Older version of the SB protein force fields that utilizes uncoupled phi/psi ... |
| ff14SBonlysc | None | Includes the ff99SB backbone parameters with updated side chain (sc) paramete... |
| ff15ipq | None | Continues the development begun with the ff14ipq force field for proteins, bu... |
| fb15 | None | The force balance (fb) protein force field that can be used for protein-water... |
| ff03 | None | A modified version of ff99, where charges are derived from quantum calculatio... |
| ff03ua | None | The united-atom counterpart of ff03, which uses the dame charging scheme as f... |
| phosaa10 | None | Force field for phosphorylated amino acids |
| phosaa14SB | None | Force field for phosphorylated amino acids with ff14SB |
| phosaa19SB | None | Force field for phosphorylated amino acids with ff19SB |
| ff14SB_modAA | None | Force field with ff14SB for modified amino acids like selenomethionine, cyano... |
| ff19SB_modAA | None | Force field with ff19SB for modified amino acids like selenomethionine, cyano... |




## Slots

| Name | Description |
| ---  | --- |
| [protein_potential_name](../slots/protein_potential_name.md) | Force field used to describe proteins |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: ProteinPotentialName
description: Force fields used to parametrize amino acids in proteins in a simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  ff19SB:
    text: ff19SB
    description: As of Amber24, ff19SB is the latest model of SB protein force fields
      and has shown to improve amino acid-dependent properties such as helical propensities
      and reproduces the differences in amino acid-specific PDB Ramachandran maps.
  ff99SB:
    text: ff99SB
    description: All-atom molecular mechanics force field specifically designed to
      simulate proteins and peptides
  ff99SB-ILDN:
    text: ff99SB-ILDN
    description: Refined extension of the foundational Amber ff99SB model, specifically
      optimized to fix errors in side-chain rotamer distributions.
  ff99SB-disp:
    text: ff99SB-disp
    description: Optimized by D.E. Shaw Research to accurately simulate both folded,
      structured proteins and intrinsically disordered proteins (IDPs) or highly flexible
      peptide states.
  ff14SB:
    text: ff14SB
    description: Older version of the SB protein force fields that utilizes uncoupled
      phi/psi dihedral parameters for the protein backbone, and every amino acid except
      for glycine used the backbone dihedral parameters fit using alanine.
  ff14SBonlysc:
    text: ff14SBonlysc
    description: Includes the ff99SB backbone parameters with updated side chain (sc)
      parameters that were derived from ab initio quantum mechanics calculations.
  ff15ipq:
    text: ff15ipq
    description: Continues the development begun with the ff14ipq force field for
      proteins, but offers new parameter choices, data fitting and validation.
  fb15:
    text: fb15
    description: The force balance (fb) protein force field that can be used for protein-water
      simulations.
  ff03:
    text: ff03
    description: A modified version of ff99, where charges are derived from quantum
      calculations that ise a continuum dielectric to mimic solvent polarization.
  ff03ua:
    text: ff03ua
    description: The united-atom counterpart of ff03, which uses the dame charging
      scheme as ff03, but the aliphatic hydrogen atoms on all amino acid side-chains
      are united to their corresponding carbon atoms.
  phosaa10:
    text: phosaa10
    description: Force field for phosphorylated amino acids.
  phosaa14SB:
    text: phosaa14SB
    description: Force field for phosphorylated amino acids with ff14SB.
  phosaa19SB:
    text: phosaa19SB
    description: Force field for phosphorylated amino acids with ff19SB.
  ff14SB_modAA:
    text: ff14SB_modAA
    description: Force field with ff14SB for modified amino acids like selenomethionine,
      cyano-phenylalanine, and azido-phenylalanine, acetylated lysine and for the
      nitroxide spin-label methanesulfonothioate (MTSL).
  ff19SB_modAA:
    text: ff19SB_modAA
    description: Force field with ff19SB for modified amino acids like selenomethionine,
      cyano-phenylalanine, and azido-phenylalanine, acetylated lysine and for the
      nitroxide spin-label methanesulfonothioate (MTSL).

```
</details>

</div>
