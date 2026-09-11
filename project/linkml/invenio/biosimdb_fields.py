"""Generated from BioSimDB LinkML schema. DO NOT EDIT MANUALLY."""

from marshmallow import Schema, fields
from marshmallow.validate import OneOf
from marshmallow_utils.fields import SanitizedUnicode

COMMUNITY = "BioSimDB"


class LengthQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['Å', 'nm']), allow_none=True)


class VolumeQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['Å³', 'nm³']), allow_none=True)


class TimeQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['s', 'ms', 'μs', 'ns', 'ps', 'fs']), allow_none=True)


class FrequencyQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['1/ps']), allow_none=True)


class FrictionCoefficientQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['a/ps', 'kg/s']), allow_none=True)


class MolarEnergyQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['kcal/mol', 'kJ/mol']), allow_none=True)


class EnergyQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['kWh']), allow_none=True)


class TemperatureQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['K', '°C', '°F']), allow_none=True)


class PressureQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['bar', 'Pa']), allow_none=True)


class CompressibilityQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['1/bar', '1/Pa']), allow_none=True)


class MassQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['g/mol', 'Da']), allow_none=True)


class ConcentrationQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['M']), allow_none=True)


class ForceQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['kJ/mol/nm', 'kcal/mol/Å']), allow_none=True)


class ChargeQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['e', 'C']), allow_none=True)


class AngleQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['degree', 'radian']), allow_none=True)


class ByteQuantitySchema(Schema):
    value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['GB', 'MB']), allow_none=True)


class VectorLengthQuantitySchema(Schema):
    vector_value = fields.List(fields.Float(), allow_none=True)
    value_unit = fields.String(validate=OneOf(['Å', 'nm']), allow_none=True)


class VectorAngleQuantitySchema(Schema):
    vector_value = fields.List(fields.Float(), allow_none=True)
    value_unit = fields.String(validate=OneOf(['degree', 'radian']), allow_none=True)


class VectorVolumeQuantitySchema(Schema):
    vector_value = fields.List(fields.Float(), allow_none=True)
    value_unit = fields.String(validate=OneOf(['Å', 'nm']), allow_none=True)


class VectorCompressibilityQuantitySchema(Schema):
    vector_value = fields.Float(allow_none=True)
    value_unit = fields.String(validate=OneOf(['1/bar', '1/Pa']), allow_none=True)


class VectorPressureQuantitySchema(Schema):
    vector_value = fields.List(fields.Float(), allow_none=True)
    value_unit = fields.String(validate=OneOf(['bar', 'Pa']), allow_none=True)


class VectorTemperatureQuantitySchema(Schema):
    vector_value = fields.List(fields.Float(), allow_none=True)
    value_unit = fields.String(validate=OneOf(['K', '°C', '°F']), allow_none=True)


class VectorTimeQuantitySchema(Schema):
    vector_value = fields.List(fields.Float(), allow_none=True)
    value_unit = fields.String(validate=OneOf(['s', 'ms', 'μs', 'ns', 'ps', 'fs']), allow_none=True)


class MatrixPressureQuantitySchema(Schema):
    vector_value = fields.List(fields.Float(), allow_none=True)
    value_unit = fields.String(validate=OneOf(['bar', 'Pa']), allow_none=True)


class MatrixCompressibilityQuantitySchema(Schema):
    vector_value = fields.List(fields.Float(), allow_none=True)
    value_unit = fields.String(validate=OneOf(['1/bar', '1/Pa']), allow_none=True)


class MatrixQuantitySchema(Schema):
    vector_value = fields.List(fields.Float(), allow_none=True)
    value_unit = SanitizedUnicode(allow_none=True)


class SetupSchema(Schema):
    setup_tool = fields.String(validate=OneOf(['pdb4amber', 'prepareforleap', 'packmol', 'packmol_memgen', 'LEaP', 'antechamber', 'pyMSMT', 'mdgx', 'parmed']), allow_none=True)


