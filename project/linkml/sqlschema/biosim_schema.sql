-- # Class: SimulationMetadata Description: root class for biosim-schema
--     * Slot: id
--     * Slot: stages_id Description: Simulation stages
--     * Slot: settings_id Description: Simulation settings
--     * Slot: observables_id Description: Simulation observables.
--     * Slot: topology_id Description: Topology information.
--     * Slot: trajectory_id Description: Trajectory information.
--     * Slot: composition_id Description: Composition of simulated system.
--     * Slot: potentials_id Description: Force field potentials used to describe simulated particles.
--     * Slot: compute_id Description: Computational environment information.
-- # Class: LengthQuantity Description: A quantity representing length.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: VolumeQuantity Description: A quantity representing volume.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: TimeQuantity Description: A quantity representing time.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: FrequencyQuantity Description: A quantity representing frequency.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: FrictionCoefficientQuantity Description: A quantity representing friction coefficients.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: MolarEnergyQuantity Description: A quantity representing molar energy.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: EnergyQuantity Description: A quantity representing energy.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: TemperatureQuantity Description: A quantity representing temperature.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: PressureQuantity Description: A quantity representing pressure.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: CompressibilityQuantity Description: A quantity representing compressibility.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: MassQuantity Description: A quantity representing mass.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: ConcentrationQuantity Description: A quantity representing concentration.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: ForceQuantity Description: A quantity representing force.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: ChargeQuantity Description: A quantity representing charge.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: AngleQuantity Description: A quantity representing angles.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: ByteQuantity Description: A quantity representing bytes.
--     * Slot: id
--     * Slot: value
--     * Slot: value_unit
-- # Class: VectorLengthQuantity Description: A quantity representing 3D lengths/dimensions.
--     * Slot: id
--     * Slot: value_unit
-- # Class: VectorAngleQuantity Description: A quantity representing 3D angles.
--     * Slot: id
--     * Slot: value_unit
-- # Class: VectorVolumeQuantity Description: A quantity representing volume as via 3 length dimensions.
--     * Slot: id
--     * Slot: value_unit
-- # Class: VectorCompressibilityQuantity Description: A quantity representing compressibility in 3D.
--     * Slot: id
--     * Slot: vector_value
--     * Slot: value_unit
-- # Class: VectorPressureQuantity Description: A quantity representing pressure in 3D.
--     * Slot: id
--     * Slot: value_unit
-- # Class: VectorTemperatureQuantity Description: Temperature values for multiple coupling groups.
--     * Slot: id
--     * Slot: value_unit
-- # Class: VectorTimeQuantity Description: Time values for multiple coupling groups.
--     * Slot: id
--     * Slot: value_unit
-- # Class: MatrixPressureQuantity Description: A quantity representing pressure vectors in 3D.
--     * Slot: id
--     * Slot: value_unit
-- # Class: MatrixCompressibilityQuantity Description: A quantity representing compressibility vectors in 3D.
--     * Slot: id
--     * Slot: value_unit
-- # Class: MatrixQuantity Description: A quantity representing general vectors in 3D.
--     * Slot: id
--     * Slot: value_unit
-- # Class: SimulationStages Description: Stages of simulation workflow.
--     * Slot: id
--     * Slot: setup_id Description: Setup stage of a simulation.
--     * Slot: minimisation_id Description: Minimisation stage of a simulation.
--     * Slot: equilibration_id Description: Equilibration stage of a simulation.
--     * Slot: production_id Description: Production stage of a simulation.
--     * Slot: analysis_id Description: Analysis stage of a simulation.
-- # Class: Setup Description: Setup stage of simulation workflow.
--     * Slot: id
--     * Slot: setup_tool Description: Name of the tool used to setup simulation.
-- # Class: Minimisation Description: Minimisation stage of simulation workflow.
--     * Slot: id
--     * Slot: number_of_minimisation_steps Description: Number of integration steps performed during minimisation of the system, given as an integer.
--     * Slot: energy_tolerance_id Description: Tolerance energy for when minimization stops, this is when the maximum force on any atom is less than this value (default is often 1000 kJ/mol/nm or 10−4kcal), given as a float.
--     * Slot: minimisation_distance_step_size_id Description: The distance the algorithm moves in a single step, controls how large a step the optimizer takes during the initial phase of minimizing the potential energy of a structure, given as a float.
-- # Class: Equilibration Description: Equilibration stage of simulation workflow.
--     * Slot: id
-- # Class: Production Description: Production stage of simulation workflow.
--     * Slot: id
--     * Slot: simulation_software_version Description: Version of software used to perform simulation step.
-- # Class: Analysis Description: Analysis stage of simulation workflow.
--     * Slot: id
-- # Class: SimulationSettings Description: Settings in simulation.
--     * Slot: id
--     * Slot: ensemble_id Description: Ensemble information.
--     * Slot: integrator_id Description: Integrator information.
--     * Slot: barostat_id Description: Barostat information.
--     * Slot: thermostat_id Description: thermostat information.
--     * Slot: interactions_id Description: Interaction information.
-- # Class: Ensemble Description: Simulation ensemble/thermodynamic properties.
--     * Slot: id
--     * Slot: ensemble_type Description: List of ensemble types used in the simulation.
--     * Slot: random_seed Description: Random number used to set (a) distribution of velocities across particles at the start of a simulation and (b) pseudo-random values for dynamics/couplings, given as an integer.
-- # Class: Interactions Description: Settings used to define particle interactions.
--     * Slot: id
--     * Slot: restraints Description: Are any positional restraints applied to molecule dynamics? (Restraints usually use harmonic potentials to keep a value near a target).
--     * Slot: bond_length_constraints_algorithm Description: Constraints applied to bonds between two particles in the simulated system.
--     * Slot: long_range_interaction_method Description: Method used to describe long-range interactions between particles.
--     * Slot: electrostatic_cutoff_distance_id Description: Distance in Angstrom at which a electrostatic interaction is turned off and a long-range non-bonded method is turned on, given as a float.
--     * Slot: vdw_cutoff_distance_id Description: Distance in Angstrom at which a Van der Waals interaction is turned off and a long-range non-bonded method is turned on.
-- # Class: Integrator Description: Settings used for the simulation integrator.
--     * Slot: id
--     * Slot: integrator_algorithm Description: List of integrator algorithms used to integrate the simulation.
--     * Slot: number_of_steps Description: Number of integration steps performed in the simulation, given as an integer.
--     * Slot: frame_step_id Description: Time between saved snapshots/frames in a simulation, given as a float.
--     * Slot: time_step_id Description: Time between integration steps in a simulation, given as a float.
--     * Slot: simulation_time_id Description: Total time molecular dynamics have been sampled in a simulation trajectory, often given by the number of integration steps multiplied by the simulation time step used by the integrator, given as a float.
-- # Class: Barostat Description: Settings used for the simulation barostat.
--     * Slot: id
--     * Slot: barostat_algorithm Description: List of barostat algorithms used in the simulation.
--     * Slot: pressure_coupling_frequency Description: Step frequency to apply the barostat, given as an integer.
--     * Slot: pressure_coupling_type Description: List of coupling types for adjusting box vectors.
--     * Slot: compressibility_id Description: Compressibility of the simulated system, given as a float.
--     * Slot: compressibility_vector_id Description: Compressibility of the simulated system, given as a float.
--     * Slot: target_pressure_id Description: Target/reference pressure set to reach in the simulation, given as a float.
--     * Slot: target_pressure_vector_id Description: Target/reference pressure set to reach in the simulation, given as a 3x3 array.
--     * Slot: pressure_time_constant_id Description: Time constant/step (relaxation time of pressure) used for coupling the system pressure, given as a float.
-- # Class: Thermostat Description: Settings used for the simulation thermostat.
--     * Slot: id
--     * Slot: thermostat_algorithm Description: List of thermostat algorithms used in the simulation.
--     * Slot: coupling_group Description: A subset of atoms for which temperature is controlled, often needed for simulating complex systems (e.g., protein in water), used in gromacs, given as a string
--     * Slot: chain_length Description: Usually required in the Nosé-Hoover thermostat, the chain length (e.g., nh-chain-length in GROMACS) is used to maintain canonical distribution, given as an integer.
--     * Slot: target_temperature_id Description: Target/reference temperature set to reach in the simulation, given as a float.
--     * Slot: target_temperature_vector_id Description: Target/reference temperature set to reach in the simulation, given as a list (e.g. 300, 300).
--     * Slot: collision_frequency_id Description: Collision frequency for the integrator, given as a float.
--     * Slot: temperature_time_constant_id Description: Time constant for coupling the system temperature in seconds units, given as a list (e.g. 300, 300).
--     * Slot: friction_coefficient_id Description: Usually used in the Langevin thermostat, the friction coefficient determines the strength of coupling between a system and a heat bath, given as a float.
-- # Class: SystemComposition Description: Molecular composition of simulated system.
--     * Slot: id
--     * Slot: system_counts_id Description: Entity counts across the simulated system.
-- # Class: SystemCounts Description: Entity counts across the simulated system.
--     * Slot: id
--     * Slot: total_molecule_count Description: Total number of simulated molecules, defined as bonded atoms or beads.
--     * Slot: total_atom_count Description: Total number of atoms in the simulation.
--     * Slot: unique_molecule_count Description: Number of unique simulated molecules, defined as bonded atoms or beads.
--     * Slot: salt_concentration_id Description: Concentration of salt in the solution.
-- # Class: MoleculeID Description: Identifiers of a molecule type in the simulated system.
--     * Slot: id
--     * Slot: PDB_ID Description: Protein Data Bank identifier
--     * Slot: UNIPROT_ID Description: UniProt accession ID
--     * Slot: SMILES Description: Simplified Molecular Input Line Entry System (SMILES) ASCII-based line notation used to describe chemical structures. It represents molecular graphs with atoms and bonds, allowing software to convert these short strings into 2D or 3D models.
--     * Slot: InChI Description: The International Chemical Identifier (InChi) is a textual identifier for chemical substances, designed to provide a standard way to encode molecular information
--     * Slot: InChIKey Description: The condensed, 27 character InChIKey, which is a hashed version of the full InChI (using the SHA-256 algorithm), designed to allow for easy web searches of chemical compounds.
--     * Slot: alphafold_ID Description: AlphaFold predicted protein structure identifier (AlphaFold DB, EMBL-EBI)
--     * Slot: PubChem_CID Description: PubChem CID of chemical molecules and their activities against biological assays.
--     * Slot: protein_sequence Description: One letter sequence for protein amino acids.
--     * Slot: nucleic_sequence Description: One letter sequence for nucleic acid nucleotides.
--     * Slot: predicted_structure Description: Are the molecule positions derived from a prediction?
--     * Slot: modified Description: Has the initial model been modified from the original?
--     * Slot: molecular_formula Description: The molecular formula of a molecule\
--     * Slot: molecule_count Description: Number of instances of a given molecule, defined as bonded atoms or beads.
--     * Slot: atom_count Description: Number of atoms in a molecule.
--     * Slot: monomer_count Description: Number of monomeric units in a polymer(e.g. protein or nucleic acid).
--     * Slot: SystemComposition_id Description: Autocreated FK slot
--     * Slot: molecular_weight_id Description: The molecular weight of a molecule.
--     * Slot: molecule_charge_id Description: Electrostatic charge of a molecule.
-- # Class: SimulationObservables Description: Simulation observables outputted from simulation.
--     * Slot: id
--     * Slot: simulation_averages_id Description: Average values of observables outputted from the simulation.
-- # Class: SimulationAverages Description: Average values of observables outputted from the simulation.
--     * Slot: id
--     * Slot: average_kinetic_energy_id Description: Average kinetic energy sampled from the simulation, given as a float.
--     * Slot: average_potential_energy_id Description: Average potential energy sampled from the simulation, given as a float.
--     * Slot: average_enthalpy_id Description: Average enthalpy sampled from the simulation, given as a float.
--     * Slot: average_pressure_id Description: Average pressure sampled from the simulation, given as a float.
--     * Slot: average_temperature_id Description: Average temperature sampled from the simulation, given as a float.
--     * Slot: average_volume_id Description: Average volume sampled from the simulation, given as a float.
--     * Slot: average_volume_vector_id Description: Average volume sampled from the simulation, given as a list, (e.g. 10, 10, 10).
-- # Class: TopologyMetadata Description: Topology information.
--     * Slot: id
--     * Slot: connectivity_id Description: Particle connectivity information
--     * Slot: particles_id Description: Particles information
-- # Class: Connectivity Description: Connectivity information included in the topology.
--     * Slot: id
--     * Slot: bonds Description: Are bond parameters present in the topology?
--     * Slot: dihedrals Description: Are dihedral parameters present in the topology?
-- # Class: Particles Description: Particle information included in the topology.
--     * Slot: id
--     * Slot: masses Description: Are masses present in the topology?
--     * Slot: fixed_charges Description: Are fixed charges on atoms included in the topology?
--     * Slot: coarse_grained Description: Are atoms coarse-grained?
--     * Slot: resolution Description: Resolution of simulated system.
--     * Slot: system_charge_id Description: Total electrostatic charge of the system given by the elementary charge (e).
-- # Class: TrajectoryMetadata Description: Trajectory information.
--     * Slot: id
--     * Slot: simulation_box_id Description: Information about the simulation box.
--     * Slot: trajectory_output_id Description: Information included in trajectory files.
-- # Class: SimulationBox Description: Simulation box information
--     * Slot: id
--     * Slot: box_type Description: The type of box used to simuluate the system.
--     * Slot: periodic_boundary_conditions Description: What directions in a simulation cell periodic boundaries are set if they are turned on.
--     * Slot: box_dimensions_id Description: The lengths/dimensions of the box used to simulate the system.
--     * Slot: box_angles_id Description: The angles of the box used to simulate the system.
-- # Class: Trajectories Description: Information in trajectory files.
--     * Slot: id
--     * Slot: positions Description: Are per-frame positions included in the trajectory?
--     * Slot: forces Description: Are per-frame forces included in the trajectory?
--     * Slot: velocities Description: Are per-frame velocities included in the trajectory?
--     * Slot: polarizable_charges Description: Are per-frame polarizable charges included in the trajectory?
--     * Slot: energies Description: Are per-frame energies included in the trajectory?
--     * Slot: water Description: Are water molecules included in the trajectory?
--     * Slot: replica Description: Is this trajectory a replica of another provided trajectory?
--     * Slot: frame_count Description: Total number of snapshots that make up a trajectory.
-- # Class: PotentialMetadata Description: Potentials used for various modelled molecules.
--     * Slot: id
--     * Slot: water_potential_id Description: Force field for water molecules.
--     * Slot: protein_potential_id Description: Force field for proteins.
--     * Slot: lipid_potential_id Description: Force field for lipids.
--     * Slot: nucleic_potential_id Description: Force field for nucleic acids.
--     * Slot: carbohydrate_potential_id Description: Force field for carbohydrates.
--     * Slot: polymer_potential_id Description: Force field for polymers (excluding proteins and nucleic acids).
--     * Slot: general_potential_id Description: Force field for molecules (in general).
--     * Slot: machine_learned_potential_id Description: ML force field for molecules (in general).
-- # Class: WaterPotential Description: Potential used for water molecules.
--     * Slot: id
--     * Slot: water_potential_name Description: Force field used to describe water molecules.
--     * Slot: modified Description: Has the initial model been modified from the original?
-- # Class: ProteinPotential Description: Potential used for protein molecules.
--     * Slot: id
--     * Slot: protein_potential_name Description: Force field used to describe proteins.
--     * Slot: modified Description: Has the initial model been modified from the original?
-- # Class: LipidPotential Description: Potential used for lipid molecules.
--     * Slot: id
--     * Slot: lipid_potential_name Description: Force field used to describe lipids.
--     * Slot: modified Description: Has the initial model been modified from the original?
-- # Class: NucleicPotential Description: Potential used for nucleic acid molecules.
--     * Slot: id
--     * Slot: nucleic_potential_name Description: Force field used to describe nucleic acids.
--     * Slot: modified Description: Has the initial model been modified from the original?
-- # Class: CarbohydratePotential Description: Potential used for carbohydrate molecules.
--     * Slot: id
--     * Slot: carbohydrate_potential_name Description: Force field used to describe carbohydrate.
--     * Slot: modified Description: Has the initial model been modified from the original?
-- # Class: PolymerPotential Description: Potential used for polymers molecules.
--     * Slot: id
--     * Slot: polymer_potential_name Description: Force field used to describe polymers (excluding proteins and nucleic acids).
--     * Slot: modified Description: Has the initial model been modified from the original?
-- # Class: GeneralPotential Description: Potential used for molecules.
--     * Slot: id
--     * Slot: general_potential_name Description: Force field used to describe molecules.
--     * Slot: modified Description: Has the initial model been modified from the original?
-- # Class: MachineLearnedPotential Description: Machine learned potential used for molecules.
--     * Slot: id
--     * Slot: machine_learned_potential_name Description: ML force field used to describe molecules.
--     * Slot: modified Description: Has the initial model been modified from the original?
-- # Class: ComputationalEnvironment Description: Computational environment used to perform simulation.
--     * Slot: id
--     * Slot: hardware_id Description: Computer hardware used to perform simulation.
--     * Slot: software_id Description: Computer software used to perform simulation.
--     * Slot: performance_id Description: Compute performance during simulation.
-- # Class: Hardware Description: Computer hardware used to perform simulation.
--     * Slot: id
--     * Slot: execution_platform Description: Broad type of system used to run the simulation workload.
--     * Slot: node_type Description: Compute node profile used for the simulation run.
--     * Slot: node_count Description: Number of compute nodes used for the run.
--     * Slot: CPU_vendor Description: CPU vendor used in the compute nodes.
--     * Slot: CPU_architecture Description: CPU instruction-set architecture of the compute nodes.
--     * Slot: sockets_per_node Description: Number of physical CPU sockets in each compute node.
--     * Slot: cores_per_socket Description: Number of physical CPU cores in each socket.
--     * Slot: threads_per_core Description: Number of hardware threads per physical core.
--     * Slot: GPU_vendor Description: GPU vendor used by the compute nodes, if applicable.
--     * Slot: GPUs_per_node Description: Number of GPUs present in each compute node.
--     * Slot: memory_per_node_id Description: Amount of memory installed per compute node.
-- # Class: Software Description: Computer software used to perform simulation.
--     * Slot: id
--     * Slot: operating_system Description: Operating system installed on the hardware used to perform the simulation.
--     * Slot: scheduler Description: Workload manager or job scheduler used to launch the simulation.
--     * Slot: MPI_library Description: MPI implementation used for distributed parallel execution.
--     * Slot: container_runtime Description: Container runtime used to execute the simulation environment, if any.
-- # Class: Performance Description: Compute performance during simulation.
--     * Slot: id
--     * Slot: wall_time_id Description: Total elapsed runtime of the simulation.
--     * Slot: energy_consumption_id Description: Total energy consumed by the simulation run.
-- # Class: VectorLengthQuantity_vector_value
--     * Slot: VectorLengthQuantity_id Description: Autocreated FK slot
--     * Slot: vector_value
-- # Class: VectorAngleQuantity_vector_value
--     * Slot: VectorAngleQuantity_id Description: Autocreated FK slot
--     * Slot: vector_value
-- # Class: VectorVolumeQuantity_vector_value
--     * Slot: VectorVolumeQuantity_id Description: Autocreated FK slot
--     * Slot: vector_value
-- # Class: VectorPressureQuantity_vector_value
--     * Slot: VectorPressureQuantity_id Description: Autocreated FK slot
--     * Slot: vector_value
-- # Class: VectorTemperatureQuantity_vector_value
--     * Slot: VectorTemperatureQuantity_id Description: Autocreated FK slot
--     * Slot: vector_value
-- # Class: VectorTimeQuantity_vector_value
--     * Slot: VectorTimeQuantity_id Description: Autocreated FK slot
--     * Slot: vector_value
-- # Class: MatrixPressureQuantity_vector_value
--     * Slot: MatrixPressureQuantity_id Description: Autocreated FK slot
--     * Slot: vector_value
-- # Class: MatrixCompressibilityQuantity_vector_value
--     * Slot: MatrixCompressibilityQuantity_id Description: Autocreated FK slot
--     * Slot: vector_value
-- # Class: MatrixQuantity_vector_value
--     * Slot: MatrixQuantity_id Description: Autocreated FK slot
--     * Slot: vector_value
-- # Class: Minimisation_minimisation_algorithm
--     * Slot: Minimisation_id Description: Autocreated FK slot
--     * Slot: minimisation_algorithm Description: Name of the method used to minimise the molecular system.
-- # Class: Minimisation_simulation_tool
--     * Slot: Minimisation_id Description: Autocreated FK slot
--     * Slot: simulation_tool Description: Tool used to perform simulation.
-- # Class: Minimisation_simulation_software
--     * Slot: Minimisation_id Description: Autocreated FK slot
--     * Slot: simulation_software Description: Name of software used to perform simulation step.
-- # Class: Equilibration_simulation_tool
--     * Slot: Equilibration_id Description: Autocreated FK slot
--     * Slot: simulation_tool Description: Tool used to perform simulation.
-- # Class: Equilibration_simulation_software
--     * Slot: Equilibration_id Description: Autocreated FK slot
--     * Slot: simulation_software Description: Name of software used to perform simulation step.
-- # Class: Production_simulation_tool
--     * Slot: Production_id Description: Autocreated FK slot
--     * Slot: simulation_tool Description: Tool used to perform simulation.
-- # Class: Production_simulation_software
--     * Slot: Production_id Description: Autocreated FK slot
--     * Slot: simulation_software Description: Name of software used to perform simulation step.
-- # Class: Production_simulation_method
--     * Slot: Production_id Description: Autocreated FK slot
--     * Slot: simulation_method Description: Method used to perform simulation.
-- # Class: Analysis_analysis_tool
--     * Slot: Analysis_id Description: Autocreated FK slot
--     * Slot: analysis_tool Description: Name of the tool used to analyse simulation.
-- # Class: Analysis_analysis_software
--     * Slot: Analysis_id Description: Autocreated FK slot
--     * Slot: analysis_software Description: Name of software used to analyse simulation.
-- # Class: Analysis_analysis_method
--     * Slot: Analysis_id Description: Autocreated FK slot
--     * Slot: analysis_method Description: Name of the method used to analyse simulation.

