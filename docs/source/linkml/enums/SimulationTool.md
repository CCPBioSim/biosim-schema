---
search:
  boost: 2.0
---


# Enum: SimulationTool




_Tools/utility used within simulation engines to perform simulations._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/SimulationTool](https://CCPBioSim.ac.uk/biosim-schema/SimulationTool)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| sander | None | A tool with AmberTools that is a basic energy minimizer and molecular dynamic... |
| pmemd | None | Part of Amber and is a version of the sander simulation tool that is optimize... |
| gem.pmemd | None | gem |
| mdrun | None | The main molecular dynamics engine of GROMACS, used to perform energy minimiz... |




## Slots

| Name | Description |
| ---  | --- |
| [simulation_tool](../slots/simulation_tool.md) | Tool used to perform simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: SimulationTool
description: Tools/utility used within simulation engines to perform simulations.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  sander:
    text: sander
    description: A tool with AmberTools that is a basic energy minimizer and molecular
      dynamics program.
  pmemd:
    text: pmemd
    description: Part of Amber and is a version of the sander simulation tool that
      is optimized for speed and for parallel scaling.
  gem.pmemd:
    text: gem.pmemd
    description: gem.pmemd is a part of AmberTools that is a CPI-only variant of the
      pmemd program that is designed for calculations using "advanced" force fields,
      such as AMOEBA and GEM.
    aliases:
    - gem.pmemd
    - gem_pmemd
  mdrun:
    text: mdrun
    description: The main molecular dynamics engine of GROMACS, used to perform energy
      minimization, molecular dynamics simulations, and analysis. It executes the
      simulation based on input files prepared by other GROMACS tools, supporting
      a wide range of simulation types and parallelization options.

```
</details>

</div>