class MinimisationSchema(Schema):
    energy_tolerance = fields.Nested(ForceQuantitySchema, allow_none=True)
    number_of_minimisation_steps = fields.Integer(allow_none=True)
    minimisation_distance_step_size = fields.Nested(LengthQuantitySchema, allow_none=True)
    minimisation_algorithm = fields.List(fields.String(validate=OneOf(['Steepest Descent', 'Conjugate Gradient', 'L-BFGS', 'XMIN', 'LMOD', 'None'])), allow_none=True)
    simulation_tool = fields.List(fields.String(validate=OneOf(['sander', 'pmemd', 'gem.pmemd', 'mdrun'])), allow_none=True)
    simulation_software = fields.List(fields.String(validate=OneOf(['Amber', 'GROMACS', 'LAMMPS', 'NAMD', 'OpenMM', 'CHARMM', 'DL_POLY', 'HOOMD-blue', 'Desmond', 'ACEMD', 'CP2K'])), allow_none=True)


class EquilibrationSchema(Schema):
    simulation_tool = fields.List(fields.String(validate=OneOf(['sander', 'pmemd', 'gem.pmemd', 'mdrun'])), allow_none=True)
    simulation_software = fields.List(fields.String(validate=OneOf(['Amber', 'GROMACS', 'LAMMPS', 'NAMD', 'OpenMM', 'CHARMM', 'DL_POLY', 'HOOMD-blue', 'Desmond', 'ACEMD', 'CP2K'])), allow_none=True)


class ProductionSchema(Schema):
    simulation_tool = fields.List(fields.String(validate=OneOf(['sander', 'pmemd', 'gem.pmemd', 'mdrun'])), allow_none=True)
    simulation_software = fields.List(fields.String(validate=OneOf(['Amber', 'GROMACS', 'LAMMPS', 'NAMD', 'OpenMM', 'CHARMM', 'DL_POLY', 'HOOMD-blue', 'Desmond', 'ACEMD', 'CP2K'])), allow_none=True)
    simulation_software_version = SanitizedUnicode(allow_none=True)
    simulation_method = fields.List(fields.String(validate=OneOf(['Self-guided Langevin Dynamics', 'Accelerated Molecular Dynamics', 'Gaussian Accelerated Molecular Dynamics', 'Targeted Molecular Dynamics', 'Nudged Elastic Band Calculations', 'Adaptive String Method', 'LMOD method', 'DL-FIND Optimization', 'Thermodynamic Integration (TI)', 'Linear Interaction Energies (LIE)', 'Replica Exchange Molecular Dynamics (REMD)', 'Adaptively Biased Molecular Dynamics (ABMD)', 'Steered Molecular Dynamics (SMD)', 'Umbrella Sampling', 'Metadynamics', 'Swarms of Trajectories String Method', 'Constant pH Molecular Dynamics', 'Constant Redox Potential Molecular Dynamics', 'Continuous Constant pH Molecular Dynamics', 'NMR Refinement', 'X-ray and CryoEM Refinement', 'Locally Enhanced Sampling'])), allow_none=True)


class AnalysisSchema(Schema):
    analysis_tool = fields.List(fields.String(validate=OneOf(['mdout_analyzer.py', 'ambpdb', 'CPPTRAJ', 'PYTRAJ', 'MMPBSA.py', 'Free Energy Workflow (FEW)', 'edgember', 'SAX-RISM', 'SAX-MD', 'MoFT', 'ndfes', 'PLUMED', 'MDanalysis'])), allow_none=True)
    analysis_software = fields.List(fields.String(validate=OneOf(['Visual Molecular Dynamics (VMD)', 'Schrödinger Maestro', 'PyMOL', 'Avogadro'])), allow_none=True)
    analysis_method = fields.List(fields.String(validate=OneOf(['RMSD', 'DSSP', 'GIST', 'Hydrogen Bonds', 'Connolly surface', 'Radius of Gyration', 'BAR/PBSA'])), allow_none=True)


class SimulationStagesSchema(Schema):
    setup = fields.Nested(SetupSchema, allow_none=True)
    minimisation = fields.Nested(MinimisationSchema, allow_none=True)
    equilibration = fields.Nested(EquilibrationSchema, allow_none=True)
    production = fields.Nested(ProductionSchema, allow_none=True)
    analysis = fields.Nested(AnalysisSchema, allow_none=True)


class EnsembleSchema(Schema):
    ensemble_type = fields.String(validate=OneOf(['NPT', 'NVT', 'NVE', 'μVT']), allow_none=True)
    random_seed = fields.Integer(allow_none=True)


