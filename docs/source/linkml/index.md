# biosim-schema

Schema for Biomolecular Simulation Data

URI: https://CCPBioSim.ac.uk/biosim-schema/

Name: biosim-schema



## Classes

| Class | Description |
| --- | --- |
| [Analysis](classes/Analysis.md) |  |
| [AngleQuantity](classes/AngleQuantity.md) |  |
| [Barostat](classes/Barostat.md) |  |
| [ByteQuantity](classes/ByteQuantity.md) |  |
| [CarbohydratePotential](classes/CarbohydratePotential.md) |  |
| [ChargeQuantity](classes/ChargeQuantity.md) |  |
| [ComputationalEnvironment](classes/ComputationalEnvironment.md) |  |
| [ConcentrationQuantity](classes/ConcentrationQuantity.md) |  |
| [Connectivity](classes/Connectivity.md) |  |
| [EnergyQuantity](classes/EnergyQuantity.md) |  |
| [Ensemble](classes/Ensemble.md) |  |
| [Equilibration](classes/Equilibration.md) |  |
| [ForceQuantity](classes/ForceQuantity.md) |  |
| [FrequencyQuantity](classes/FrequencyQuantity.md) |  |
| [FrictionCoefficientQuantity](classes/FrictionCoefficientQuantity.md) |  |
| [GeneralPotential](classes/GeneralPotential.md) |  |
| [Hardware](classes/Hardware.md) |  |
| [Integrator](classes/Integrator.md) |  |
| [Interactions](classes/Interactions.md) |  |
| [LengthQuantity](classes/LengthQuantity.md) |  |
| [LipidPotential](classes/LipidPotential.md) |  |
| [MachineLearnedPotential](classes/MachineLearnedPotential.md) |  |
| [MassQuantity](classes/MassQuantity.md) |  |
| [MatrixCompressibilityQuantity](classes/MatrixCompressibilityQuantity.md) |  |
| [MatrixPressureQuantity](classes/MatrixPressureQuantity.md) |  |
| [MatrixQuantity](classes/MatrixQuantity.md) |  |
| [Minimisation](classes/Minimisation.md) |  |
| [MolarEnergyQuantity](classes/MolarEnergyQuantity.md) |  |
| [MoleculeID](classes/MoleculeID.md) |  |
| [NucleicPotential](classes/NucleicPotential.md) |  |
| [Particles](classes/Particles.md) |  |
| [Performance](classes/Performance.md) |  |
| [PolymerPotential](classes/PolymerPotential.md) |  |
| [PotentialMetadata](classes/PotentialMetadata.md) |  |
| [PressureQuantity](classes/PressureQuantity.md) |  |
| [Production](classes/Production.md) |  |
| [ProteinPotential](classes/ProteinPotential.md) |  |
| [Setup](classes/Setup.md) |  |
| [SimulationAverages](classes/SimulationAverages.md) |  |
| [SimulationBox](classes/SimulationBox.md) |  |
| [SimulationMetadata](classes/SimulationMetadata.md) |  |
| [SimulationObservables](classes/SimulationObservables.md) |  |
| [SimulationSettings](classes/SimulationSettings.md) |  |
| [SimulationStages](classes/SimulationStages.md) |  |
| [Software](classes/Software.md) |  |
| [SystemComposition](classes/SystemComposition.md) |  |
| [SystemCounts](classes/SystemCounts.md) |  |
| [TemperatureQuantity](classes/TemperatureQuantity.md) |  |
| [Thermostat](classes/Thermostat.md) |  |
| [TimeQuantity](classes/TimeQuantity.md) |  |
| [TopologyMetadata](classes/TopologyMetadata.md) |  |
| [Trajectories](classes/Trajectories.md) |  |
| [TrajectoryMetadata](classes/TrajectoryMetadata.md) |  |
| [VectorAngleQuantity](classes/VectorAngleQuantity.md) | A quantity representing 3D angles |
| [VectorCompressibilityQuantity](classes/VectorCompressibilityQuantity.md) |  |
| [VectorLengthQuantity](classes/VectorLengthQuantity.md) | A quantity representing 3D lengths/dimensions |
| [VectorPressureQuantity](classes/VectorPressureQuantity.md) |  |
| [VectorTemperatureQuantity](classes/VectorTemperatureQuantity.md) | Temperature values for multiple coupling groups |
| [VectorTimeQuantity](classes/VectorTimeQuantity.md) | Time values for multiple coupling groups |
| [VectorVolumeQuantity](classes/VectorVolumeQuantity.md) |  |
| [VolumeQuantity](classes/VolumeQuantity.md) |  |
| [WaterPotential](classes/WaterPotential.md) |  |



