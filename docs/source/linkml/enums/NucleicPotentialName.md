---
search:
  boost: 2.0
---


# Enum: NucleicPotentialName




_Force fields used to parametrize nucleic acids in a simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/NucleicPotentialName](https://CCPBioSim.ac.uk/biosim-schema/NucleicPotentialName)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ff99-bsc0 | None | Force field for nucliec acids |
| ff99OL3 | None | Force field for RNA, where quantum mechanics methods at various levels were e... |
| LJbb | None | RNA force field with modified phosphate parameters (from OL force field) and ... |
| ROC | None | Force field with alternative set of torsions for RNA, fit to quantum calculat... |
| Shaw | None | RNA force field with more extensive modifications |
| OL15 | None | Force field for DNA, with a combination of three dihedral updates |
| OL21 | None | DNA force field that adds some new torsion modifications, aimed at non-B doub... |
| OL24 | None |  |
| OL3 | None |  |
| bsc1 | None | Updated version of bsc0 force field for DNA, using an implicit solvation mode... |
| terminal_monophosphate | None | Force field library for the 5\’ end of many DNA and RNA chains have one or mo... |




## Slots

| Name | Description |
| ---  | --- |
| [nucleic_potential_name](../slots/nucleic_potential_name.md) | Force field used to describe nucleic acids |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: NucleicPotentialName
description: Force fields used to parametrize nucleic acids in a simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  ff99-bsc0:
    text: ff99-bsc0
    description: Force field for nucliec acids. High level quantum mechanics calculations
      were perfomed on models of sugars and phosphates, specifically a sugar-phosphate
      model and a sugar-phosphate-sugar model.
  ff99OL3:
    text: ff99OL3
    description: Force field for RNA, where quantum mechanics methods at various levels
      were employed to improve the chi angle distribution using relevant model systems.
  LJbb:
    text: LJbb
    description: RNA force field with modified phosphate parameters (from OL force
      field) and an improved water model (OPC), which has better agreement with NMR
      data for RNA tetranucleotide populations.
  ROC:
    text: ROC
    description: Force field with alternative set of torsions for RNA, fit to quantum
      calculations.
  Shaw:
    text: Shaw
    description: RNA force field with more extensive modifications.
  OL15:
    text: OL15
    description: Force field for DNA, with a combination of three dihedral updates.
  OL21:
    text: OL21
    description: DNA force field that adds some new torsion modifications, aimed at
      non-B double helices, as of Amber24, is the current recommended DNA force field.
  OL24:
    text: OL24
  OL3:
    text: OL3
  bsc1:
    text: bsc1
    description: Updated version of bsc0 force field for DNA, using an implicit solvation
      model and a rigorous quantum mechanics methodology.
  terminal_monophosphate:
    text: terminal_monophosphate
    description: Force field library for the 5\’ end of many DNA and RNA chains have
      one or more phosphate groups.

```
</details>

</div>