class IntegratorSchema(Schema):
    integrator_algorithm = fields.String(validate=OneOf(['Velocity-Verlet', 'Leap-frog', 'Verlet', 'Euler']), allow_none=True)
    frame_step = fields.Nested(TimeQuantitySchema, allow_none=True)
    time_step = fields.Nested(TimeQuantitySchema, allow_none=True)
    number_of_steps = fields.Integer(allow_none=True)
    simulation_time = fields.Nested(TimeQuantitySchema, allow_none=True)


class BarostatSchema(Schema):
    barostat_algorithm = fields.String(validate=OneOf(['Berendsen', 'Andersen', 'Parrinello-Rahman', 'Nose-Hoover', 'Monte Carlo', 'Martyna-Tuckerman-Tobias-Klein']), allow_none=True)
    compressibility = fields.Nested(CompressibilityQuantitySchema, allow_none=True)
    compressibility_vector = fields.Nested(MatrixCompressibilityQuantitySchema, allow_none=True)
    target_pressure = fields.Nested(PressureQuantitySchema, allow_none=True)
    target_pressure_vector = fields.Nested(MatrixPressureQuantitySchema, allow_none=True)
    pressure_time_constant = fields.Nested(TimeQuantitySchema, allow_none=True)
    pressure_coupling_frequency = fields.Nested(FrequencyQuantitySchema, allow_none=True)
    pressure_coupling_type = fields.String(validate=OneOf(['isotropic', 'semi-isotropic', 'anisotropic', 'surface tension']), allow_none=True)


class ThermostatSchema(Schema):
    thermostat_algorithm = fields.String(validate=OneOf(['Langevin', 'Berendsen', 'Andersen', 'Nose-Hoover', 'Bussi']), allow_none=True)
    target_temperature = fields.Nested(TemperatureQuantitySchema, allow_none=True)
    target_temperature_vector = fields.Nested(VectorTemperatureQuantitySchema, allow_none=True)
    collision_frequency = fields.Nested(FrequencyQuantitySchema, allow_none=True)
    temperature_time_constant = fields.Nested(VectorTimeQuantitySchema, allow_none=True)
    coupling_group = SanitizedUnicode(allow_none=True)
    chain_length = fields.Integer(allow_none=True)
    friction_coefficient = fields.Nested(FrictionCoefficientQuantitySchema, allow_none=True)


class InteractionsSchema(Schema):
    restraints = fields.Boolean(allow_none=True)
    electrostatic_cutoff_distance = fields.Nested(LengthQuantitySchema, allow_none=True)
    vdw_cutoff_distance = fields.Nested(LengthQuantitySchema, allow_none=True)
    bond_length_constraints_algorithm = fields.String(validate=OneOf(['SHAKE', 'RATTLE', 'SETTLE', 'LINCS', 'CCMA']), allow_none=True)
    long_range_interaction_method = fields.String(validate=OneOf(['Cutoff', 'Ewald', 'PME', 'P3M', 'FMM', 'RF']), allow_none=True)


class SimulationSettingsSchema(Schema):
    ensemble = fields.Nested(EnsembleSchema, allow_none=True)
    integrator = fields.Nested(IntegratorSchema, allow_none=True)
    barostat = fields.Nested(BarostatSchema, allow_none=True)
    thermostat = fields.Nested(ThermostatSchema, allow_none=True)
    interactions = fields.Nested(InteractionsSchema, allow_none=True)


class SystemCountsSchema(Schema):
    total_molecule_count = fields.Integer(allow_none=True)
    total_atom_count = fields.Integer(allow_none=True)
    unique_molecule_count = fields.Integer(allow_none=True)
    salt_concentration = fields.Nested(ConcentrationQuantitySchema, allow_none=True)


class MoleculeIDSchema(Schema):
    PDB_ID = SanitizedUnicode(allow_none=True)
    UNIPROT_ID = SanitizedUnicode(allow_none=True)
    SMILES = SanitizedUnicode(allow_none=True)
    InChI = SanitizedUnicode(allow_none=True)
    InChIKey = SanitizedUnicode(allow_none=True)
    alphafold_ID = SanitizedUnicode(allow_none=True)
    PubChem_CID = SanitizedUnicode(allow_none=True)
    protein_sequence = SanitizedUnicode(allow_none=True)
    nucleic_sequence = SanitizedUnicode(allow_none=True)
    predicted_structure = fields.Boolean(allow_none=True)
    modified = fields.Boolean(allow_none=True)
    molecular_formula = SanitizedUnicode(allow_none=True)
    molecular_weight = fields.Nested(MassQuantitySchema, allow_none=True)
    molecule_charge = fields.Nested(ChargeQuantitySchema, allow_none=True)
    molecule_count = fields.Integer(allow_none=True)
    atom_count = fields.Integer(allow_none=True)
    monomer_count = fields.Integer(allow_none=True)
    simulated_particle_names = SanitizedUnicode(allow_none=True)
    simulated_molecule_name = SanitizedUnicode(allow_none=True)


