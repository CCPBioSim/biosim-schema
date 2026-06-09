---
search:
  boost: 2.0
---


# Enum: SetupTool




_Tool used to setup a system for simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/SetupTool](https://CCPBioSim.ac.uk/biosim-schema/SetupTool)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| pdb4amber | None | Helps in preparing pdb-format files coming from other places to be compatible... |
| prepareforleap | None | An action inside cpptraj, that also helps make pdb-format files compatible wi... |
| packmol | None |  |
| packmol_memgen | None | Packmol-memgen provides a way to generate membrane systems, with or without p... |
| LEaP | None | The primary program to create a new system in Amber, or to modify existing sy... |
| antechamber | None | The main program to develop force fields for small organic molecules using a ... |
| pyMSMT | None | A way to build, prototype and validate MM models of metalloproteins and organ... |
| mdgx | None | Allows the generation of bonded force field parameters for any molecule by fi... |
| parmed | None | Provides a way to extract information about parameters defined in a parameter... |




## Slots

| Name | Description |
| ---  | --- |
| [setup_tool](../slots/setup_tool.md) | Name of the tool used to setup simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: SetupTool
description: Tool used to setup a system for simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  pdb4amber:
    text: pdb4amber
    description: Helps in preparing pdb-format files coming from other places to be
      compatible with LEaP.
  prepareforleap:
    text: prepareforleap
    description: An action inside cpptraj, that also helps make pdb-format files compatible
      with LEaP. It is particularly useful for carbohydrates.
  packmol:
    text: packmol
  packmol_memgen:
    text: packmol_memgen
    description: Packmol-memgen provides a way to generate membrane systems, with
      or without protein, by orienting input proteins with Memembed and using Packmol
      as the packing engine.
  LEaP:
    text: LEaP
    description: The primary program to create a new system in Amber, or to modify
      existing systems.
  antechamber:
    text: antechamber
    description: The main program to develop force fields for small organic molecules
      using a version of the general Amber force field (GAFF).
  pyMSMT:
    text: pyMSMT
    description: A way to build, prototype and validate MM models of metalloproteins
      and organometallic compounds.
  mdgx:
    text: mdgx
    description: Allows the generation of bonded force field parameters for any molecule
      by fitting to quantum data.
  parmed:
    text: parmed
    description: Provides a way to extract information about parameters defined in
      a parameter-topology file.

```
</details>

</div>
