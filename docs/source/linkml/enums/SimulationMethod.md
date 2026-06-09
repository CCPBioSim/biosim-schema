---
search:
  boost: 2.0
---


# Enum: SimulationMethod




_Options for simulation methods._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/SimulationMethod](https://CCPBioSim.ac.uk/biosim-schema/SimulationMethod)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Self-guided Langevin Dynamics | None | Method that accelerates low frequency motion to enhance conformational sampli... |
| Accelerated Molecular Dynamics | None | Method where a bias potential that reduces the height of local barriers, allo... |
| Gaussian Accelerated Molecular Dynamics | None | Method that adds a harmonic boost potential (following a Gaussian distributio... |
| Targeted Molecular Dynamics | None | Method that adds an additional term to the energy function based on the mass-... |
| Nudged Elastic Band Calculations | None | Method where the path for a conformational change is approximated with a seri... |
| Adaptive String Method | None | Method to find the Minimum Free Energy Path (MFEP) in the space of selected c... |
| LMOD method | None | Conformational search algorithm based on eigenvector following of low frequen... |
| DL-FIND Optimization | None | Method to search for potential energy stationary points along a chemical reac... |
| Thermodynamic Integration (TI) | None | Method to calculate ensemble-averaged energies "on-the-fly" along a path as t... |
| Linear Interaction Energies (LIE) | None | Method to compute binding free energies using the linear interaction energy m... |
| Replica Exchange Molecular Dynamics (REMD) | None | An expanded ensemble energy method that samples from an ensemble larger than ... |
| Adaptively Biased Molecular Dynamics (ABMD) | None | Method for calculating free energy landscapes as a function of a small number... |
| Steered Molecular Dynamics (SMD) | None | Method that applies an external force onto a physical system, and drives a ch... |
| Umbrella Sampling | None | A method that enhances sampling of rare events by applying a biasing potentia... |
| Metadynamics | None | An enhanced sampling technique that adds a history-dependent bias to the pote... |
| Swarms of Trajectories String Method | None | A version of the string method, a path-finding algorithm that refines a punat... |
| Constant pH Molecular Dynamics | None | Method that uses Monte Carlo sampling of the Boltzmann distribution of discre... |
| Constant Redox Potential Molecular Dynamics | None | Method that uses Monte Carlo sampling of the Boltzmann distribution of discre... |
| Continuous Constant pH Molecular Dynamics | None | A method that is an alternative to the Monte-Carlo based constant pH methods ... |
| NMR Refinement | None | Method to incorporate a variety of restraints (e |
| X-ray and CryoEM Refinement | None | Method to incorporate electron microscopy (EM) image information into macromo... |
| Locally Enhanced Sampling | None | A method to allow for multiple local copies of regions within a larger biomol... |




## Slots

| Name | Description |
| ---  | --- |
| [simulation_method](../slots/simulation_method.md) | Method used to perform simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: SimulationMethod
description: Options for simulation methods.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Self-guided Langevin Dynamics:
    text: Self-guided Langevin Dynamics
    description: Method that accelerates low frequency motion to enhance conformational
      sampling.
    aliases:
    - Self-guided Langevin Dynamics
    - selfguided_langevin_dynamics
  Accelerated Molecular Dynamics:
    text: Accelerated Molecular Dynamics
    description: Method where a bias potential that reduces the height of local barriers,
      allowing the faster evolution of a calculation.
    aliases:
    - Accelerated Molecular Dynamics
    - accelerated_molecular_dynamics
  Gaussian Accelerated Molecular Dynamics:
    text: Gaussian Accelerated Molecular Dynamics
    description: Method that adds a harmonic boost potential (following a Gaussian
      distribution) to smooth the system potential energy surface.
    aliases:
    - Gaussian Accelerated Molecular Dynamics
    - Gaussian_accelerated_molecular_dynamics
  Targeted Molecular Dynamics:
    text: Targeted Molecular Dynamics
    description: Method that adds an additional term to the energy function based
      on the mass-wieghted root mean square deviation of a set of atoms in the current
      structure compared to a reference structure.
    aliases:
    - Targeted Molecular Dynamics
    - targeted_molecular_dynamics
  Nudged Elastic Band Calculations:
    text: Nudged Elastic Band Calculations
    description: Method where the path for a conformational change is approximated
      with a series of images describing the molecule at discrete points along the
      path.
    aliases:
    - Nudged Elastic Band Calculations
    - nudged_elastic_band_calculations
  Adaptive String Method:
    text: Adaptive String Method
    description: Method to find the Minimum Free Energy Path (MFEP) in the space of
      selected collective variables connecting initial and final stages of a given
      process.
    aliases:
    - Adaptive String Method
    - adaptive_string_method
  LMOD method:
    text: LMOD method
    description: Conformational search algorithm based on eigenvector following of
      low frequency vibrational modes.
    aliases:
    - LMOD method
    - LMOD_method
  DL-FIND Optimization:
    text: DL-FIND Optimization
    description: Method to search for potential energy stationary points along a chemical
      reaction in a QM/MM simulation.
    aliases:
    - DL-FIND Optimization
    - DLFind_optimization
  Thermodynamic Integration (TI):
    text: Thermodynamic Integration (TI)
    description: Method to calculate ensemble-averaged energies "on-the-fly" along
      a path as the simulation progresses between two states.
    aliases:
    - Thermodynamic Integration (TI)
    - thermodynamic_integration
  Linear Interaction Energies (LIE):
    text: Linear Interaction Energies (LIE)
    description: Method to compute binding free energies using the linear interaction
      energy model.
    aliases:
    - Linear Interaction Energies (LIE)
    - linear_interaction_energies
  Replica Exchange Molecular Dynamics (REMD):
    text: Replica Exchange Molecular Dynamics (REMD)
    description: An expanded ensemble energy method that samples from an ensemble
      larger than a typical statistical mechanical ensemble defined by the Hamiltonian
      governing the system.
    aliases:
    - Replica Exchange Molecular Dynamics (REMD)
    - replica_exchange_molecular_dynamics
  Adaptively Biased Molecular Dynamics (ABMD):
    text: Adaptively Biased Molecular Dynamics (ABMD)
    description: Method for calculating free energy landscapes as a function of a
      small number of collective variables.
    aliases:
    - Adaptively Biased Molecular Dynamics (ABMD)
    - adaptively_biased_molecular_dynamics
  Steered Molecular Dynamics (SMD):
    text: Steered Molecular Dynamics (SMD)
    description: Method that applies an external force onto a physical system, and
      drives a change in coordinates within a certain time. The moethod should be
      thought of as umbrella sampling where the center of the restraint is time-dependent.
    aliases:
    - Steered Molecular Dynamics (SMD)
    - steered_molecular_dynamics
  Umbrella Sampling:
    text: Umbrella Sampling
    description: A method that enhances sampling of rare events by applying a biasing
      potential to restrain the system along a chosen coordinate, allowing for the
      calculation of free energy profiles.
    aliases:
    - Umbrella Sampling
    - umbrella_sampling
  Metadynamics:
    text: Metadynamics
    description: An enhanced sampling technique that adds a history-dependent bias
      to the potential energy surface, encouraging the system to escape local minima
      and explore new configurations, often used to reconstruct free energy landscapes.
    aliases:
    - Metadynamics
    - metadynamics
  Swarms of Trajectories String Method:
    text: Swarms of Trajectories String Method
    description: A version of the string method, a path-finding algorithm that refines
      a punative transition pathway iteratively until the path is deemed to have been
      converged.
    aliases:
    - Swarms of Trajectories String Method
    - swarms_of_trajectories_string_method
  Constant pH Molecular Dynamics:
    text: Constant pH Molecular Dynamics
    description: Method that uses Monte Carlo sampling of the Boltzmann distribution
      of discrete protonation states concurrent with the molecular dynamics simulation.
    aliases:
    - Constant pH Molecular Dynamics
    - constant_pH_molecular_dynamics
  Constant Redox Potential Molecular Dynamics:
    text: Constant Redox Potential Molecular Dynamics
    description: Method that uses Monte Carlo sampling of the Boltzmann distribution
      of discrete redox sates concurrent with the molecular dynamics simulation.
    aliases:
    - Constant Redox Potential Molecular Dynamics
    - constant_redox_potential_molecular_dynamics
  Continuous Constant pH Molecular Dynamics:
    text: Continuous Constant pH Molecular Dynamics
    description: A method that is an alternative to the Monte-Carlo based constant
      pH methods where particles with fictitious mass and coordinates bound between
      0 (protonated) and 1 (deprotonated) are added to the system to present protonation
      states of titratable sites.
    aliases:
    - Continuous Constant pH Molecular Dynamics
    - continuous_constant_pH_molecular_dynamics
  NMR Refinement:
    text: NMR Refinement
    description: Method to incorporate a variety of restraints (e.g. NMR restraints
      derived from NOE and J-coupling data) into an optimization procedure.
    aliases:
    - NMR Refinement
    - NMR_refinement
  X-ray and CryoEM Refinement:
    text: X-ray and CryoEM Refinement
    description: Method to incorporate electron microscopy (EM) image information
      into macromolecular structure determination, by applying restraints for rigid
      and flexible fitting into EM maps.
    aliases:
    - X-ray and CryoEM Refinement
    - Xray_and_cryoEM_refinement
  Locally Enhanced Sampling:
    text: Locally Enhanced Sampling
    description: A method to allow for multiple local copies of regions within a larger
      biomolecule, e.g. to allow sidechains in a protein to be "disordered", while
      the backbone is represented as a single configuration.
    aliases:
    - Locally Enhanced Sampling
    - locally_enhanced_sampling

```
</details>

</div>