class SystemCompositionSchema(Schema):
    system_counts = fields.Nested(SystemCountsSchema, allow_none=True)
    molecule_ID = fields.List(fields.Nested(MoleculeIDSchema), allow_none=True)


class SimulationAveragesSchema(Schema):
    average_kinetic_energy = fields.Nested(MolarEnergyQuantitySchema, allow_none=True)
    average_potential_energy = fields.Nested(MolarEnergyQuantitySchema, allow_none=True)
    average_enthalpy = fields.Nested(MolarEnergyQuantitySchema, allow_none=True)
    average_pressure = fields.Nested(PressureQuantitySchema, allow_none=True)
    average_temperature = fields.Nested(TemperatureQuantitySchema, allow_none=True)
    average_volume = fields.Nested(VolumeQuantitySchema, allow_none=True)
    average_volume_vector = fields.Nested(VectorVolumeQuantitySchema, allow_none=True)


class SimulationObservablesSchema(Schema):
    simulation_averages = fields.Nested(SimulationAveragesSchema, allow_none=True)


class ConnectivitySchema(Schema):
    bonds = fields.Boolean(allow_none=True)
    dihedrals = fields.Boolean(allow_none=True)


class ParticlesSchema(Schema):
    masses = fields.Boolean(allow_none=True)
    fixed_charges = fields.Boolean(allow_none=True)
    system_charge = fields.Nested(ChargeQuantitySchema, allow_none=True)
    coarse_grained = fields.Boolean(allow_none=True)
    resolution = fields.String(validate=OneOf(['All Atom', 'United Atom', 'Coarse-Grained', 'Mesoscale']), allow_none=True)


class TopologyMetadataSchema(Schema):
    connectivity = fields.Nested(ConnectivitySchema, allow_none=True)
    particles = fields.Nested(ParticlesSchema, allow_none=True)


class SimulationBoxSchema(Schema):
    box_dimensions = fields.Nested(VectorLengthQuantitySchema, allow_none=True)
    box_angles = fields.Nested(VectorAngleQuantitySchema, allow_none=True)
    box_type = fields.String(validate=OneOf(['Cubic', 'Tetragonal', 'Orthorhombic', 'Truncated Octahedron', 'Triclinic']), allow_none=True)
    periodic_boundary_conditions = fields.String(validate=OneOf(['None', 'xyz', 'xy', 'xz', 'yz']), allow_none=True)


class TrajectoriesSchema(Schema):
    positions = fields.Boolean(allow_none=True)
    forces = fields.Boolean(allow_none=True)
    velocities = fields.Boolean(allow_none=True)
    polarizable_charges = fields.Boolean(allow_none=True)
    energies = fields.Boolean(allow_none=True)
    water = fields.Boolean(allow_none=True)
    replica = fields.Boolean(allow_none=True)
    frame_count = fields.Integer(allow_none=True)


class TrajectoryMetadataSchema(Schema):
    simulation_box = fields.Nested(SimulationBoxSchema, allow_none=True)
    trajectory_output = fields.Nested(TrajectoriesSchema, allow_none=True)


class WaterPotentialSchema(Schema):
    water_potential_name = fields.String(validate=OneOf(['OPC', 'OPC3', 'OPC3POL', 'POL3', 'TIP3P', 'TIP3PFB', 'TIP4PFB', 'TIP4P', 'TIP5P', 'TIP4PEW', 'SPCE', 'SPCEB', 'SPC/Fw', 'q-SPC/Fw']), allow_none=True)
    modified = fields.Boolean(allow_none=True)


class ProteinPotentialSchema(Schema):
    protein_potential_name = fields.String(validate=OneOf(['ff19SB', 'ff99SB', 'ff99SB-ILDN', 'ff99SB-disp', 'ff14SB', 'ff14SBonlysc', 'ff15ipq', 'fb15', 'ff03', 'ff03ua', 'phosaa10', 'phosaa14SB', 'phosaa19SB', 'ff14SB_modAA', 'ff19SB_modAA']), allow_none=True)
    modified = fields.Boolean(allow_none=True)


