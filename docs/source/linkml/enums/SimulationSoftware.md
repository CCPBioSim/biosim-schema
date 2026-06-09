---
search:
  boost: 2.0
---


# Enum: SimulationSoftware




_Simulation software used to perform molecular dynamics simulations and related functions._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/SimulationSoftware](https://CCPBioSim.ac.uk/biosim-schema/SimulationSoftware)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Amber | None | A collective name for a suite of programs that allo users to carry out molecu... |
| GROMACS | None | GROMACS (GROningen Machine for Chemical Simulations) is a free, open-source, ... |
| LAMMPS | None | LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) is an open... |
| NAMD | None | NAMD (Nanoscale Molecular Dynamics, formerly Not Another Molecular Dynamics P... |
| OpenMM | None | OpenMM is a library for performing molecular dynamics simulations on a wide v... |
| CHARMM | None | CHARMM (Chemistry at HARvard Macromolecular Mechanics) is a molecular simulat... |
| DL_POLY | None | DL_POLY is a general purpose classical molecular dynamics (MD) simulation sof... |
| HOOMD-blue | None | HOOMD-blue is a Python package that runs simulations of particle systems on C... |
| Desmond | None | Desmond is a software package developed at D |
| ACEMD | None | A software framework for molecular dynamics-based discovery |
| CP2K | None | CP2K is a quantum chemistry and solid state physics software package that can... |




## Slots

| Name | Description |
| ---  | --- |
| [simulation_software](../slots/simulation_software.md) | Name of software used to perform simulation step |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: SimulationSoftware
description: Simulation software used to perform molecular dynamics simulations and
  related functions.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Amber:
    text: Amber
    description: A collective name for a suite of programs that allo users to carry
      out molecular dynamics simulations, particulary on biomolecules.
    aliases:
    - Amber
    - amber
  GROMACS:
    text: GROMACS
    description: GROMACS (GROningen Machine for Chemical Simulations) is a free, open-source,
      high-performance MD software package designed for simulating biochemical molecules
      like proteins, lipids, and nucleic acids.
    aliases:
    - GROMACS
    - gromacs
  LAMMPS:
    text: LAMMPS
    description: LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator)
      is an open-source classical molecular dynamics code designed for material modeling,
      including solids, soft matter, and coarse-grained systems.
    aliases:
    - LAMMPS
    - lammps
  NAMD:
    text: NAMD
    description: NAMD (Nanoscale Molecular Dynamics, formerly Not Another Molecular
      Dynamics Program) is computer software for molecular dynamics simulation, written
      using the Charm++ parallel programming model.
    aliases:
    - NAMD
    - namd
  OpenMM:
    text: OpenMM
    description: OpenMM is a library for performing molecular dynamics simulations
      on a wide variety of hardware architectures.
    aliases:
    - OpenMM
    - openmm
  CHARMM:
    text: CHARMM
    description: CHARMM (Chemistry at HARvard Macromolecular Mechanics) is a molecular
      simulation program with broad application to many-particle systems with a comprehensive
      set of energy functions, a variety of enhanced sampling methods, and support
      for multi-scale techniques including QM/MM, MM/CG, and a range of implicit solvent
      models.
    aliases:
    - CHARMM
    - charmm
  DL_POLY:
    text: DL_POLY
    description: DL_POLY is a general purpose classical molecular dynamics (MD) simulation
      software developed at Daresbury Laboratory since 1992.
    aliases:
    - DL_POLY
    - dl_poly
  HOOMD-blue:
    text: HOOMD-blue
    description: HOOMD-blue is a Python package that runs simulations of particle
      systems on CPUs and GPUs.
    aliases:
    - HOOMD-blue
    - hoomd_blue
  Desmond:
    text: Desmond
    description: Desmond is a software package developed at D. E. Shaw Research to
      perform high-speed molecular dynamics simulations of biological systems on conventional
      computer clusters.
    aliases:
    - Desmond
    - desmond
  ACEMD:
    text: ACEMD
    description: A software framework for molecular dynamics-based discovery.
    aliases:
    - ACEMD
    - acemd
  CP2K:
    text: CP2K
    description: CP2K is a quantum chemistry and solid state physics software package
      that can perform atomistic simulations of solid state, liquid, molecular, periodic,
      material, crystal, and biological systems.
    aliases:
    - CP2K
    - cp2k

```
</details>

</div>