CREATE TABLE "LengthQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(2),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LengthQuantity_id" ON "LengthQuantity" (id);

CREATE TABLE "VolumeQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(3),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VolumeQuantity_id" ON "VolumeQuantity" (id);

CREATE TABLE "TimeQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(2),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TimeQuantity_id" ON "TimeQuantity" (id);

CREATE TABLE "FrequencyQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(4),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_FrequencyQuantity_id" ON "FrequencyQuantity" (id);

CREATE TABLE "FrictionCoefficientQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(4),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_FrictionCoefficientQuantity_id" ON "FrictionCoefficientQuantity" (id);

CREATE TABLE "MolarEnergyQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(8),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MolarEnergyQuantity_id" ON "MolarEnergyQuantity" (id);

CREATE TABLE "EnergyQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(3),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_EnergyQuantity_id" ON "EnergyQuantity" (id);

CREATE TABLE "TemperatureQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(2),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TemperatureQuantity_id" ON "TemperatureQuantity" (id);

CREATE TABLE "PressureQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(3),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PressureQuantity_id" ON "PressureQuantity" (id);

CREATE TABLE "CompressibilityQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(5),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CompressibilityQuantity_id" ON "CompressibilityQuantity" (id);

CREATE TABLE "MassQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(5),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MassQuantity_id" ON "MassQuantity" (id);