class LipidPotentialSchema(Schema):
    lipid_potential_name = fields.String(validate=OneOf(['LIPID21']), allow_none=True)
    modified = fields.Boolean(allow_none=True)


class NucleicPotentialSchema(Schema):
    nucleic_potential_name = fields.String(validate=OneOf(['ff99-bsc0', 'ff99OL3', 'LJbb', 'ROC', 'Shaw', 'OL15', 'OL21', 'OL24', 'OL3', 'bsc1', 'terminal_monophosphate']), allow_none=True)
    modified = fields.Boolean(allow_none=True)


class CarbohydratePotentialSchema(Schema):
    carbohydrate_potential_name = fields.String(validate=OneOf(['GLYCAM06', 'GLYCAM_06EP', 'GLYCAM_06j-1']), allow_none=True)
    modified = fields.Boolean(allow_none=True)


class PolymerPotentialSchema(Schema):
    polymer_potential_name = fields.String(validate=OneOf(['LignAmb25']), allow_none=True)
    modified = fields.Boolean(allow_none=True)


class GeneralPotentialSchema(Schema):
    general_potential_name = fields.String(validate=OneOf(['gem.pmemd', 'GAFF', 'GAFF2', 'OPLS', 'GROMOS', 'CHARMM']), allow_none=True)
    modified = fields.Boolean(allow_none=True)


class MachineLearnedPotentialSchema(Schema):
    machine_learned_potential_name = fields.String(validate=OneOf(['MACE', 'ANI', 'NequIP', 'UMA', 'AceFF']), allow_none=True)
    modified = fields.Boolean(allow_none=True)


class PotentialMetadataSchema(Schema):
    water_potential = fields.Nested(WaterPotentialSchema, allow_none=True)
    protein_potential = fields.Nested(ProteinPotentialSchema, allow_none=True)
    lipid_potential = fields.Nested(LipidPotentialSchema, allow_none=True)
    nucleic_potential = fields.Nested(NucleicPotentialSchema, allow_none=True)
    carbohydrate_potential = fields.Nested(CarbohydratePotentialSchema, allow_none=True)
    polymer_potential = fields.Nested(PolymerPotentialSchema, allow_none=True)
    general_potential = fields.Nested(GeneralPotentialSchema, allow_none=True)
    machine_learned_potential = fields.Nested(MachineLearnedPotentialSchema, allow_none=True)


class HardwareSchema(Schema):
    execution_platform = fields.String(validate=OneOf(['HPC Cluster', 'Cloud VM', 'Local']), allow_none=True)
    node_type = fields.String(validate=OneOf(['CPU only', 'GPU Accelerated', 'Hybrid CPU GPU']), allow_none=True)
    node_count = fields.Integer(allow_none=True)
    CPU_vendor = fields.String(validate=OneOf(['AMD', 'Intel', 'ARM', 'Other']), allow_none=True)
    CPU_architecture = fields.String(validate=OneOf(['x86', 'ARM']), allow_none=True)
    sockets_per_node = fields.Integer(allow_none=True)
    cores_per_socket = fields.Integer(allow_none=True)
    threads_per_core = fields.Integer(allow_none=True)
    GPU_vendor = fields.String(validate=OneOf(['Nvidia', 'AMD', 'Intel', 'None']), allow_none=True)
    GPUs_per_node = fields.Integer(allow_none=True)
    memory_per_node = fields.Nested(ByteQuantitySchema, allow_none=True)


class SoftwareSchema(Schema):
    operating_system = fields.String(validate=OneOf(['Linux', 'macOS', 'Windows']), allow_none=True)
    scheduler = fields.String(validate=OneOf(['SLURM', 'PBS', 'LSF', 'SGE', 'None']), allow_none=True)
    MPI_library = fields.String(validate=OneOf(['OpenMPI', 'MPICH', 'IntelMPI', 'MVAPICH2', 'None']), allow_none=True)
    container_runtime = fields.String(validate=OneOf(['Apptainer', 'Docker', 'Podman', 'None']), allow_none=True)


class PerformanceSchema(Schema):
    wall_time = fields.Nested(TimeQuantitySchema, allow_none=True)
    energy_consumption = fields.Nested(EnergyQuantitySchema, allow_none=True)