## Slots

| Slot | Description |
| --- | --- |
| [alphafold_ID](slots/alphafold_ID.md) | AlphaFold predicted protein structure identifier (AlphaFold DB, EMBL-EBI) |
| [analysis](slots/analysis.md) | Analysis stage of a simulation |
| [analysis_method](slots/analysis_method.md) | Name of the method used to analyse simulation |
| [analysis_software](slots/analysis_software.md) | Name of software used to analyse simulation |
| [analysis_tool](slots/analysis_tool.md) | Name of the tool used to analyse simulation |
| [atom_count](slots/atom_count.md) | Number of atoms in a molecule |
| [average_enthalpy](slots/average_enthalpy.md) | Average enthalpy sampled from the simulation, given as a float |
| [average_kinetic_energy](slots/average_kinetic_energy.md) | Average kinetic energy sampled from the simulation, given as a float |
| [average_potential_energy](slots/average_potential_energy.md) | Average potential energy sampled from the simulation, given as a float |
| [average_pressure](slots/average_pressure.md) | Average pressure sampled from the simulation, given as a float |
| [average_temperature](slots/average_temperature.md) | Average temperature sampled from the simulation, given as a float |
| [average_volume](slots/average_volume.md) | Average volume sampled from the simulation, given as a float |
| [average_volume_vector](slots/average_volume_vector.md) | Average volume sampled from the simulation, given as a list, (e |
| [barostat](slots/barostat.md) | Barostat information |
| [barostat_algorithm](slots/barostat_algorithm.md) | List of barostat algorithms used in the simulation |
| [bond_length_constraints_algorithm](slots/bond_length_constraints_algorithm.md) | Constraints applied to bonds between two particles in the simulated system |
| [bonds](slots/bonds.md) | Are bond parameters present in the topology? |
| [box_angles](slots/box_angles.md) | The angles of the box used to simulate the system |
| [box_dimensions](slots/box_dimensions.md) | The lengths/dimensions of the box used to simulate the system |
| [box_type](slots/box_type.md) | The type of box used to simuluate the system |
| [carbohydrate_potential](slots/carbohydrate_potential.md) | Force field for carbohydrates |
| [carbohydrate_potential_name](slots/carbohydrate_potential_name.md) | Force field used to describe carbohydrate |
| [chain_length](slots/chain_length.md) | Usually required in the Nosé-Hoover thermostat, the chain length (e |
| [coarse_grained](slots/coarse_grained.md) | Are atoms coarse-grained? |
| [collision_frequency](slots/collision_frequency.md) | Collision frequency for the integrator, given as a float |
| [composition](slots/composition.md) |  |
| [compressibility](slots/compressibility.md) | Compressibility of the simulated system, given as a float |
| [compute](slots/compute.md) |  |
| [connectivity](slots/connectivity.md) | Particle connectivity information |
| [container_runtime](slots/container_runtime.md) | Container runtime used to execute the simulation environment, if any |
| [cores_per_socket](slots/cores_per_socket.md) | Number of physical CPU cores in each socket |
| [coupling_group](slots/coupling_group.md) | A subset of atoms for which temperature is controlled, often needed for simul... |
| [CPU_architecture](slots/CPU_architecture.md) | CPU instruction-set architecture of the compute nodes |
| [CPU_vendor](slots/CPU_vendor.md) | CPU vendor used in the compute nodes |
| [dihedrals](slots/dihedrals.md) | Are dihedral parameters present in the topology? |
| [electrostatic_cutoff_distance](slots/electrostatic_cutoff_distance.md) | Distance in Angstrom at which a electrostatic interaction is turned off and a... |
| [EMDB_ID](slots/EMDB_ID.md) | Electron Microscopy Data Bank ID |
| [energies](slots/energies.md) | Are per-frame energies included in the trajectory? |
| [energy_consumption](slots/energy_consumption.md) | Total energy consumed by the simulation run |
| [energy_tolerance](slots/energy_tolerance.md) | Tolerance energy for when minimization stops, this is when the maximum force ... |
| [engine_mapping](slots/engine_mapping.md) | Mapping from engine-specific parameter names to schema slots |
| [ensemble](slots/ensemble.md) | Ensemble information |
| [ensemble_type](slots/ensemble_type.md) | List of ensemble types used in the simulation |
| [equilibration](slots/equilibration.md) | Equilibration stage of a simulation |
| [execution_platform](slots/execution_platform.md) | Broad type of system used to run the simulation workload |
| [fixed_charges](slots/fixed_charges.md) | Are fixed charges on atoms included in the topology? |
| [forces](slots/forces.md) | Are per-frame forces included in the trajectory? |
| [frame_count](slots/frame_count.md) | Total number of snapshots that make up a trajectory |
| [frame_step](slots/frame_step.md) | Time between saved snapshots/frames in a simulation, given as a float |
| [friction_coefficient](slots/friction_coefficient.md) | Usually used in the Langevin thermostat, the friction coefficient determines ... |
| [general_potential](slots/general_potential.md) | Force field for molecules (in general) |
| [general_potential_name](slots/general_potential_name.md) | Force field used to describe molecules |
| [GPU_vendor](slots/GPU_vendor.md) | GPU vendor used by the compute nodes, if applicable |
| [GPUs_per_node](slots/GPUs_per_node.md) | Number of GPUs present in each compute node |
| [hardware](slots/hardware.md) |  |
| [identifier](slots/identifier.md) | External database identifier |
| [InChI](slots/InChI.md) | The International Chemical Identifier (InChi) is a textual identifier for che... |
| [InChIKey](slots/InChIKey.md) | The condensed, 27 character InChIKey, which is a hashed version of the full I... |
| [integrator](slots/integrator.md) | Integrator information |
| [integrator_algorithm](slots/integrator_algorithm.md) | List of integrator algorithms used to integrate the simulation |
| [interactions](slots/interactions.md) | Interaction information |
| [lipid_potential](slots/lipid_potential.md) | Force field for lipids |
| [lipid_potential_name](slots/lipid_potential_name.md) | Force field used to describe lipids |
| [long_range_interaction_method](slots/long_range_interaction_method.md) | Method used to describe long-range interactions between particles |
| [machine_learned_potential](slots/machine_learned_potential.md) | ML force field for molecules (in general) |
| [machine_learned_potential_name](slots/machine_learned_potential_name.md) | ML force field used to describe molecules |
| [masses](slots/masses.md) | Are masses present in the topology? |
| [memory_per_node](slots/memory_per_node.md) | Amount of memory installed per compute node |
| [minimisation](slots/minimisation.md) | Minimisation stage of a simulation |
| [minimisation_algorithm](slots/minimisation_algorithm.md) | Name of the method used to minimise the molecular system |
| [minimisation_distance_step_size](slots/minimisation_distance_step_size.md) | The distance the algorithm moves in a single step, controls how large a step ... |
| [modified](slots/modified.md) | Has the initial model been modified from the original? |
| [molecular_formula](slots/molecular_formula.md) | The molecular formula of a molecule\ |
| [molecular_weight](slots/molecular_weight.md) | The molecular weight of a molecule |
| [molecule_charge](slots/molecule_charge.md) | Electrostatic charge of a molecule |
| [molecule_count](slots/molecule_count.md) | Number of instances of a given molecule, defined as bonded atoms or beads |
| [molecule_ID](slots/molecule_ID.md) | Persistent identifier of a molecule being simulated |
| [monomer_count](slots/monomer_count.md) | Number of monomeric units in a polymer(e |
| [MPI_library](slots/MPI_library.md) | MPI implementation used for distributed parallel execution |
| [node_count](slots/node_count.md) | Number of compute nodes used for the run |
| [node_type](slots/node_type.md) | Compute node profile used for the simulation run |
| [nucleic_potential](slots/nucleic_potential.md) | Force field for nucleic acids |
| [nucleic_potential_name](slots/nucleic_potential_name.md) | Force field used to describe nucleic acids |
| [nucleic_sequence](slots/nucleic_sequence.md) | One letter sequence for nucleic acid nucleotides |
| [number_of_minimisation_steps](slots/number_of_minimisation_steps.md) | Number of integration steps performed during minimisation of the system, give... |
| [number_of_steps](slots/number_of_steps.md) | Number of integration steps performed in the simulation, given as an integer |
| [observables](slots/observables.md) |  |
| [operating_system](slots/operating_system.md) | Operating system installed on the hardware used to perform the simulation |
| [particles](slots/particles.md) | Particles information |
| [PDB_ID](slots/PDB_ID.md) | Protein Data Bank identifier |
| [performance](slots/performance.md) |  |
| [periodic_boundary_conditions](slots/periodic_boundary_conditions.md) | What directions in a simulation cell periodic boundaries are set if they are ... |
| [polarizable_charges](slots/polarizable_charges.md) | Are per-frame polarizable charges included in the trajectory? |
| [polymer_potential](slots/polymer_potential.md) | Force field for polymers (excluding proteins and nucleic acids) |
| [polymer_potential_name](slots/polymer_potential_name.md) | Force field used to describe polymers (excluding proteins and nucleic acids) |
| [positions](slots/positions.md) | Are per-frame positions included in the trajectory? |
| [potentials](slots/potentials.md) |  |
| [predicted_structure](slots/predicted_structure.md) | Are the molecule positions derived from a prediction? |
| [pressure_coupling_frequency](slots/pressure_coupling_frequency.md) | Step frequency to apply the barostat, given as an integer |
| [pressure_coupling_type](slots/pressure_coupling_type.md) | List of coupling types for adjusting box vectors |
| [pressure_time_constant](slots/pressure_time_constant.md) | Time constant/step (relaxation time of pressure) used for coupling the system... |
| [production](slots/production.md) | Production stage of a simulation |
| [protein_potential](slots/protein_potential.md) | Force field for proteins |
| [protein_potential_name](slots/protein_potential_name.md) | Force field used to describe proteins |
| [protein_sequence](slots/protein_sequence.md) | One letter sequence for protein amino acids |
| [PubChem_CID](slots/PubChem_CID.md) | PubChem CID of chemical molecules and their activities against biological ass... |
| [random_seed](slots/random_seed.md) | Random number used to set (a) distribution of velocities across particles at ... |
| [replica](slots/replica.md) | Is this trajectory a replica of another provided trajectory? |
| [resolution](slots/resolution.md) | Resolution of simulated system |
| [restraints](slots/restraints.md) | Are any positional restraints applied to molecule dynamics? (Restraints usual... |
| [salt_concentration](slots/salt_concentration.md) | Concentration of salt in the solution |
| [scheduler](slots/scheduler.md) | Workload manager or job scheduler used to launch the simulation |
| [settings](slots/settings.md) |  |
| [setup](slots/setup.md) | Setup stage of a simulation |
| [setup_tool](slots/setup_tool.md) | Name of the tool used to setup simulation |
| [simulation_averages](slots/simulation_averages.md) | Average values of observables outputted from the simulation |
| [simulation_box](slots/simulation_box.md) | Information about the simulation box |
| [simulation_method](slots/simulation_method.md) | Method used to perform simulation |
| [simulation_software](slots/simulation_software.md) | Name of software used to perform simulation step |
| [simulation_software_version](slots/simulation_software_version.md) | Version of software used to perform simulation step |
| [simulation_time](slots/simulation_time.md) | Total time molecular dynamics have been sampled in a simulation trajectory, o... |
| [simulation_tool](slots/simulation_tool.md) | Tool used to perform simulation |
| [SMILES](slots/SMILES.md) | Simplified Molecular Input Line Entry System (SMILES) ASCII-based line notati... |
| [sockets_per_node](slots/sockets_per_node.md) | Number of physical CPU sockets in each compute node |
| [software](slots/software.md) |  |
| [stages](slots/stages.md) |  |
| [system_charge](slots/system_charge.md) | Total electrostatic charge of the system given by the elementary charge (e) |
| [system_counts](slots/system_counts.md) |  |
| [target_pressure](slots/target_pressure.md) | Target/reference pressure set to reach in the simulation, given as a float or... |
| [target_temperature](slots/target_temperature.md) | Target/reference temperature set to reach in the simulation, given as a list ... |
| [temperature_time_constant](slots/temperature_time_constant.md) | Time constant for coupling the system temperature in seconds units, given as ... |
| [thermostat](slots/thermostat.md) | thermostat information |
| [thermostat_algorithm](slots/thermostat_algorithm.md) | List of thermostat algorithms used in the simulation |
| [threads_per_core](slots/threads_per_core.md) | Number of hardware threads per physical core |
| [time_step](slots/time_step.md) | Time between integration steps in a simulation, given as a float |
| [topology](slots/topology.md) |  |
| [total_atom_count](slots/total_atom_count.md) | Total number of atoms in the simulation |
| [total_molecule_count](slots/total_molecule_count.md) | Total number of simulated molecules, defined as bonded atoms or beads |
| [trajectory](slots/trajectory.md) |  |
| [trajectory_output](slots/trajectory_output.md) | Information included in trajectory files |
| [UNIPROT_ID](slots/UNIPROT_ID.md) | UniProt accession ID |
| [unique_molecule_count](slots/unique_molecule_count.md) | Number of unique simulated molecules, defined as bonded atoms or beads |
| [value](slots/value.md) | value for a given quantity |
| [value_unit](slots/value_unit.md) | unit for a given value |
| [vdw_cutoff_distance](slots/vdw_cutoff_distance.md) | Distance in Angstrom at which a Van der Waals interaction is turned off and a... |
| [vector_value](slots/vector_value.md) | vector value for a given quantity |
| [velocities](slots/velocities.md) | Are per-frame velocities included in the trajectory? |
| [wall_time](slots/wall_time.md) | Total elapsed runtime of the simulation |
| [water](slots/water.md) | Are water molecules included in the trajectory? |
| [water_potential](slots/water_potential.md) | Force field for water molecules |
| [water_potential_name](slots/water_potential_name.md) | Force field used to describe water molecules |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AnalysisMethod](enums/AnalysisMethod.md) | Methods used to analyse simulation outputs |
| [AnalysisSoftware](enums/AnalysisSoftware.md) | Software used to analyse simulation outputs |
| [AnalysisTool](enums/AnalysisTool.md) | Tools used to analyse simulation outputs |
| [AngleUnit](enums/AngleUnit.md) | Units for angles |
| [BarostatAlgorithm](enums/BarostatAlgorithm.md) | Barostat algorithm used to set the pressure in a simulation |
| [BondLengthConstraintsAlgorithm](enums/BondLengthConstraintsAlgorithm.md) | Fix specific molecular degrees of freedom—typically fast bond vibrations invo... |
| [BoxType](enums/BoxType.md) | Types of box used to simulate the system |
| [ByteUnit](enums/ByteUnit.md) | Units for Bytes |
| [CarbohydratePotentialName](enums/CarbohydratePotentialName.md) | Force fields used to parametrize carbohydrates in a simulation |
| [ChargeUnit](enums/ChargeUnit.md) |  |
| [CompressibilityUnit](enums/CompressibilityUnit.md) |  |
| [ConcentrationUnit](enums/ConcentrationUnit.md) |  |
| [ContainerRuntime](enums/ContainerRuntime.md) | Container runtime used to package and run software |
| [CpuArchitecture](enums/CpuArchitecture.md) | CPU architecture used by the compute nodes |
| [CpuVendor](enums/CpuVendor.md) | Vendor of the CPU used in the compute nodes |
| [EnergyUnit](enums/EnergyUnit.md) | Units for energy |
| [EnsembleType](enums/EnsembleType.md) | Ensemble used in a simulation |
| [ExecutionPlatform](enums/ExecutionPlatform.md) | Type of platform used to run the simulation |
| [ForceUnit](enums/ForceUnit.md) |  |
| [FrequencyUnit](enums/FrequencyUnit.md) | Units used to describe frequency |
| [FrictionCoefficientUnit](enums/FrictionCoefficientUnit.md) |  |
| [GeneralPotentialName](enums/GeneralPotentialName.md) | Force fields used to parametrize molecules in a simulation |
| [GpuVendor](enums/GpuVendor.md) | Vendor of the GPU used in the compute nodes |
| [IntegratorAlgorithm](enums/IntegratorAlgorithm.md) | Algorithm used to integrate the simulation |
| [LengthUnit](enums/LengthUnit.md) |  |
| [LipidPotentialName](enums/LipidPotentialName.md) | Force fields used to parametrize lipids in a simulation |
| [LongRangeInteractionMethod](enums/LongRangeInteractionMethod.md) | Method used to implement long-range interactions of point charges in the simu... |
| [MachineLearnedPotentialName](enums/MachineLearnedPotentialName.md) | Machine learned potentials |
| [MassUnit](enums/MassUnit.md) | Units for mass/molecular weight |
| [MinimisationAlgorithm](enums/MinimisationAlgorithm.md) | Algorithm used to minimise particle interactions |
| [ModelResolution](enums/ModelResolution.md) | Resolution of simulated molecules |
| [MolarEnergyUnit](enums/MolarEnergyUnit.md) | Units for molar energy |
| [MPILibrary](enums/MPILibrary.md) | MPI implementation used for message passing |
| [NodeType](enums/NodeType.md) | Type of compute node used in the system |
| [NucleicPotentialName](enums/NucleicPotentialName.md) | Force fields used to parametrize nucleic acids in a simulation |
| [OperatingSystem](enums/OperatingSystem.md) | List of operating systems installed on the hardware used to perform the simul... |
| [PeriodicBoundaryConditions](enums/PeriodicBoundaryConditions.md) | What directions in a simulation cell periodic boundaries are set if they are ... |
| [PolymerPotentialName](enums/PolymerPotentialName.md) | Force fields used to parametrize polymers in a simulation |
| [PressureCouplingType](enums/PressureCouplingType.md) | Coupling type for adjusting box vectors |
| [PressureUnit](enums/PressureUnit.md) |  |
| [ProteinPotentialName](enums/ProteinPotentialName.md) | Force fields used to parametrize amino acids in proteins in a simulation |
| [Scheduler](enums/Scheduler.md) | Job scheduler used for simulation execution |
| [SetupTool](enums/SetupTool.md) | Tool used to setup a system for simulation |
| [SimulationMethod](enums/SimulationMethod.md) | Options for simulation methods |
| [SimulationSoftware](enums/SimulationSoftware.md) | Simulation software used to perform molecular dynamics simulations and relate... |
| [SimulationTool](enums/SimulationTool.md) | Tools/utility used within simulation engines to perform simulations |
| [TemperatureUnit](enums/TemperatureUnit.md) |  |
| [ThermostatAlgorithm](enums/ThermostatAlgorithm.md) | Thermostat algorithm used to set the temperature in a simulation |
| [TimeUnit](enums/TimeUnit.md) | Units used to describe time |
| [VolumeUnit](enums/VolumeUnit.md) |  |
| [WaterPotentialName](enums/WaterPotentialName.md) | Force fields used to parametrize water molecules in a simulation |


## Types

| Type | Description |
| --- | --- |
| [boolean](types/boolean.md) | A binary (true or false) value |
| [curie](types/curie.md) | a compact URI |
| [date](types/date.md) | a date (year, month and day) in an idealized calendar |
| [date_or_datetime](types/date_or_datetime.md) | Either a date or a datetime |
| [datetime](types/datetime.md) | The combination of a date and time |
| [decimal](types/decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [double](types/double.md) | A real number that conforms to the xsd:double specification |
| [float](types/float.md) | A real number that conforms to the xsd:float specification |
| [integer](types/integer.md) | An integer |
| [jsonpath](types/jsonpath.md) | A string encoding a JSON Path |
| [jsonpointer](types/jsonpointer.md) | A string encoding a JSON Pointer |
| [ncname](types/ncname.md) | Prefix part of CURIE |
| [nodeidentifier](types/nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [objectidentifier](types/objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [sparqlpath](types/sparqlpath.md) | A string encoding a SPARQL Property Path |
| [string](types/string.md) | A character string |
| [time](types/time.md) | A time object represents a (local) time of day, independent of any particular... |
| [uri](types/uri.md) | a complete URI |
| [uriorcurie](types/uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