CREATE TABLE "ConcentrationQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(1),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ConcentrationQuantity_id" ON "ConcentrationQuantity" (id);

CREATE TABLE "ForceQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(10),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ForceQuantity_id" ON "ForceQuantity" (id);

CREATE TABLE "ChargeQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(1),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ChargeQuantity_id" ON "ChargeQuantity" (id);

CREATE TABLE "AngleQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(6),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AngleQuantity_id" ON "AngleQuantity" (id);

CREATE TABLE "ByteQuantity" (
	id INTEGER NOT NULL,
	value FLOAT,
	value_unit VARCHAR(2),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ByteQuantity_id" ON "ByteQuantity" (id);

CREATE TABLE "VectorLengthQuantity" (
	id INTEGER NOT NULL,
	value_unit VARCHAR(2),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VectorLengthQuantity_id" ON "VectorLengthQuantity" (id);

CREATE TABLE "VectorAngleQuantity" (
	id INTEGER NOT NULL,
	value_unit VARCHAR(6),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VectorAngleQuantity_id" ON "VectorAngleQuantity" (id);

CREATE TABLE "VectorVolumeQuantity" (
	id INTEGER NOT NULL,
	value_unit VARCHAR(2),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VectorVolumeQuantity_id" ON "VectorVolumeQuantity" (id);

CREATE TABLE "VectorCompressibilityQuantity" (
	id INTEGER NOT NULL,
	vector_value FLOAT,
	value_unit VARCHAR(5),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VectorCompressibilityQuantity_id" ON "VectorCompressibilityQuantity" (id);

CREATE TABLE "VectorPressureQuantity" (
	id INTEGER NOT NULL,
	value_unit VARCHAR(3),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VectorPressureQuantity_id" ON "VectorPressureQuantity" (id);

CREATE TABLE "VectorTemperatureQuantity" (
	id INTEGER NOT NULL,
	value_unit VARCHAR(2),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VectorTemperatureQuantity_id" ON "VectorTemperatureQuantity" (id);

CREATE TABLE "VectorTimeQuantity" (
	id INTEGER NOT NULL,
	value_unit VARCHAR(2),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VectorTimeQuantity_id" ON "VectorTimeQuantity" (id);

CREATE TABLE "MatrixPressureQuantity" (
	id INTEGER NOT NULL,
	value_unit VARCHAR(3),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MatrixPressureQuantity_id" ON "MatrixPressureQuantity" (id);

CREATE TABLE "MatrixCompressibilityQuantity" (
	id INTEGER NOT NULL,
	value_unit VARCHAR(5),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MatrixCompressibilityQuantity_id" ON "MatrixCompressibilityQuantity" (id);

CREATE TABLE "MatrixQuantity" (
	id INTEGER NOT NULL,
	value_unit TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MatrixQuantity_id" ON "MatrixQuantity" (id);

CREATE TABLE "Setup" (
	id INTEGER NOT NULL,
	setup_tool VARCHAR(14),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Setup_id" ON "Setup" (id);

CREATE TABLE "Equilibration" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Equilibration_id" ON "Equilibration" (id);

CREATE TABLE "Production" (
	id INTEGER NOT NULL,
	simulation_software_version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Production_id" ON "Production" (id);

CREATE TABLE "Analysis" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Analysis_id" ON "Analysis" (id);

CREATE TABLE "Ensemble" (
	id INTEGER NOT NULL,
	ensemble_type VARCHAR(3),
	random_seed INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Ensemble_id" ON "Ensemble" (id);

CREATE TABLE "Connectivity" (
	id INTEGER NOT NULL,
	bonds BOOLEAN,
	dihedrals BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Connectivity_id" ON "Connectivity" (id);

CREATE TABLE "Trajectories" (
	id INTEGER NOT NULL,
	positions BOOLEAN,
	forces BOOLEAN,
	velocities BOOLEAN,
	polarizable_charges BOOLEAN,
	energies BOOLEAN,
	water BOOLEAN,
	replica BOOLEAN,
	frame_count INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Trajectories_id" ON "Trajectories" (id);

CREATE TABLE "WaterPotential" (
	id INTEGER NOT NULL,
	water_potential_name VARCHAR(8),
	modified BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_WaterPotential_id" ON "WaterPotential" (id);

CREATE TABLE "ProteinPotential" (
	id INTEGER NOT NULL,
	protein_potential_name VARCHAR(12),
	modified BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ProteinPotential_id" ON "ProteinPotential" (id);

CREATE TABLE "LipidPotential" (
	id INTEGER NOT NULL,
	lipid_potential_name VARCHAR(7),
	modified BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LipidPotential_id" ON "LipidPotential" (id);

CREATE TABLE "NucleicPotential" (
	id INTEGER NOT NULL,
	nucleic_potential_name VARCHAR(22),
	modified BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NucleicPotential_id" ON "NucleicPotential" (id);

CREATE TABLE "CarbohydratePotential" (
	id INTEGER NOT NULL,
	carbohydrate_potential_name VARCHAR(12),
	modified BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CarbohydratePotential_id" ON "CarbohydratePotential" (id);

CREATE TABLE "PolymerPotential" (
	id INTEGER NOT NULL,
	polymer_potential_name VARCHAR(9),
	modified BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PolymerPotential_id" ON "PolymerPotential" (id);

CREATE TABLE "GeneralPotential" (
	id INTEGER NOT NULL,
	general_potential_name VARCHAR(9),
	modified BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GeneralPotential_id" ON "GeneralPotential" (id);

CREATE TABLE "MachineLearnedPotential" (
	id INTEGER NOT NULL,
	machine_learned_potential_name VARCHAR(6),
	modified BOOLEAN,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MachineLearnedPotential_id" ON "MachineLearnedPotential" (id);

CREATE TABLE "Software" (
	id INTEGER NOT NULL,
	operating_system VARCHAR(7),
	scheduler VARCHAR(5),
	"MPI_library" VARCHAR(8),
	container_runtime VARCHAR(9),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Software_id" ON "Software" (id);

CREATE TABLE "Minimisation" (
	id INTEGER NOT NULL,
	number_of_minimisation_steps INTEGER,
	energy_tolerance_id INTEGER,
	minimisation_distance_step_size_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(energy_tolerance_id) REFERENCES "ForceQuantity" (id),
	FOREIGN KEY(minimisation_distance_step_size_id) REFERENCES "LengthQuantity" (id)
);
CREATE INDEX "ix_Minimisation_id" ON "Minimisation" (id);

CREATE TABLE "Interactions" (
	id INTEGER NOT NULL,
	restraints BOOLEAN,
	bond_length_constraints_algorithm VARCHAR(6),
	long_range_interaction_method VARCHAR(6),
	electrostatic_cutoff_distance_id INTEGER,
	vdw_cutoff_distance_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(electrostatic_cutoff_distance_id) REFERENCES "LengthQuantity" (id),
	FOREIGN KEY(vdw_cutoff_distance_id) REFERENCES "LengthQuantity" (id)
);
CREATE INDEX "ix_Interactions_id" ON "Interactions" (id);

CREATE TABLE "Integrator" (
	id INTEGER NOT NULL,
	integrator_algorithm VARCHAR(15),
	number_of_steps INTEGER,
	frame_step_id INTEGER,
	time_step_id INTEGER,
	simulation_time_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(frame_step_id) REFERENCES "TimeQuantity" (id),
	FOREIGN KEY(time_step_id) REFERENCES "TimeQuantity" (id),
	FOREIGN KEY(simulation_time_id) REFERENCES "TimeQuantity" (id)
);
CREATE INDEX "ix_Integrator_id" ON "Integrator" (id);

CREATE TABLE "Barostat" (
	id INTEGER NOT NULL,
	barostat_algorithm VARCHAR(30),
	pressure_coupling_frequency INTEGER,
	pressure_coupling_type VARCHAR(15),
	compressibility_id INTEGER,
	compressibility_vector_id INTEGER,
	target_pressure_id INTEGER,
	target_pressure_vector_id INTEGER,
	pressure_time_constant_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(compressibility_id) REFERENCES "CompressibilityQuantity" (id),
	FOREIGN KEY(compressibility_vector_id) REFERENCES "MatrixCompressibilityQuantity" (id),
	FOREIGN KEY(target_pressure_id) REFERENCES "PressureQuantity" (id),
	FOREIGN KEY(target_pressure_vector_id) REFERENCES "MatrixPressureQuantity" (id),
	FOREIGN KEY(pressure_time_constant_id) REFERENCES "TimeQuantity" (id)
);
CREATE INDEX "ix_Barostat_id" ON "Barostat" (id);

CREATE TABLE "Thermostat" (
	id INTEGER NOT NULL,
	thermostat_algorithm VARCHAR(11),
	coupling_group TEXT,
	chain_length INTEGER,
	target_temperature_id INTEGER,
	target_temperature_vector_id INTEGER,
	collision_frequency_id INTEGER,
	temperature_time_constant_id INTEGER,
	friction_coefficient_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(target_temperature_id) REFERENCES "TemperatureQuantity" (id),
	FOREIGN KEY(target_temperature_vector_id) REFERENCES "VectorTemperatureQuantity" (id),
	FOREIGN KEY(collision_frequency_id) REFERENCES "FrequencyQuantity" (id),
	FOREIGN KEY(temperature_time_constant_id) REFERENCES "VectorTimeQuantity" (id),
	FOREIGN KEY(friction_coefficient_id) REFERENCES "FrictionCoefficientQuantity" (id)
);
CREATE INDEX "ix_Thermostat_id" ON "Thermostat" (id);

CREATE TABLE "SystemCounts" (
	id INTEGER NOT NULL,
	total_molecule_count INTEGER,
	total_atom_count INTEGER,
	unique_molecule_count INTEGER,
	salt_concentration_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(salt_concentration_id) REFERENCES "ConcentrationQuantity" (id)
);
CREATE INDEX "ix_SystemCounts_id" ON "SystemCounts" (id);

CREATE TABLE "SimulationAverages" (
	id INTEGER NOT NULL,
	average_kinetic_energy_id INTEGER,
	average_potential_energy_id INTEGER,
	average_enthalpy_id INTEGER,
	average_pressure_id INTEGER,
	average_temperature_id INTEGER,
	average_volume_id INTEGER,
	average_volume_vector_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(average_kinetic_energy_id) REFERENCES "MolarEnergyQuantity" (id),
	FOREIGN KEY(average_potential_energy_id) REFERENCES "MolarEnergyQuantity" (id),
	FOREIGN KEY(average_enthalpy_id) REFERENCES "MolarEnergyQuantity" (id),
	FOREIGN KEY(average_pressure_id) REFERENCES "PressureQuantity" (id),
	FOREIGN KEY(average_temperature_id) REFERENCES "TemperatureQuantity" (id),
	FOREIGN KEY(average_volume_id) REFERENCES "VolumeQuantity" (id),
	FOREIGN KEY(average_volume_vector_id) REFERENCES "VectorVolumeQuantity" (id)
);
CREATE INDEX "ix_SimulationAverages_id" ON "SimulationAverages" (id);

CREATE TABLE "Particles" (
	id INTEGER NOT NULL,
	masses BOOLEAN,
	fixed_charges BOOLEAN,
	coarse_grained BOOLEAN,
	resolution VARCHAR(14),
	system_charge_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(system_charge_id) REFERENCES "ChargeQuantity" (id)
);
CREATE INDEX "ix_Particles_id" ON "Particles" (id);

CREATE TABLE "SimulationBox" (
	id INTEGER NOT NULL,
	box_type VARCHAR(20),
	periodic_boundary_conditions VARCHAR(4),
	box_dimensions_id INTEGER,
	box_angles_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(box_dimensions_id) REFERENCES "VectorLengthQuantity" (id),
	FOREIGN KEY(box_angles_id) REFERENCES "VectorAngleQuantity" (id)
);
CREATE INDEX "ix_SimulationBox_id" ON "SimulationBox" (id);

CREATE TABLE "PotentialMetadata" (
	id INTEGER NOT NULL,
	water_potential_id INTEGER,
	protein_potential_id INTEGER,
	lipid_potential_id INTEGER,
	nucleic_potential_id INTEGER,
	carbohydrate_potential_id INTEGER,
	polymer_potential_id INTEGER,
	general_potential_id INTEGER,
	machine_learned_potential_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(water_potential_id) REFERENCES "WaterPotential" (id),
	FOREIGN KEY(protein_potential_id) REFERENCES "ProteinPotential" (id),
	FOREIGN KEY(lipid_potential_id) REFERENCES "LipidPotential" (id),
	FOREIGN KEY(nucleic_potential_id) REFERENCES "NucleicPotential" (id),
	FOREIGN KEY(carbohydrate_potential_id) REFERENCES "CarbohydratePotential" (id),
	FOREIGN KEY(polymer_potential_id) REFERENCES "PolymerPotential" (id),
	FOREIGN KEY(general_potential_id) REFERENCES "GeneralPotential" (id),
	FOREIGN KEY(machine_learned_potential_id) REFERENCES "MachineLearnedPotential" (id)
);
CREATE INDEX "ix_PotentialMetadata_id" ON "PotentialMetadata" (id);

CREATE TABLE "Hardware" (
	id INTEGER NOT NULL,
	execution_platform VARCHAR(11),
	node_type VARCHAR(15),
	node_count INTEGER,
	"CPU_vendor" VARCHAR(5),
	"CPU_architecture" VARCHAR(3),
	sockets_per_node INTEGER,
	cores_per_socket INTEGER,
	threads_per_core INTEGER,
	"GPU_vendor" VARCHAR(6),
	"GPUs_per_node" INTEGER,
	memory_per_node_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(memory_per_node_id) REFERENCES "ByteQuantity" (id)
);
CREATE INDEX "ix_Hardware_id" ON "Hardware" (id);

CREATE TABLE "Performance" (
	id INTEGER NOT NULL,
	wall_time_id INTEGER,
	energy_consumption_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(wall_time_id) REFERENCES "TimeQuantity" (id),
	FOREIGN KEY(energy_consumption_id) REFERENCES "EnergyQuantity" (id)
);
CREATE INDEX "ix_Performance_id" ON "Performance" (id);

CREATE TABLE "VectorLengthQuantity_vector_value" (
	"VectorLengthQuantity_id" INTEGER,
	vector_value FLOAT,
	PRIMARY KEY ("VectorLengthQuantity_id", vector_value),
	FOREIGN KEY("VectorLengthQuantity_id") REFERENCES "VectorLengthQuantity" (id)
);
CREATE INDEX "ix_VectorLengthQuantity_vector_value_VectorLengthQuantity_id" ON "VectorLengthQuantity_vector_value" ("VectorLengthQuantity_id");
CREATE INDEX "ix_VectorLengthQuantity_vector_value_vector_value" ON "VectorLengthQuantity_vector_value" (vector_value);

CREATE TABLE "VectorAngleQuantity_vector_value" (
	"VectorAngleQuantity_id" INTEGER,
	vector_value FLOAT,
	PRIMARY KEY ("VectorAngleQuantity_id", vector_value),
	FOREIGN KEY("VectorAngleQuantity_id") REFERENCES "VectorAngleQuantity" (id)
);
CREATE INDEX "ix_VectorAngleQuantity_vector_value_VectorAngleQuantity_id" ON "VectorAngleQuantity_vector_value" ("VectorAngleQuantity_id");
CREATE INDEX "ix_VectorAngleQuantity_vector_value_vector_value" ON "VectorAngleQuantity_vector_value" (vector_value);

CREATE TABLE "VectorVolumeQuantity_vector_value" (
	"VectorVolumeQuantity_id" INTEGER,
	vector_value FLOAT,
	PRIMARY KEY ("VectorVolumeQuantity_id", vector_value),
	FOREIGN KEY("VectorVolumeQuantity_id") REFERENCES "VectorVolumeQuantity" (id)
);
CREATE INDEX "ix_VectorVolumeQuantity_vector_value_VectorVolumeQuantity_id" ON "VectorVolumeQuantity_vector_value" ("VectorVolumeQuantity_id");
CREATE INDEX "ix_VectorVolumeQuantity_vector_value_vector_value" ON "VectorVolumeQuantity_vector_value" (vector_value);

CREATE TABLE "VectorPressureQuantity_vector_value" (
	"VectorPressureQuantity_id" INTEGER,
	vector_value FLOAT,
	PRIMARY KEY ("VectorPressureQuantity_id", vector_value),
	FOREIGN KEY("VectorPressureQuantity_id") REFERENCES "VectorPressureQuantity" (id)
);
CREATE INDEX "ix_VectorPressureQuantity_vector_value_VectorPressureQuantity_id" ON "VectorPressureQuantity_vector_value" ("VectorPressureQuantity_id");
CREATE INDEX "ix_VectorPressureQuantity_vector_value_vector_value" ON "VectorPressureQuantity_vector_value" (vector_value);

CREATE TABLE "VectorTemperatureQuantity_vector_value" (
	"VectorTemperatureQuantity_id" INTEGER,
	vector_value FLOAT,
	PRIMARY KEY ("VectorTemperatureQuantity_id", vector_value),
	FOREIGN KEY("VectorTemperatureQuantity_id") REFERENCES "VectorTemperatureQuantity" (id)
);
CREATE INDEX "ix_VectorTemperatureQuantity_vector_value_VectorTemperatureQuantity_id" ON "VectorTemperatureQuantity_vector_value" ("VectorTemperatureQuantity_id");
CREATE INDEX "ix_VectorTemperatureQuantity_vector_value_vector_value" ON "VectorTemperatureQuantity_vector_value" (vector_value);

CREATE TABLE "VectorTimeQuantity_vector_value" (
	"VectorTimeQuantity_id" INTEGER,
	vector_value FLOAT,
	PRIMARY KEY ("VectorTimeQuantity_id", vector_value),
	FOREIGN KEY("VectorTimeQuantity_id") REFERENCES "VectorTimeQuantity" (id)
);
CREATE INDEX "ix_VectorTimeQuantity_vector_value_VectorTimeQuantity_id" ON "VectorTimeQuantity_vector_value" ("VectorTimeQuantity_id");
CREATE INDEX "ix_VectorTimeQuantity_vector_value_vector_value" ON "VectorTimeQuantity_vector_value" (vector_value);

CREATE TABLE "MatrixPressureQuantity_vector_value" (
	"MatrixPressureQuantity_id" INTEGER,
	vector_value FLOAT,
	PRIMARY KEY ("MatrixPressureQuantity_id", vector_value),
	FOREIGN KEY("MatrixPressureQuantity_id") REFERENCES "MatrixPressureQuantity" (id)
);
CREATE INDEX "ix_MatrixPressureQuantity_vector_value_MatrixPressureQuantity_id" ON "MatrixPressureQuantity_vector_value" ("MatrixPressureQuantity_id");
CREATE INDEX "ix_MatrixPressureQuantity_vector_value_vector_value" ON "MatrixPressureQuantity_vector_value" (vector_value);

CREATE TABLE "MatrixCompressibilityQuantity_vector_value" (
	"MatrixCompressibilityQuantity_id" INTEGER,
	vector_value FLOAT,
	PRIMARY KEY ("MatrixCompressibilityQuantity_id", vector_value),
	FOREIGN KEY("MatrixCompressibilityQuantity_id") REFERENCES "MatrixCompressibilityQuantity" (id)
);
CREATE INDEX "ix_MatrixCompressibilityQuantity_vector_value_MatrixCompressibilityQuantity_id" ON "MatrixCompressibilityQuantity_vector_value" ("MatrixCompressibilityQuantity_id");
CREATE INDEX "ix_MatrixCompressibilityQuantity_vector_value_vector_value" ON "MatrixCompressibilityQuantity_vector_value" (vector_value);

CREATE TABLE "MatrixQuantity_vector_value" (
	"MatrixQuantity_id" INTEGER,
	vector_value FLOAT,
	PRIMARY KEY ("MatrixQuantity_id", vector_value),
	FOREIGN KEY("MatrixQuantity_id") REFERENCES "MatrixQuantity" (id)
);
CREATE INDEX "ix_MatrixQuantity_vector_value_MatrixQuantity_id" ON "MatrixQuantity_vector_value" ("MatrixQuantity_id");
CREATE INDEX "ix_MatrixQuantity_vector_value_vector_value" ON "MatrixQuantity_vector_value" (vector_value);

CREATE TABLE "Equilibration_simulation_tool" (
	"Equilibration_id" INTEGER,
	simulation_tool VARCHAR(9),
	PRIMARY KEY ("Equilibration_id", simulation_tool),
	FOREIGN KEY("Equilibration_id") REFERENCES "Equilibration" (id)
);
CREATE INDEX "ix_Equilibration_simulation_tool_Equilibration_id" ON "Equilibration_simulation_tool" ("Equilibration_id");
CREATE INDEX "ix_Equilibration_simulation_tool_simulation_tool" ON "Equilibration_simulation_tool" (simulation_tool);

CREATE TABLE "Equilibration_simulation_software" (
	"Equilibration_id" INTEGER,
	simulation_software VARCHAR(10),
	PRIMARY KEY ("Equilibration_id", simulation_software),
	FOREIGN KEY("Equilibration_id") REFERENCES "Equilibration" (id)
);
CREATE INDEX "ix_Equilibration_simulation_software_simulation_software" ON "Equilibration_simulation_software" (simulation_software);
CREATE INDEX "ix_Equilibration_simulation_software_Equilibration_id" ON "Equilibration_simulation_software" ("Equilibration_id");

CREATE TABLE "Production_simulation_tool" (
	"Production_id" INTEGER,
	simulation_tool VARCHAR(9),
	PRIMARY KEY ("Production_id", simulation_tool),
	FOREIGN KEY("Production_id") REFERENCES "Production" (id)
);
CREATE INDEX "ix_Production_simulation_tool_Production_id" ON "Production_simulation_tool" ("Production_id");
CREATE INDEX "ix_Production_simulation_tool_simulation_tool" ON "Production_simulation_tool" (simulation_tool);

CREATE TABLE "Production_simulation_software" (
	"Production_id" INTEGER,
	simulation_software VARCHAR(10),
	PRIMARY KEY ("Production_id", simulation_software),
	FOREIGN KEY("Production_id") REFERENCES "Production" (id)
);
CREATE INDEX "ix_Production_simulation_software_Production_id" ON "Production_simulation_software" ("Production_id");
CREATE INDEX "ix_Production_simulation_software_simulation_software" ON "Production_simulation_software" (simulation_software);

CREATE TABLE "Production_simulation_method" (
	"Production_id" INTEGER,
	simulation_method VARCHAR(43),
	PRIMARY KEY ("Production_id", simulation_method),
	FOREIGN KEY("Production_id") REFERENCES "Production" (id)
);
CREATE INDEX "ix_Production_simulation_method_simulation_method" ON "Production_simulation_method" (simulation_method);
CREATE INDEX "ix_Production_simulation_method_Production_id" ON "Production_simulation_method" ("Production_id");

CREATE TABLE "Analysis_analysis_tool" (
	"Analysis_id" INTEGER,
	analysis_tool VARCHAR(26),
	PRIMARY KEY ("Analysis_id", analysis_tool),
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
);
CREATE INDEX "ix_Analysis_analysis_tool_Analysis_id" ON "Analysis_analysis_tool" ("Analysis_id");
CREATE INDEX "ix_Analysis_analysis_tool_analysis_tool" ON "Analysis_analysis_tool" (analysis_tool);

CREATE TABLE "Analysis_analysis_software" (
	"Analysis_id" INTEGER,
	analysis_software VARCHAR(31),
	PRIMARY KEY ("Analysis_id", analysis_software),
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
);
CREATE INDEX "ix_Analysis_analysis_software_analysis_software" ON "Analysis_analysis_software" (analysis_software);
CREATE INDEX "ix_Analysis_analysis_software_Analysis_id" ON "Analysis_analysis_software" ("Analysis_id");

CREATE TABLE "Analysis_analysis_method" (
	"Analysis_id" INTEGER,
	analysis_method VARCHAR(18),
	PRIMARY KEY ("Analysis_id", analysis_method),
	FOREIGN KEY("Analysis_id") REFERENCES "Analysis" (id)
);
CREATE INDEX "ix_Analysis_analysis_method_Analysis_id" ON "Analysis_analysis_method" ("Analysis_id");
CREATE INDEX "ix_Analysis_analysis_method_analysis_method" ON "Analysis_analysis_method" (analysis_method);

CREATE TABLE "SimulationStages" (
	id INTEGER NOT NULL,
	setup_id INTEGER,
	minimisation_id INTEGER,
	equilibration_id INTEGER,
	production_id INTEGER,
	analysis_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(setup_id) REFERENCES "Setup" (id),
	FOREIGN KEY(minimisation_id) REFERENCES "Minimisation" (id),
	FOREIGN KEY(equilibration_id) REFERENCES "Equilibration" (id),
	FOREIGN KEY(production_id) REFERENCES "Production" (id),
	FOREIGN KEY(analysis_id) REFERENCES "Analysis" (id)
);
CREATE INDEX "ix_SimulationStages_id" ON "SimulationStages" (id);

CREATE TABLE "SimulationSettings" (
	id INTEGER NOT NULL,
	ensemble_id INTEGER,
	integrator_id INTEGER,
	barostat_id INTEGER,
	thermostat_id INTEGER,
	interactions_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(ensemble_id) REFERENCES "Ensemble" (id),
	FOREIGN KEY(integrator_id) REFERENCES "Integrator" (id),
	FOREIGN KEY(barostat_id) REFERENCES "Barostat" (id),
	FOREIGN KEY(thermostat_id) REFERENCES "Thermostat" (id),
	FOREIGN KEY(interactions_id) REFERENCES "Interactions" (id)
);
CREATE INDEX "ix_SimulationSettings_id" ON "SimulationSettings" (id);

CREATE TABLE "SystemComposition" (
	id INTEGER NOT NULL,
	system_counts_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(system_counts_id) REFERENCES "SystemCounts" (id)
);
CREATE INDEX "ix_SystemComposition_id" ON "SystemComposition" (id);

CREATE TABLE "SimulationObservables" (
	id INTEGER NOT NULL,
	simulation_averages_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(simulation_averages_id) REFERENCES "SimulationAverages" (id)
);
CREATE INDEX "ix_SimulationObservables_id" ON "SimulationObservables" (id);

CREATE TABLE "TopologyMetadata" (
	id INTEGER NOT NULL,
	connectivity_id INTEGER,
	particles_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(connectivity_id) REFERENCES "Connectivity" (id),
	FOREIGN KEY(particles_id) REFERENCES "Particles" (id)
);
CREATE INDEX "ix_TopologyMetadata_id" ON "TopologyMetadata" (id);

CREATE TABLE "TrajectoryMetadata" (
	id INTEGER NOT NULL,
	simulation_box_id INTEGER,
	trajectory_output_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(simulation_box_id) REFERENCES "SimulationBox" (id),
	FOREIGN KEY(trajectory_output_id) REFERENCES "Trajectories" (id)
);
CREATE INDEX "ix_TrajectoryMetadata_id" ON "TrajectoryMetadata" (id);

CREATE TABLE "ComputationalEnvironment" (
	id INTEGER NOT NULL,
	hardware_id INTEGER,
	software_id INTEGER,
	performance_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(hardware_id) REFERENCES "Hardware" (id),
	FOREIGN KEY(software_id) REFERENCES "Software" (id),
	FOREIGN KEY(performance_id) REFERENCES "Performance" (id)
);
CREATE INDEX "ix_ComputationalEnvironment_id" ON "ComputationalEnvironment" (id);

CREATE TABLE "Minimisation_minimisation_algorithm" (
	"Minimisation_id" INTEGER,
	minimisation_algorithm VARCHAR(18),
	PRIMARY KEY ("Minimisation_id", minimisation_algorithm),
	FOREIGN KEY("Minimisation_id") REFERENCES "Minimisation" (id)
);
CREATE INDEX "ix_Minimisation_minimisation_algorithm_minimisation_algorithm" ON "Minimisation_minimisation_algorithm" (minimisation_algorithm);
CREATE INDEX "ix_Minimisation_minimisation_algorithm_Minimisation_id" ON "Minimisation_minimisation_algorithm" ("Minimisation_id");

CREATE TABLE "Minimisation_simulation_tool" (
	"Minimisation_id" INTEGER,
	simulation_tool VARCHAR(9),
	PRIMARY KEY ("Minimisation_id", simulation_tool),
	FOREIGN KEY("Minimisation_id") REFERENCES "Minimisation" (id)
);
CREATE INDEX "ix_Minimisation_simulation_tool_Minimisation_id" ON "Minimisation_simulation_tool" ("Minimisation_id");
CREATE INDEX "ix_Minimisation_simulation_tool_simulation_tool" ON "Minimisation_simulation_tool" (simulation_tool);

CREATE TABLE "Minimisation_simulation_software" (
	"Minimisation_id" INTEGER,
	simulation_software VARCHAR(10),
	PRIMARY KEY ("Minimisation_id", simulation_software),
	FOREIGN KEY("Minimisation_id") REFERENCES "Minimisation" (id)
);
CREATE INDEX "ix_Minimisation_simulation_software_Minimisation_id" ON "Minimisation_simulation_software" ("Minimisation_id");
CREATE INDEX "ix_Minimisation_simulation_software_simulation_software" ON "Minimisation_simulation_software" (simulation_software);

CREATE TABLE "SimulationMetadata" (
	id INTEGER NOT NULL,
	stages_id INTEGER,
	settings_id INTEGER,
	observables_id INTEGER,
	topology_id INTEGER,
	trajectory_id INTEGER,
	composition_id INTEGER,
	potentials_id INTEGER,
	compute_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(stages_id) REFERENCES "SimulationStages" (id),
	FOREIGN KEY(settings_id) REFERENCES "SimulationSettings" (id),
	FOREIGN KEY(observables_id) REFERENCES "SimulationObservables" (id),
	FOREIGN KEY(topology_id) REFERENCES "TopologyMetadata" (id),
	FOREIGN KEY(trajectory_id) REFERENCES "TrajectoryMetadata" (id),
	FOREIGN KEY(composition_id) REFERENCES "SystemComposition" (id),
	FOREIGN KEY(potentials_id) REFERENCES "PotentialMetadata" (id),
	FOREIGN KEY(compute_id) REFERENCES "ComputationalEnvironment" (id)
);
CREATE INDEX "ix_SimulationMetadata_id" ON "SimulationMetadata" (id);

CREATE TABLE "MoleculeID" (
	id INTEGER NOT NULL,
	"PDB_ID" TEXT,
	"UNIPROT_ID" TEXT,
	"SMILES" TEXT,
	"InChI" TEXT,
	"InChIKey" TEXT,
	"alphafold_ID" TEXT,
	"PubChem_CID" TEXT,
	protein_sequence TEXT,
	nucleic_sequence TEXT,
	predicted_structure BOOLEAN,
	modified BOOLEAN,
	molecular_formula TEXT,
	molecule_count INTEGER,
	atom_count INTEGER,
	monomer_count INTEGER,
	"SystemComposition_id" INTEGER,
	molecular_weight_id INTEGER,
	molecule_charge_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SystemComposition_id") REFERENCES "SystemComposition" (id),
	FOREIGN KEY(molecular_weight_id) REFERENCES "MassQuantity" (id),
	FOREIGN KEY(molecule_charge_id) REFERENCES "ChargeQuantity" (id)
);
CREATE INDEX "ix_MoleculeID_id" ON "MoleculeID" (id);