class ComputationalEnvironmentSchema(Schema):
    hardware = fields.Nested(HardwareSchema, allow_none=True)
    software = fields.Nested(SoftwareSchema, allow_none=True)
    performance = fields.Nested(PerformanceSchema, allow_none=True)


class FileMetadataSchema(Schema):
    file_name = SanitizedUnicode(required=True)
    file_size = fields.Nested(ByteQuantitySchema, allow_none=True)
    file_hash = SanitizedUnicode(allow_none=True)
    file_hash_algorithm = fields.String(validate=OneOf(['sha256', 'md5', 'xxh3_64']), allow_none=True)
    file_role = fields.String(validate=OneOf(['topology', 'trajectory', 'metadata', 'log', 'parameter', 'other']), allow_none=True)


class SimulationMetadataSchema(Schema):
    stages = fields.Nested(SimulationStagesSchema, allow_none=True)
    settings = fields.Nested(SimulationSettingsSchema, allow_none=True)
    observables = fields.Nested(SimulationObservablesSchema, allow_none=True)
    topology = fields.Nested(TopologyMetadataSchema, allow_none=True)
    trajectory = fields.Nested(TrajectoryMetadataSchema, allow_none=True)
    composition = fields.Nested(SystemCompositionSchema, allow_none=True)
    potentials = fields.Nested(PotentialMetadataSchema, allow_none=True)
    compute = fields.Nested(ComputationalEnvironmentSchema, allow_none=True)
    files = fields.List(fields.Nested(FileMetadataSchema), allow_none=True)
    biosim_schema_version = SanitizedUnicode(allow_none=True)


FIELDS = {
    "stages": fields.Nested(SimulationStagesSchema, allow_none=True),
    "settings": fields.Nested(SimulationSettingsSchema, allow_none=True),
    "observables": fields.Nested(SimulationObservablesSchema, allow_none=True),
    "topology": fields.Nested(TopologyMetadataSchema, allow_none=True),
    "trajectory": fields.Nested(TrajectoryMetadataSchema, allow_none=True),
    "composition": fields.Nested(SystemCompositionSchema, allow_none=True),
    "potentials": fields.Nested(PotentialMetadataSchema, allow_none=True),
    "compute": fields.Nested(ComputationalEnvironmentSchema, allow_none=True),
    "files": fields.Nested(FileMetadataSchema, allow_none=True),
    "biosim_schema_version": SanitizedUnicode(allow_none=True),
}

MAPPING = {
    "stages": {
        "type": "object",
        "properties": {
            "setup": {
                "type": "object",
                "properties": {
                    "setup_tool": {
                        "type": "keyword"
                    }
                }
            },
            "minimisation": {
                "type": "object",
                "properties": {
                    "energy_tolerance": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "number_of_minimisation_steps": {
                        "type": "integer"
                    },
                    "minimisation_distance_step_size": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "minimisation_algorithm": {
                        "type": "keyword"
                    },
                    "simulation_tool": {
                        "type": "keyword"
                    },
                    "simulation_software": {
                        "type": "keyword"
                    }
                }
            },
            "equilibration": {
                "type": "object",
                "properties": {
                    "simulation_tool": {
                        "type": "keyword"
                    },
                    "simulation_software": {
                        "type": "keyword"
                    }
                }
            },
            "production": {
                "type": "object",
                "properties": {
                    "simulation_tool": {
                        "type": "keyword"
                    },
                    "simulation_software": {
                        "type": "keyword"
                    },
                    "simulation_software_version": {
                        "type": "text"
                    },
                    "simulation_method": {
                        "type": "keyword"
                    }
                }
            },
            "analysis": {
                "type": "object",
                "properties": {
                    "analysis_tool": {
                        "type": "keyword"
                    },
                    "analysis_software": {
                        "type": "keyword"
                    },
                    "analysis_method": {
                        "type": "keyword"
                    }
                }
            }
        }
    },
    "settings": {
        "type": "object",
        "properties": {
            "ensemble": {
                "type": "object",
                "properties": {
                    "ensemble_type": {
                        "type": "keyword"
                    },
                    "random_seed": {
                        "type": "integer"
                    }
                }
            },
            "integrator": {
                "type": "object",
                "properties": {
                    "integrator_algorithm": {
                        "type": "keyword"
                    },
                    "frame_step": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "time_step": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "number_of_steps": {
                        "type": "integer"
                    },
                    "simulation_time": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    }
                }
            },
            "barostat": {
                "type": "object",
                "properties": {
                    "barostat_algorithm": {
                        "type": "keyword"
                    },
                    "compressibility": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "compressibility_vector": {
                        "type": "object",
                        "properties": {
                            "vector_value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "target_pressure": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "target_pressure_vector": {
                        "type": "object",
                        "properties": {
                            "vector_value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "pressure_time_constant": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "pressure_coupling_frequency": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "pressure_coupling_type": {
                        "type": "keyword"
                    }
                }
            },
            "thermostat": {
                "type": "object",
                "properties": {
                    "thermostat_algorithm": {
                        "type": "keyword"
                    },
                    "target_temperature": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "target_temperature_vector": {
                        "type": "object",
                        "properties": {
                            "vector_value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "collision_frequency": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "temperature_time_constant": {
                        "type": "object",
                        "properties": {
                            "vector_value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "coupling_group": {
                        "type": "text"
                    },
                    "chain_length": {
                        "type": "integer"
                    },
                    "friction_coefficient": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    }
                }
            },
            "interactions": {
                "type": "object",
                "properties": {
                    "restraints": {
                        "type": "boolean"
                    },
                    "electrostatic_cutoff_distance": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "vdw_cutoff_distance": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "bond_length_constraints_algorithm": {
                        "type": "keyword"
                    },
                    "long_range_interaction_method": {
                        "type": "keyword"
                    }
                }
            }
        }
    },
    "observables": {
        "type": "object",
        "properties": {
            "simulation_averages": {
                "type": "object",
                "properties": {
                    "average_kinetic_energy": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "average_potential_energy": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "average_enthalpy": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "average_pressure": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "average_temperature": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "average_volume": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "average_volume_vector": {
                        "type": "object",
                        "properties": {
                            "vector_value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    }
                }
            }
        }
    },
    "topology": {
        "type": "object",
        "properties": {
            "connectivity": {
                "type": "object",
                "properties": {
                    "bonds": {
                        "type": "boolean"
                    },
                    "dihedrals": {
                        "type": "boolean"
                    }
                }
            },
            "particles": {
                "type": "object",
                "properties": {
                    "masses": {
                        "type": "boolean"
                    },
                    "fixed_charges": {
                        "type": "boolean"
                    },
                    "system_charge": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "coarse_grained": {
                        "type": "boolean"
                    },
                    "resolution": {
                        "type": "keyword"
                    }
                }
            }
        }
    },
    "trajectory": {
        "type": "object",
        "properties": {
            "simulation_box": {
                "type": "object",
                "properties": {
                    "box_dimensions": {
                        "type": "object",
                        "properties": {
                            "vector_value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "box_angles": {
                        "type": "object",
                        "properties": {
                            "vector_value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "box_type": {
                        "type": "keyword"
                    },
                    "periodic_boundary_conditions": {
                        "type": "keyword"
                    }
                }
            },
            "trajectory_output": {
                "type": "object",
                "properties": {
                    "positions": {
                        "type": "boolean"
                    },
                    "forces": {
                        "type": "boolean"
                    },
                    "velocities": {
                        "type": "boolean"
                    },
                    "polarizable_charges": {
                        "type": "boolean"
                    },
                    "energies": {
                        "type": "boolean"
                    },
                    "water": {
                        "type": "boolean"
                    },
                    "replica": {
                        "type": "boolean"
                    },
                    "frame_count": {
                        "type": "integer"
                    }
                }
            }
        }
    },
    "composition": {
        "type": "object",
        "properties": {
            "system_counts": {
                "type": "object",
                "properties": {
                    "total_molecule_count": {
                        "type": "integer"
                    },
                    "total_atom_count": {
                        "type": "integer"
                    },
                    "unique_molecule_count": {
                        "type": "integer"
                    },
                    "salt_concentration": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    }
                }
            },
            "molecule_ID": {
                "type": "object",
                "properties": {
                    "PDB_ID": {
                        "type": "text"
                    },
                    "UNIPROT_ID": {
                        "type": "text"
                    },
                    "SMILES": {
                        "type": "text"
                    },
                    "InChI": {
                        "type": "text"
                    },
                    "InChIKey": {
                        "type": "text"
                    },
                    "alphafold_ID": {
                        "type": "text"
                    },
                    "PubChem_CID": {
                        "type": "text"
                    },
                    "protein_sequence": {
                        "type": "text"
                    },
                    "nucleic_sequence": {
                        "type": "text"
                    },
                    "predicted_structure": {
                        "type": "boolean"
                    },
                    "modified": {
                        "type": "boolean"
                    },
                    "molecular_formula": {
                        "type": "text"
                    },
                    "molecular_weight": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "molecule_charge": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "molecule_count": {
                        "type": "integer"
                    },
                    "atom_count": {
                        "type": "integer"
                    },
                    "monomer_count": {
                        "type": "integer"
                    },
                    "simulated_particle_names": {
                        "type": "text"
                    },
                    "simulated_molecule_name": {
                        "type": "text"
                    }
                }
            }
        }
    },
    "potentials": {
        "type": "object",
        "properties": {
            "water_potential": {
                "type": "object",
                "properties": {
                    "water_potential_name": {
                        "type": "keyword"
                    },
                    "modified": {
                        "type": "boolean"
                    }
                }
            },
            "protein_potential": {
                "type": "object",
                "properties": {
                    "protein_potential_name": {
                        "type": "keyword"
                    },
                    "modified": {
                        "type": "boolean"
                    }
                }
            },
            "lipid_potential": {
                "type": "object",
                "properties": {
                    "lipid_potential_name": {
                        "type": "keyword"
                    },
                    "modified": {
                        "type": "boolean"
                    }
                }
            },
            "nucleic_potential": {
                "type": "object",
                "properties": {
                    "nucleic_potential_name": {
                        "type": "keyword"
                    },
                    "modified": {
                        "type": "boolean"
                    }
                }
            },
            "carbohydrate_potential": {
                "type": "object",
                "properties": {
                    "carbohydrate_potential_name": {
                        "type": "keyword"
                    },
                    "modified": {
                        "type": "boolean"
                    }
                }
            },
            "polymer_potential": {
                "type": "object",
                "properties": {
                    "polymer_potential_name": {
                        "type": "keyword"
                    },
                    "modified": {
                        "type": "boolean"
                    }
                }
            },
            "general_potential": {
                "type": "object",
                "properties": {
                    "general_potential_name": {
                        "type": "keyword"
                    },
                    "modified": {
                        "type": "boolean"
                    }
                }
            },
            "machine_learned_potential": {
                "type": "object",
                "properties": {
                    "machine_learned_potential_name": {
                        "type": "keyword"
                    },
                    "modified": {
                        "type": "boolean"
                    }
                }
            }
        }
    },
    "compute": {
        "type": "object",
        "properties": {
            "hardware": {
                "type": "object",
                "properties": {
                    "execution_platform": {
                        "type": "keyword"
                    },
                    "node_type": {
                        "type": "keyword"
                    },
                    "node_count": {
                        "type": "integer"
                    },
                    "CPU_vendor": {
                        "type": "keyword"
                    },
                    "CPU_architecture": {
                        "type": "keyword"
                    },
                    "sockets_per_node": {
                        "type": "integer"
                    },
                    "cores_per_socket": {
                        "type": "integer"
                    },
                    "threads_per_core": {
                        "type": "integer"
                    },
                    "GPU_vendor": {
                        "type": "keyword"
                    },
                    "GPUs_per_node": {
                        "type": "integer"
                    },
                    "memory_per_node": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    }
                }
            },
            "software": {
                "type": "object",
                "properties": {
                    "operating_system": {
                        "type": "keyword"
                    },
                    "scheduler": {
                        "type": "keyword"
                    },
                    "MPI_library": {
                        "type": "keyword"
                    },
                    "container_runtime": {
                        "type": "keyword"
                    }
                }
            },
            "performance": {
                "type": "object",
                "properties": {
                    "wall_time": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    },
                    "energy_consumption": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "double"
                            },
                            "value_unit": {
                                "type": "keyword"
                            }
                        }
                    }
                }
            }
        }
    },
    "files": {
        "type": "object",
        "properties": {
            "file_name": {
                "type": "text"
            },
            "file_size": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "double"
                    },
                    "value_unit": {
                        "type": "keyword"
                    }
                }
            },
            "file_hash": {
                "type": "text"
            },
            "file_hash_algorithm": {
                "type": "keyword"
            },
            "file_role": {
                "type": "keyword"
            }
        }
    },
    "biosim_schema_version": {
        "type": "text"
    }
}
