# Auto generated from biosim_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-01T09:33:41
# Schema: biosim-schema
#
# id: https://CCPBioSim.ac.uk/biosim-schema/
# description: Schema for Biomolecular Simulation Data
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.11.0"
version = "0.0.3"

# Namespaces
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
BIOSIM_SCHEMA = CurieNamespace('biosim_schema', 'https://CCPBioSim.ac.uk/biosim-schema/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PDB = CurieNamespace('pdb', 'https://identifiers.org/pdb')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
UNIPROT = CurieNamespace('uniprot', 'https://identifiers.org/uniprot')
DEFAULT_ = BIOSIM_SCHEMA


# Types

# Class references



@dataclass(repr=False)
class SimulationMetadata(YAMLRoot):
    """
    root class for biosim-schema
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["SimulationMetadata"]
    class_class_curie: ClassVar[str] = "biosim_schema:SimulationMetadata"
    class_name: ClassVar[str] = "SimulationMetadata"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.SimulationMetadata

    stages: Optional[Union[dict, "SimulationStages"]] = None
    settings: Optional[Union[dict, "SimulationSettings"]] = None
    observables: Optional[Union[dict, "SimulationObservables"]] = None
    topology: Optional[Union[dict, "TopologyMetadata"]] = None
    trajectory: Optional[Union[dict, "TrajectoryMetadata"]] = None
    composition: Optional[Union[dict, "SystemComposition"]] = None
    potentials: Optional[Union[dict, "PotentialMetadata"]] = None
    compute: Optional[Union[dict, "ComputationalEnvironment"]] = None
    files: Optional[Union[Union[dict, "FileMetadata"], list[Union[dict, "FileMetadata"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.stages is not None and not isinstance(self.stages, SimulationStages):
            self.stages = SimulationStages(**as_dict(self.stages))

        if self.settings is not None and not isinstance(self.settings, SimulationSettings):
            self.settings = SimulationSettings(**as_dict(self.settings))

        if self.observables is not None and not isinstance(self.observables, SimulationObservables):
            self.observables = SimulationObservables(**as_dict(self.observables))

        if self.topology is not None and not isinstance(self.topology, TopologyMetadata):
            self.topology = TopologyMetadata(**as_dict(self.topology))

        if self.trajectory is not None and not isinstance(self.trajectory, TrajectoryMetadata):
            self.trajectory = TrajectoryMetadata(**as_dict(self.trajectory))

        if self.composition is not None and not isinstance(self.composition, SystemComposition):
            self.composition = SystemComposition(**as_dict(self.composition))

        if self.potentials is not None and not isinstance(self.potentials, PotentialMetadata):
            self.potentials = PotentialMetadata(**as_dict(self.potentials))

        if self.compute is not None and not isinstance(self.compute, ComputationalEnvironment):
            self.compute = ComputationalEnvironment(**as_dict(self.compute))

        self._normalize_inlined_as_list(slot_name="files", slot_type=FileMetadata, key_name="file_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LengthQuantity(YAMLRoot):
    """
    A quantity representing length.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/LengthQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/LengthQuantity"
    class_name: ClassVar[str] = "LengthQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.LengthQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "LengthUnit"]] = 'nm'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, LengthUnit):
            self.value_unit = LengthUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VolumeQuantity(YAMLRoot):
    """
    A quantity representing volume.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/VolumeQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/VolumeQuantity"
    class_name: ClassVar[str] = "VolumeQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.VolumeQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "VolumeUnit"]] = 'nm³'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, VolumeUnit):
            self.value_unit = VolumeUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimeQuantity(YAMLRoot):
    """
    A quantity representing time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/TimeQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/TimeQuantity"
    class_name: ClassVar[str] = "TimeQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.TimeQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "TimeUnit"]] = 's'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, TimeUnit):
            self.value_unit = TimeUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FrequencyQuantity(YAMLRoot):
    """
    A quantity representing frequency.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/FrequencyQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/FrequencyQuantity"
    class_name: ClassVar[str] = "FrequencyQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.FrequencyQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "FrequencyUnit"]] = '1/ps'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, FrequencyUnit):
            self.value_unit = FrequencyUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FrictionCoefficientQuantity(YAMLRoot):
    """
    A quantity representing friction coefficients.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/FrictionCoefficientQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/FrictionCoefficientQuantity"
    class_name: ClassVar[str] = "FrictionCoefficientQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.FrictionCoefficientQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "FrictionCoefficientUnit"]] = 'a/ps'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, FrictionCoefficientUnit):
            self.value_unit = FrictionCoefficientUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolarEnergyQuantity(YAMLRoot):
    """
    A quantity representing molar energy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/MolarEnergyQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/MolarEnergyQuantity"
    class_name: ClassVar[str] = "MolarEnergyQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.MolarEnergyQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "MolarEnergyUnit"]] = 'kJ/mol'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, MolarEnergyUnit):
            self.value_unit = MolarEnergyUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnergyQuantity(YAMLRoot):
    """
    A quantity representing energy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/EnergyQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/EnergyQuantity"
    class_name: ClassVar[str] = "EnergyQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.EnergyQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "EnergyUnit"]] = 'kWh'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, EnergyUnit):
            self.value_unit = EnergyUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemperatureQuantity(YAMLRoot):
    """
    A quantity representing temperature.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/TemperatureQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/TemperatureQuantity"
    class_name: ClassVar[str] = "TemperatureQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.TemperatureQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "TemperatureUnit"]] = 'K'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, TemperatureUnit):
            self.value_unit = TemperatureUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PressureQuantity(YAMLRoot):
    """
    A quantity representing pressure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/PressureQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/PressureQuantity"
    class_name: ClassVar[str] = "PressureQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.PressureQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "PressureUnit"]] = 'bar'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, PressureUnit):
            self.value_unit = PressureUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompressibilityQuantity(YAMLRoot):
    """
    A quantity representing compressibility.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/CompressibilityQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/CompressibilityQuantity"
    class_name: ClassVar[str] = "CompressibilityQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.CompressibilityQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "CompressibilityUnit"]] = '1/bar'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, CompressibilityUnit):
            self.value_unit = CompressibilityUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassQuantity(YAMLRoot):
    """
    A quantity representing mass.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/MassQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/MassQuantity"
    class_name: ClassVar[str] = "MassQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.MassQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "MassUnit"]] = 'g/mol'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, MassUnit):
            self.value_unit = MassUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConcentrationQuantity(YAMLRoot):
    """
    A quantity representing concentration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/ConcentrationQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/ConcentrationQuantity"
    class_name: ClassVar[str] = "ConcentrationQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.ConcentrationQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "ConcentrationUnit"]] = 'M'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, ConcentrationUnit):
            self.value_unit = ConcentrationUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ForceQuantity(YAMLRoot):
    """
    A quantity representing force.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/ForceQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/ForceQuantity"
    class_name: ClassVar[str] = "ForceQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.ForceQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "ForceUnit"]] = 'kJ/mol/nm'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, ForceUnit):
            self.value_unit = ForceUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChargeQuantity(YAMLRoot):
    """
    A quantity representing charge.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/ChargeQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/ChargeQuantity"
    class_name: ClassVar[str] = "ChargeQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.ChargeQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "ChargeUnit"]] = 'e'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, ChargeUnit):
            self.value_unit = ChargeUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AngleQuantity(YAMLRoot):
    """
    A quantity representing angles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/AngleQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/AngleQuantity"
    class_name: ClassVar[str] = "AngleQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.AngleQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "AngleUnit"]] = 'degree'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, AngleUnit):
            self.value_unit = AngleUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ByteQuantity(YAMLRoot):
    """
    A quantity representing bytes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/ByteQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/ByteQuantity"
    class_name: ClassVar[str] = "ByteQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.ByteQuantity

    value: Optional[float] = None
    value_unit: Optional[Union[str, "ByteUnit"]] = 'GB'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.value_unit is not None and not isinstance(self.value_unit, ByteUnit):
            self.value_unit = ByteUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VectorLengthQuantity(YAMLRoot):
    """
    A quantity representing 3D lengths/dimensions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/VectorLengthQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/VectorLengthQuantity"
    class_name: ClassVar[str] = "VectorLengthQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.VectorLengthQuantity

    vector_value: Optional[Union[float, list[float]]] = empty_list()
    value_unit: Optional[Union[str, "LengthUnit"]] = 'nm'

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vector_value, list):
            self.vector_value = [self.vector_value] if self.vector_value is not None else []
        self.vector_value = [v if isinstance(v, float) else float(v) for v in self.vector_value]

        if self.value_unit is not None and not isinstance(self.value_unit, LengthUnit):
            self.value_unit = LengthUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VectorAngleQuantity(YAMLRoot):
    """
    A quantity representing 3D angles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/VectorAngleQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/VectorAngleQuantity"
    class_name: ClassVar[str] = "VectorAngleQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.VectorAngleQuantity

    vector_value: Optional[Union[float, list[float]]] = empty_list()
    value_unit: Optional[Union[str, "AngleUnit"]] = 'degree'

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vector_value, list):
            self.vector_value = [self.vector_value] if self.vector_value is not None else []
        self.vector_value = [v if isinstance(v, float) else float(v) for v in self.vector_value]

        if self.value_unit is not None and not isinstance(self.value_unit, AngleUnit):
            self.value_unit = AngleUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VectorVolumeQuantity(YAMLRoot):
    """
    A quantity representing volume as via 3 length dimensions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/VectorVolumeQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/VectorVolumeQuantity"
    class_name: ClassVar[str] = "VectorVolumeQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.VectorVolumeQuantity

    vector_value: Optional[Union[float, list[float]]] = empty_list()
    value_unit: Optional[Union[str, "LengthUnit"]] = 'nm'

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vector_value, list):
            self.vector_value = [self.vector_value] if self.vector_value is not None else []
        self.vector_value = [v if isinstance(v, float) else float(v) for v in self.vector_value]

        if self.value_unit is not None and not isinstance(self.value_unit, LengthUnit):
            self.value_unit = LengthUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VectorCompressibilityQuantity(YAMLRoot):
    """
    A quantity representing compressibility in 3D.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/VectorCompressibilityQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/VectorCompressibilityQuantity"
    class_name: ClassVar[str] = "VectorCompressibilityQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.VectorCompressibilityQuantity

    vector_value: Optional[float] = None
    value_unit: Optional[Union[str, "CompressibilityUnit"]] = '1/bar'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.vector_value is not None and not isinstance(self.vector_value, float):
            self.vector_value = float(self.vector_value)

        if self.value_unit is not None and not isinstance(self.value_unit, CompressibilityUnit):
            self.value_unit = CompressibilityUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VectorPressureQuantity(YAMLRoot):
    """
    A quantity representing pressure in 3D.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/VectorPressureQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/VectorPressureQuantity"
    class_name: ClassVar[str] = "VectorPressureQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.VectorPressureQuantity

    vector_value: Optional[Union[float, list[float]]] = empty_list()
    value_unit: Optional[Union[str, "PressureUnit"]] = 'bar'

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vector_value, list):
            self.vector_value = [self.vector_value] if self.vector_value is not None else []
        self.vector_value = [v if isinstance(v, float) else float(v) for v in self.vector_value]

        if self.value_unit is not None and not isinstance(self.value_unit, PressureUnit):
            self.value_unit = PressureUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VectorTemperatureQuantity(YAMLRoot):
    """
    Temperature values for multiple coupling groups.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/VectorTemperatureQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/VectorTemperatureQuantity"
    class_name: ClassVar[str] = "VectorTemperatureQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.VectorTemperatureQuantity

    vector_value: Optional[Union[float, list[float]]] = empty_list()
    value_unit: Optional[Union[str, "TemperatureUnit"]] = 'K'

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vector_value, list):
            self.vector_value = [self.vector_value] if self.vector_value is not None else []
        self.vector_value = [v if isinstance(v, float) else float(v) for v in self.vector_value]

        if self.value_unit is not None and not isinstance(self.value_unit, TemperatureUnit):
            self.value_unit = TemperatureUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VectorTimeQuantity(YAMLRoot):
    """
    Time values for multiple coupling groups.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/VectorTimeQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/VectorTimeQuantity"
    class_name: ClassVar[str] = "VectorTimeQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.VectorTimeQuantity

    vector_value: Optional[Union[float, list[float]]] = empty_list()
    value_unit: Optional[Union[str, "TimeUnit"]] = 's'

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vector_value, list):
            self.vector_value = [self.vector_value] if self.vector_value is not None else []
        self.vector_value = [v if isinstance(v, float) else float(v) for v in self.vector_value]

        if self.value_unit is not None and not isinstance(self.value_unit, TimeUnit):
            self.value_unit = TimeUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MatrixPressureQuantity(YAMLRoot):
    """
    A quantity representing pressure vectors in 3D.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/MatrixPressureQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/MatrixPressureQuantity"
    class_name: ClassVar[str] = "MatrixPressureQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.MatrixPressureQuantity

    vector_value: Optional[Union[float, list[float]]] = empty_list()
    value_unit: Optional[Union[str, "PressureUnit"]] = 'bar'

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vector_value, list):
            self.vector_value = [self.vector_value] if self.vector_value is not None else []
        self.vector_value = [v if isinstance(v, float) else float(v) for v in self.vector_value]

        if self.value_unit is not None and not isinstance(self.value_unit, PressureUnit):
            self.value_unit = PressureUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MatrixCompressibilityQuantity(YAMLRoot):
    """
    A quantity representing compressibility vectors in 3D.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/MatrixCompressibilityQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/MatrixCompressibilityQuantity"
    class_name: ClassVar[str] = "MatrixCompressibilityQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.MatrixCompressibilityQuantity

    vector_value: Optional[Union[float, list[float]]] = empty_list()
    value_unit: Optional[Union[str, "CompressibilityUnit"]] = '1/bar'

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vector_value, list):
            self.vector_value = [self.vector_value] if self.vector_value is not None else []
        self.vector_value = [v if isinstance(v, float) else float(v) for v in self.vector_value]

        if self.value_unit is not None and not isinstance(self.value_unit, CompressibilityUnit):
            self.value_unit = CompressibilityUnit(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MatrixQuantity(YAMLRoot):
    """
    A quantity representing general vectors in 3D.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["quantities/MatrixQuantity"]
    class_class_curie: ClassVar[str] = "biosim_schema:quantities/MatrixQuantity"
    class_name: ClassVar[str] = "MatrixQuantity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.MatrixQuantity

    vector_value: Optional[Union[float, list[float]]] = empty_list()
    value_unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.vector_value, list):
            self.vector_value = [self.vector_value] if self.vector_value is not None else []
        self.vector_value = [v if isinstance(v, float) else float(v) for v in self.vector_value]

        if self.value_unit is not None and not isinstance(self.value_unit, str):
            self.value_unit = str(self.value_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SimulationStages(YAMLRoot):
    """
    Stages of simulation workflow.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["stages/SimulationStages"]
    class_class_curie: ClassVar[str] = "biosim_schema:stages/SimulationStages"
    class_name: ClassVar[str] = "SimulationStages"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.SimulationStages

    setup: Optional[Union[dict, "Setup"]] = None
    minimisation: Optional[Union[dict, "Minimisation"]] = None
    equilibration: Optional[Union[dict, "Equilibration"]] = None
    production: Optional[Union[dict, "Production"]] = None
    analysis: Optional[Union[dict, "Analysis"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.setup is not None and not isinstance(self.setup, Setup):
            self.setup = Setup(**as_dict(self.setup))

        if self.minimisation is not None and not isinstance(self.minimisation, Minimisation):
            self.minimisation = Minimisation(**as_dict(self.minimisation))

        if self.equilibration is not None and not isinstance(self.equilibration, Equilibration):
            self.equilibration = Equilibration(**as_dict(self.equilibration))

        if self.production is not None and not isinstance(self.production, Production):
            self.production = Production(**as_dict(self.production))

        if self.analysis is not None and not isinstance(self.analysis, Analysis):
            self.analysis = Analysis(**as_dict(self.analysis))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Setup(YAMLRoot):
    """
    Setup stage of simulation workflow.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["stages/Setup"]
    class_class_curie: ClassVar[str] = "biosim_schema:stages/Setup"
    class_name: ClassVar[str] = "Setup"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Setup

    setup_tool: Optional[Union[str, "SetupTool"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.setup_tool is not None and not isinstance(self.setup_tool, SetupTool):
            self.setup_tool = SetupTool(self.setup_tool)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Minimisation(YAMLRoot):
    """
    Minimisation stage of simulation workflow.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["stages/Minimisation"]
    class_class_curie: ClassVar[str] = "biosim_schema:stages/Minimisation"
    class_name: ClassVar[str] = "Minimisation"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Minimisation

    energy_tolerance: Optional[Union[dict, ForceQuantity]] = None
    number_of_minimisation_steps: Optional[int] = None
    minimisation_distance_step_size: Optional[Union[dict, LengthQuantity]] = None
    minimisation_algorithm: Optional[Union[Union[str, "MinimisationAlgorithm"], list[Union[str, "MinimisationAlgorithm"]]]] = empty_list()
    simulation_tool: Optional[Union[Union[str, "SimulationTool"], list[Union[str, "SimulationTool"]]]] = empty_list()
    simulation_software: Optional[Union[Union[str, "SimulationSoftware"], list[Union[str, "SimulationSoftware"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.energy_tolerance is not None and not isinstance(self.energy_tolerance, ForceQuantity):
            self.energy_tolerance = ForceQuantity(**as_dict(self.energy_tolerance))

        if self.number_of_minimisation_steps is not None and not isinstance(self.number_of_minimisation_steps, int):
            self.number_of_minimisation_steps = int(self.number_of_minimisation_steps)

        if self.minimisation_distance_step_size is not None and not isinstance(self.minimisation_distance_step_size, LengthQuantity):
            self.minimisation_distance_step_size = LengthQuantity(**as_dict(self.minimisation_distance_step_size))

        if not isinstance(self.minimisation_algorithm, list):
            self.minimisation_algorithm = [self.minimisation_algorithm] if self.minimisation_algorithm is not None else []
        self.minimisation_algorithm = [v if isinstance(v, MinimisationAlgorithm) else MinimisationAlgorithm(v) for v in self.minimisation_algorithm]

        if not isinstance(self.simulation_tool, list):
            self.simulation_tool = [self.simulation_tool] if self.simulation_tool is not None else []
        self.simulation_tool = [v if isinstance(v, SimulationTool) else SimulationTool(v) for v in self.simulation_tool]

        if not isinstance(self.simulation_software, list):
            self.simulation_software = [self.simulation_software] if self.simulation_software is not None else []
        self.simulation_software = [v if isinstance(v, SimulationSoftware) else SimulationSoftware(v) for v in self.simulation_software]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Equilibration(YAMLRoot):
    """
    Equilibration stage of simulation workflow.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["stages/Equilibration"]
    class_class_curie: ClassVar[str] = "biosim_schema:stages/Equilibration"
    class_name: ClassVar[str] = "Equilibration"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Equilibration

    simulation_tool: Optional[Union[Union[str, "SimulationTool"], list[Union[str, "SimulationTool"]]]] = empty_list()
    simulation_software: Optional[Union[Union[str, "SimulationSoftware"], list[Union[str, "SimulationSoftware"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.simulation_tool, list):
            self.simulation_tool = [self.simulation_tool] if self.simulation_tool is not None else []
        self.simulation_tool = [v if isinstance(v, SimulationTool) else SimulationTool(v) for v in self.simulation_tool]

        if not isinstance(self.simulation_software, list):
            self.simulation_software = [self.simulation_software] if self.simulation_software is not None else []
        self.simulation_software = [v if isinstance(v, SimulationSoftware) else SimulationSoftware(v) for v in self.simulation_software]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Production(YAMLRoot):
    """
    Production stage of simulation workflow.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["stages/Production"]
    class_class_curie: ClassVar[str] = "biosim_schema:stages/Production"
    class_name: ClassVar[str] = "Production"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Production

    simulation_tool: Optional[Union[Union[str, "SimulationTool"], list[Union[str, "SimulationTool"]]]] = empty_list()
    simulation_software: Optional[Union[Union[str, "SimulationSoftware"], list[Union[str, "SimulationSoftware"]]]] = empty_list()
    simulation_software_version: Optional[str] = None
    simulation_method: Optional[Union[Union[str, "SimulationMethod"], list[Union[str, "SimulationMethod"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.simulation_tool, list):
            self.simulation_tool = [self.simulation_tool] if self.simulation_tool is not None else []
        self.simulation_tool = [v if isinstance(v, SimulationTool) else SimulationTool(v) for v in self.simulation_tool]

        if not isinstance(self.simulation_software, list):
            self.simulation_software = [self.simulation_software] if self.simulation_software is not None else []
        self.simulation_software = [v if isinstance(v, SimulationSoftware) else SimulationSoftware(v) for v in self.simulation_software]

        if self.simulation_software_version is not None and not isinstance(self.simulation_software_version, str):
            self.simulation_software_version = str(self.simulation_software_version)

        if not isinstance(self.simulation_method, list):
            self.simulation_method = [self.simulation_method] if self.simulation_method is not None else []
        self.simulation_method = [v if isinstance(v, SimulationMethod) else SimulationMethod(v) for v in self.simulation_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Analysis(YAMLRoot):
    """
    Analysis stage of simulation workflow.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["stages/Analysis"]
    class_class_curie: ClassVar[str] = "biosim_schema:stages/Analysis"
    class_name: ClassVar[str] = "Analysis"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Analysis

    analysis_tool: Optional[Union[Union[str, "AnalysisTool"], list[Union[str, "AnalysisTool"]]]] = empty_list()
    analysis_software: Optional[Union[Union[str, "AnalysisSoftware"], list[Union[str, "AnalysisSoftware"]]]] = empty_list()
    analysis_method: Optional[Union[Union[str, "AnalysisMethod"], list[Union[str, "AnalysisMethod"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.analysis_tool, list):
            self.analysis_tool = [self.analysis_tool] if self.analysis_tool is not None else []
        self.analysis_tool = [v if isinstance(v, AnalysisTool) else AnalysisTool(v) for v in self.analysis_tool]

        if not isinstance(self.analysis_software, list):
            self.analysis_software = [self.analysis_software] if self.analysis_software is not None else []
        self.analysis_software = [v if isinstance(v, AnalysisSoftware) else AnalysisSoftware(v) for v in self.analysis_software]

        if not isinstance(self.analysis_method, list):
            self.analysis_method = [self.analysis_method] if self.analysis_method is not None else []
        self.analysis_method = [v if isinstance(v, AnalysisMethod) else AnalysisMethod(v) for v in self.analysis_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SimulationSettings(YAMLRoot):
    """
    Settings in simulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["settings/SimulationSettings"]
    class_class_curie: ClassVar[str] = "biosim_schema:settings/SimulationSettings"
    class_name: ClassVar[str] = "SimulationSettings"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.SimulationSettings

    ensemble: Optional[Union[dict, "Ensemble"]] = None
    integrator: Optional[Union[dict, "Integrator"]] = None
    barostat: Optional[Union[dict, "Barostat"]] = None
    thermostat: Optional[Union[dict, "Thermostat"]] = None
    interactions: Optional[Union[dict, "Interactions"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ensemble is not None and not isinstance(self.ensemble, Ensemble):
            self.ensemble = Ensemble(**as_dict(self.ensemble))

        if self.integrator is not None and not isinstance(self.integrator, Integrator):
            self.integrator = Integrator(**as_dict(self.integrator))

        if self.barostat is not None and not isinstance(self.barostat, Barostat):
            self.barostat = Barostat(**as_dict(self.barostat))

        if self.thermostat is not None and not isinstance(self.thermostat, Thermostat):
            self.thermostat = Thermostat(**as_dict(self.thermostat))

        if self.interactions is not None and not isinstance(self.interactions, Interactions):
            self.interactions = Interactions(**as_dict(self.interactions))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ensemble(YAMLRoot):
    """
    Simulation ensemble/thermodynamic properties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["settings/Ensemble"]
    class_class_curie: ClassVar[str] = "biosim_schema:settings/Ensemble"
    class_name: ClassVar[str] = "Ensemble"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Ensemble

    ensemble_type: Optional[Union[str, "EnsembleType"]] = None
    random_seed: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ensemble_type is not None and not isinstance(self.ensemble_type, EnsembleType):
            self.ensemble_type = EnsembleType(self.ensemble_type)

        if self.random_seed is not None and not isinstance(self.random_seed, int):
            self.random_seed = int(self.random_seed)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Interactions(YAMLRoot):
    """
    Settings used to define particle interactions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["settings/Interactions"]
    class_class_curie: ClassVar[str] = "biosim_schema:settings/Interactions"
    class_name: ClassVar[str] = "Interactions"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Interactions

    restraints: Optional[Union[bool, Bool]] = None
    electrostatic_cutoff_distance: Optional[Union[dict, LengthQuantity]] = None
    vdw_cutoff_distance: Optional[Union[dict, LengthQuantity]] = None
    bond_length_constraints_algorithm: Optional[Union[str, "BondLengthConstraintsAlgorithm"]] = None
    long_range_interaction_method: Optional[Union[str, "LongRangeInteractionMethod"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.restraints is not None and not isinstance(self.restraints, Bool):
            self.restraints = Bool(self.restraints)

        if self.electrostatic_cutoff_distance is not None and not isinstance(self.electrostatic_cutoff_distance, LengthQuantity):
            self.electrostatic_cutoff_distance = LengthQuantity(**as_dict(self.electrostatic_cutoff_distance))

        if self.vdw_cutoff_distance is not None and not isinstance(self.vdw_cutoff_distance, LengthQuantity):
            self.vdw_cutoff_distance = LengthQuantity(**as_dict(self.vdw_cutoff_distance))

        if self.bond_length_constraints_algorithm is not None and not isinstance(self.bond_length_constraints_algorithm, BondLengthConstraintsAlgorithm):
            self.bond_length_constraints_algorithm = BondLengthConstraintsAlgorithm(self.bond_length_constraints_algorithm)

        if self.long_range_interaction_method is not None and not isinstance(self.long_range_interaction_method, LongRangeInteractionMethod):
            self.long_range_interaction_method = LongRangeInteractionMethod(self.long_range_interaction_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Integrator(YAMLRoot):
    """
    Settings used for the simulation integrator.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["settings/Integrator"]
    class_class_curie: ClassVar[str] = "biosim_schema:settings/Integrator"
    class_name: ClassVar[str] = "Integrator"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Integrator

    integrator_algorithm: Optional[Union[str, "IntegratorAlgorithm"]] = None
    frame_step: Optional[Union[dict, TimeQuantity]] = None
    time_step: Optional[Union[dict, TimeQuantity]] = None
    number_of_steps: Optional[int] = None
    simulation_time: Optional[Union[dict, TimeQuantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.integrator_algorithm is not None and not isinstance(self.integrator_algorithm, IntegratorAlgorithm):
            self.integrator_algorithm = IntegratorAlgorithm(self.integrator_algorithm)

        if self.frame_step is not None and not isinstance(self.frame_step, TimeQuantity):
            self.frame_step = TimeQuantity(**as_dict(self.frame_step))

        if self.time_step is not None and not isinstance(self.time_step, TimeQuantity):
            self.time_step = TimeQuantity(**as_dict(self.time_step))

        if self.number_of_steps is not None and not isinstance(self.number_of_steps, int):
            self.number_of_steps = int(self.number_of_steps)

        if self.simulation_time is not None and not isinstance(self.simulation_time, TimeQuantity):
            self.simulation_time = TimeQuantity(**as_dict(self.simulation_time))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Barostat(YAMLRoot):
    """
    Settings used for the simulation barostat.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["settings/Barostat"]
    class_class_curie: ClassVar[str] = "biosim_schema:settings/Barostat"
    class_name: ClassVar[str] = "Barostat"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Barostat

    barostat_algorithm: Optional[Union[str, "BarostatAlgorithm"]] = None
    compressibility: Optional[Union[dict, CompressibilityQuantity]] = None
    compressibility_vector: Optional[Union[dict, MatrixCompressibilityQuantity]] = None
    target_pressure: Optional[Union[dict, PressureQuantity]] = None
    target_pressure_vector: Optional[Union[dict, MatrixPressureQuantity]] = None
    pressure_time_constant: Optional[Union[dict, TimeQuantity]] = None
    pressure_coupling_frequency: Optional[Union[dict, FrequencyQuantity]] = None
    pressure_coupling_type: Optional[Union[str, "PressureCouplingType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.barostat_algorithm is not None and not isinstance(self.barostat_algorithm, BarostatAlgorithm):
            self.barostat_algorithm = BarostatAlgorithm(self.barostat_algorithm)

        if self.compressibility is not None and not isinstance(self.compressibility, CompressibilityQuantity):
            self.compressibility = CompressibilityQuantity(**as_dict(self.compressibility))

        if self.compressibility_vector is not None and not isinstance(self.compressibility_vector, MatrixCompressibilityQuantity):
            self.compressibility_vector = MatrixCompressibilityQuantity(**as_dict(self.compressibility_vector))

        if self.target_pressure is not None and not isinstance(self.target_pressure, PressureQuantity):
            self.target_pressure = PressureQuantity(**as_dict(self.target_pressure))

        if self.target_pressure_vector is not None and not isinstance(self.target_pressure_vector, MatrixPressureQuantity):
            self.target_pressure_vector = MatrixPressureQuantity(**as_dict(self.target_pressure_vector))

        if self.pressure_time_constant is not None and not isinstance(self.pressure_time_constant, TimeQuantity):
            self.pressure_time_constant = TimeQuantity(**as_dict(self.pressure_time_constant))

        if self.pressure_coupling_frequency is not None and not isinstance(self.pressure_coupling_frequency, FrequencyQuantity):
            self.pressure_coupling_frequency = FrequencyQuantity(**as_dict(self.pressure_coupling_frequency))

        if self.pressure_coupling_type is not None and not isinstance(self.pressure_coupling_type, PressureCouplingType):
            self.pressure_coupling_type = PressureCouplingType(self.pressure_coupling_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Thermostat(YAMLRoot):
    """
    Settings used for the simulation thermostat.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["settings/Thermostat"]
    class_class_curie: ClassVar[str] = "biosim_schema:settings/Thermostat"
    class_name: ClassVar[str] = "Thermostat"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Thermostat

    thermostat_algorithm: Optional[Union[str, "ThermostatAlgorithm"]] = None
    target_temperature: Optional[Union[dict, TemperatureQuantity]] = None
    target_temperature_vector: Optional[Union[dict, VectorTemperatureQuantity]] = None
    collision_frequency: Optional[Union[dict, FrequencyQuantity]] = None
    temperature_time_constant: Optional[Union[dict, VectorTimeQuantity]] = None
    coupling_group: Optional[str] = None
    chain_length: Optional[int] = None
    friction_coefficient: Optional[Union[dict, FrictionCoefficientQuantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.thermostat_algorithm is not None and not isinstance(self.thermostat_algorithm, ThermostatAlgorithm):
            self.thermostat_algorithm = ThermostatAlgorithm(self.thermostat_algorithm)

        if self.target_temperature is not None and not isinstance(self.target_temperature, TemperatureQuantity):
            self.target_temperature = TemperatureQuantity(**as_dict(self.target_temperature))

        if self.target_temperature_vector is not None and not isinstance(self.target_temperature_vector, VectorTemperatureQuantity):
            self.target_temperature_vector = VectorTemperatureQuantity(**as_dict(self.target_temperature_vector))

        if self.collision_frequency is not None and not isinstance(self.collision_frequency, FrequencyQuantity):
            self.collision_frequency = FrequencyQuantity(**as_dict(self.collision_frequency))

        if self.temperature_time_constant is not None and not isinstance(self.temperature_time_constant, VectorTimeQuantity):
            self.temperature_time_constant = VectorTimeQuantity(**as_dict(self.temperature_time_constant))

        if self.coupling_group is not None and not isinstance(self.coupling_group, str):
            self.coupling_group = str(self.coupling_group)

        if self.chain_length is not None and not isinstance(self.chain_length, int):
            self.chain_length = int(self.chain_length)

        if self.friction_coefficient is not None and not isinstance(self.friction_coefficient, FrictionCoefficientQuantity):
            self.friction_coefficient = FrictionCoefficientQuantity(**as_dict(self.friction_coefficient))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemComposition(YAMLRoot):
    """
    Molecular composition of simulated system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["composition/SystemComposition"]
    class_class_curie: ClassVar[str] = "biosim_schema:composition/SystemComposition"
    class_name: ClassVar[str] = "SystemComposition"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.SystemComposition

    system_counts: Optional[Union[dict, "SystemCounts"]] = None
    molecule_ID: Optional[Union[Union[dict, "MoleculeID"], list[Union[dict, "MoleculeID"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.system_counts is not None and not isinstance(self.system_counts, SystemCounts):
            self.system_counts = SystemCounts(**as_dict(self.system_counts))

        if not isinstance(self.molecule_ID, list):
            self.molecule_ID = [self.molecule_ID] if self.molecule_ID is not None else []
        self.molecule_ID = [v if isinstance(v, MoleculeID) else MoleculeID(**as_dict(v)) for v in self.molecule_ID]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemCounts(YAMLRoot):
    """
    Entity counts across the simulated system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["composition/SystemCounts"]
    class_class_curie: ClassVar[str] = "biosim_schema:composition/SystemCounts"
    class_name: ClassVar[str] = "SystemCounts"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.SystemCounts

    total_molecule_count: Optional[int] = None
    total_atom_count: Optional[int] = None
    unique_molecule_count: Optional[int] = None
    salt_concentration: Optional[Union[dict, ConcentrationQuantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.total_molecule_count is not None and not isinstance(self.total_molecule_count, int):
            self.total_molecule_count = int(self.total_molecule_count)

        if self.total_atom_count is not None and not isinstance(self.total_atom_count, int):
            self.total_atom_count = int(self.total_atom_count)

        if self.unique_molecule_count is not None and not isinstance(self.unique_molecule_count, int):
            self.unique_molecule_count = int(self.unique_molecule_count)

        if self.salt_concentration is not None and not isinstance(self.salt_concentration, ConcentrationQuantity):
            self.salt_concentration = ConcentrationQuantity(**as_dict(self.salt_concentration))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MoleculeID(YAMLRoot):
    """
    Identifiers of a molecule type in the simulated system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["composition/MoleculeID"]
    class_class_curie: ClassVar[str] = "biosim_schema:composition/MoleculeID"
    class_name: ClassVar[str] = "MoleculeID"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.MoleculeID

    PDB_ID: Optional[str] = None
    UNIPROT_ID: Optional[str] = None
    SMILES: Optional[str] = None
    InChI: Optional[str] = None
    InChIKey: Optional[str] = None
    alphafold_ID: Optional[str] = None
    PubChem_CID: Optional[str] = None
    protein_sequence: Optional[str] = None
    nucleic_sequence: Optional[str] = None
    predicted_structure: Optional[Union[bool, Bool]] = None
    modified: Optional[Union[bool, Bool]] = None
    molecular_formula: Optional[str] = None
    molecular_weight: Optional[Union[dict, MassQuantity]] = None
    molecule_charge: Optional[Union[dict, ChargeQuantity]] = None
    molecule_count: Optional[int] = None
    atom_count: Optional[int] = None
    monomer_count: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.PDB_ID is not None and not isinstance(self.PDB_ID, str):
            self.PDB_ID = str(self.PDB_ID)

        if self.UNIPROT_ID is not None and not isinstance(self.UNIPROT_ID, str):
            self.UNIPROT_ID = str(self.UNIPROT_ID)

        if self.SMILES is not None and not isinstance(self.SMILES, str):
            self.SMILES = str(self.SMILES)

        if self.InChI is not None and not isinstance(self.InChI, str):
            self.InChI = str(self.InChI)

        if self.InChIKey is not None and not isinstance(self.InChIKey, str):
            self.InChIKey = str(self.InChIKey)

        if self.alphafold_ID is not None and not isinstance(self.alphafold_ID, str):
            self.alphafold_ID = str(self.alphafold_ID)

        if self.PubChem_CID is not None and not isinstance(self.PubChem_CID, str):
            self.PubChem_CID = str(self.PubChem_CID)

        if self.protein_sequence is not None and not isinstance(self.protein_sequence, str):
            self.protein_sequence = str(self.protein_sequence)

        if self.nucleic_sequence is not None and not isinstance(self.nucleic_sequence, str):
            self.nucleic_sequence = str(self.nucleic_sequence)

        if self.predicted_structure is not None and not isinstance(self.predicted_structure, Bool):
            self.predicted_structure = Bool(self.predicted_structure)

        if self.modified is not None and not isinstance(self.modified, Bool):
            self.modified = Bool(self.modified)

        if self.molecular_formula is not None and not isinstance(self.molecular_formula, str):
            self.molecular_formula = str(self.molecular_formula)

        if self.molecular_weight is not None and not isinstance(self.molecular_weight, MassQuantity):
            self.molecular_weight = MassQuantity(**as_dict(self.molecular_weight))

        if self.molecule_charge is not None and not isinstance(self.molecule_charge, ChargeQuantity):
            self.molecule_charge = ChargeQuantity(**as_dict(self.molecule_charge))

        if self.molecule_count is not None and not isinstance(self.molecule_count, int):
            self.molecule_count = int(self.molecule_count)

        if self.atom_count is not None and not isinstance(self.atom_count, int):
            self.atom_count = int(self.atom_count)

        if self.monomer_count is not None and not isinstance(self.monomer_count, int):
            self.monomer_count = int(self.monomer_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SimulationObservables(YAMLRoot):
    """
    Simulation observables outputted from simulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["observables/SimulationObservables"]
    class_class_curie: ClassVar[str] = "biosim_schema:observables/SimulationObservables"
    class_name: ClassVar[str] = "SimulationObservables"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.SimulationObservables

    simulation_averages: Optional[Union[dict, "SimulationAverages"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.simulation_averages is not None and not isinstance(self.simulation_averages, SimulationAverages):
            self.simulation_averages = SimulationAverages(**as_dict(self.simulation_averages))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SimulationAverages(YAMLRoot):
    """
    Average values of observables outputted from the simulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["observables/SimulationAverages"]
    class_class_curie: ClassVar[str] = "biosim_schema:observables/SimulationAverages"
    class_name: ClassVar[str] = "SimulationAverages"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.SimulationAverages

    average_kinetic_energy: Optional[Union[dict, MolarEnergyQuantity]] = None
    average_potential_energy: Optional[Union[dict, MolarEnergyQuantity]] = None
    average_enthalpy: Optional[Union[dict, MolarEnergyQuantity]] = None
    average_pressure: Optional[Union[dict, PressureQuantity]] = None
    average_temperature: Optional[Union[dict, TemperatureQuantity]] = None
    average_volume: Optional[Union[dict, VolumeQuantity]] = None
    average_volume_vector: Optional[Union[dict, VectorVolumeQuantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.average_kinetic_energy is not None and not isinstance(self.average_kinetic_energy, MolarEnergyQuantity):
            self.average_kinetic_energy = MolarEnergyQuantity(**as_dict(self.average_kinetic_energy))

        if self.average_potential_energy is not None and not isinstance(self.average_potential_energy, MolarEnergyQuantity):
            self.average_potential_energy = MolarEnergyQuantity(**as_dict(self.average_potential_energy))

        if self.average_enthalpy is not None and not isinstance(self.average_enthalpy, MolarEnergyQuantity):
            self.average_enthalpy = MolarEnergyQuantity(**as_dict(self.average_enthalpy))

        if self.average_pressure is not None and not isinstance(self.average_pressure, PressureQuantity):
            self.average_pressure = PressureQuantity(**as_dict(self.average_pressure))

        if self.average_temperature is not None and not isinstance(self.average_temperature, TemperatureQuantity):
            self.average_temperature = TemperatureQuantity(**as_dict(self.average_temperature))

        if self.average_volume is not None and not isinstance(self.average_volume, VolumeQuantity):
            self.average_volume = VolumeQuantity(**as_dict(self.average_volume))

        if self.average_volume_vector is not None and not isinstance(self.average_volume_vector, VectorVolumeQuantity):
            self.average_volume_vector = VectorVolumeQuantity(**as_dict(self.average_volume_vector))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TopologyMetadata(YAMLRoot):
    """
    Topology information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["topology/TopologyMetadata"]
    class_class_curie: ClassVar[str] = "biosim_schema:topology/TopologyMetadata"
    class_name: ClassVar[str] = "TopologyMetadata"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.TopologyMetadata

    connectivity: Optional[Union[dict, "Connectivity"]] = None
    particles: Optional[Union[dict, "Particles"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.connectivity is not None and not isinstance(self.connectivity, Connectivity):
            self.connectivity = Connectivity(**as_dict(self.connectivity))

        if self.particles is not None and not isinstance(self.particles, Particles):
            self.particles = Particles(**as_dict(self.particles))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Connectivity(YAMLRoot):
    """
    Connectivity information included in the topology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["topology/Connectivity"]
    class_class_curie: ClassVar[str] = "biosim_schema:topology/Connectivity"
    class_name: ClassVar[str] = "Connectivity"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Connectivity

    bonds: Optional[Union[bool, Bool]] = None
    dihedrals: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.bonds is not None and not isinstance(self.bonds, Bool):
            self.bonds = Bool(self.bonds)

        if self.dihedrals is not None and not isinstance(self.dihedrals, Bool):
            self.dihedrals = Bool(self.dihedrals)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Particles(YAMLRoot):
    """
    Particle information included in the topology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["topology/Particles"]
    class_class_curie: ClassVar[str] = "biosim_schema:topology/Particles"
    class_name: ClassVar[str] = "Particles"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Particles

    masses: Optional[Union[bool, Bool]] = None
    fixed_charges: Optional[Union[bool, Bool]] = None
    system_charge: Optional[Union[dict, ChargeQuantity]] = None
    coarse_grained: Optional[Union[bool, Bool]] = None
    resolution: Optional[Union[str, "ModelResolution"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.masses is not None and not isinstance(self.masses, Bool):
            self.masses = Bool(self.masses)

        if self.fixed_charges is not None and not isinstance(self.fixed_charges, Bool):
            self.fixed_charges = Bool(self.fixed_charges)

        if self.system_charge is not None and not isinstance(self.system_charge, ChargeQuantity):
            self.system_charge = ChargeQuantity(**as_dict(self.system_charge))

        if self.coarse_grained is not None and not isinstance(self.coarse_grained, Bool):
            self.coarse_grained = Bool(self.coarse_grained)

        if self.resolution is not None and not isinstance(self.resolution, ModelResolution):
            self.resolution = ModelResolution(self.resolution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TrajectoryMetadata(YAMLRoot):
    """
    Trajectory information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["trajectory/TrajectoryMetadata"]
    class_class_curie: ClassVar[str] = "biosim_schema:trajectory/TrajectoryMetadata"
    class_name: ClassVar[str] = "TrajectoryMetadata"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.TrajectoryMetadata

    simulation_box: Optional[Union[dict, "SimulationBox"]] = None
    trajectory_output: Optional[Union[dict, "Trajectories"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.simulation_box is not None and not isinstance(self.simulation_box, SimulationBox):
            self.simulation_box = SimulationBox(**as_dict(self.simulation_box))

        if self.trajectory_output is not None and not isinstance(self.trajectory_output, Trajectories):
            self.trajectory_output = Trajectories(**as_dict(self.trajectory_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SimulationBox(YAMLRoot):
    """
    Simulation box information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["trajectory/SimulationBox"]
    class_class_curie: ClassVar[str] = "biosim_schema:trajectory/SimulationBox"
    class_name: ClassVar[str] = "SimulationBox"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.SimulationBox

    box_dimensions: Optional[Union[dict, VectorLengthQuantity]] = None
    box_angles: Optional[Union[dict, VectorAngleQuantity]] = None
    box_type: Optional[Union[str, "BoxType"]] = None
    periodic_boundary_conditions: Optional[Union[str, "PeriodicBoundaryConditions"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.box_dimensions is not None and not isinstance(self.box_dimensions, VectorLengthQuantity):
            self.box_dimensions = VectorLengthQuantity(**as_dict(self.box_dimensions))

        if self.box_angles is not None and not isinstance(self.box_angles, VectorAngleQuantity):
            self.box_angles = VectorAngleQuantity(**as_dict(self.box_angles))

        if self.box_type is not None and not isinstance(self.box_type, BoxType):
            self.box_type = BoxType(self.box_type)

        if self.periodic_boundary_conditions is not None and not isinstance(self.periodic_boundary_conditions, PeriodicBoundaryConditions):
            self.periodic_boundary_conditions = PeriodicBoundaryConditions(self.periodic_boundary_conditions)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Trajectories(YAMLRoot):
    """
    Information in trajectory files.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["trajectory/Trajectories"]
    class_class_curie: ClassVar[str] = "biosim_schema:trajectory/Trajectories"
    class_name: ClassVar[str] = "Trajectories"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Trajectories

    positions: Optional[Union[bool, Bool]] = None
    forces: Optional[Union[bool, Bool]] = None
    velocities: Optional[Union[bool, Bool]] = None
    polarizable_charges: Optional[Union[bool, Bool]] = None
    energies: Optional[Union[bool, Bool]] = None
    water: Optional[Union[bool, Bool]] = None
    replica: Optional[Union[bool, Bool]] = None
    frame_count: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.positions is not None and not isinstance(self.positions, Bool):
            self.positions = Bool(self.positions)

        if self.forces is not None and not isinstance(self.forces, Bool):
            self.forces = Bool(self.forces)

        if self.velocities is not None and not isinstance(self.velocities, Bool):
            self.velocities = Bool(self.velocities)

        if self.polarizable_charges is not None and not isinstance(self.polarizable_charges, Bool):
            self.polarizable_charges = Bool(self.polarizable_charges)

        if self.energies is not None and not isinstance(self.energies, Bool):
            self.energies = Bool(self.energies)

        if self.water is not None and not isinstance(self.water, Bool):
            self.water = Bool(self.water)

        if self.replica is not None and not isinstance(self.replica, Bool):
            self.replica = Bool(self.replica)

        if self.frame_count is not None and not isinstance(self.frame_count, int):
            self.frame_count = int(self.frame_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PotentialMetadata(YAMLRoot):
    """
    Potentials used for various modelled molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["potentials/PotentialMetadata"]
    class_class_curie: ClassVar[str] = "biosim_schema:potentials/PotentialMetadata"
    class_name: ClassVar[str] = "PotentialMetadata"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.PotentialMetadata

    water_potential: Optional[Union[dict, "WaterPotential"]] = None
    protein_potential: Optional[Union[dict, "ProteinPotential"]] = None
    lipid_potential: Optional[Union[dict, "LipidPotential"]] = None
    nucleic_potential: Optional[Union[dict, "NucleicPotential"]] = None
    carbohydrate_potential: Optional[Union[dict, "CarbohydratePotential"]] = None
    polymer_potential: Optional[Union[dict, "PolymerPotential"]] = None
    general_potential: Optional[Union[dict, "GeneralPotential"]] = None
    machine_learned_potential: Optional[Union[dict, "MachineLearnedPotential"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.water_potential is not None and not isinstance(self.water_potential, WaterPotential):
            self.water_potential = WaterPotential(**as_dict(self.water_potential))

        if self.protein_potential is not None and not isinstance(self.protein_potential, ProteinPotential):
            self.protein_potential = ProteinPotential(**as_dict(self.protein_potential))

        if self.lipid_potential is not None and not isinstance(self.lipid_potential, LipidPotential):
            self.lipid_potential = LipidPotential(**as_dict(self.lipid_potential))

        if self.nucleic_potential is not None and not isinstance(self.nucleic_potential, NucleicPotential):
            self.nucleic_potential = NucleicPotential(**as_dict(self.nucleic_potential))

        if self.carbohydrate_potential is not None and not isinstance(self.carbohydrate_potential, CarbohydratePotential):
            self.carbohydrate_potential = CarbohydratePotential(**as_dict(self.carbohydrate_potential))

        if self.polymer_potential is not None and not isinstance(self.polymer_potential, PolymerPotential):
            self.polymer_potential = PolymerPotential(**as_dict(self.polymer_potential))

        if self.general_potential is not None and not isinstance(self.general_potential, GeneralPotential):
            self.general_potential = GeneralPotential(**as_dict(self.general_potential))

        if self.machine_learned_potential is not None and not isinstance(self.machine_learned_potential, MachineLearnedPotential):
            self.machine_learned_potential = MachineLearnedPotential(**as_dict(self.machine_learned_potential))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WaterPotential(YAMLRoot):
    """
    Potential used for water molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["potentials/WaterPotential"]
    class_class_curie: ClassVar[str] = "biosim_schema:potentials/WaterPotential"
    class_name: ClassVar[str] = "WaterPotential"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.WaterPotential

    water_potential_name: Optional[Union[str, "WaterPotentialName"]] = None
    modified: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.water_potential_name is not None and not isinstance(self.water_potential_name, WaterPotentialName):
            self.water_potential_name = WaterPotentialName(self.water_potential_name)

        if self.modified is not None and not isinstance(self.modified, Bool):
            self.modified = Bool(self.modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinPotential(YAMLRoot):
    """
    Potential used for protein molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["potentials/ProteinPotential"]
    class_class_curie: ClassVar[str] = "biosim_schema:potentials/ProteinPotential"
    class_name: ClassVar[str] = "ProteinPotential"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.ProteinPotential

    protein_potential_name: Optional[Union[str, "ProteinPotentialName"]] = None
    modified: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.protein_potential_name is not None and not isinstance(self.protein_potential_name, ProteinPotentialName):
            self.protein_potential_name = ProteinPotentialName(self.protein_potential_name)

        if self.modified is not None and not isinstance(self.modified, Bool):
            self.modified = Bool(self.modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LipidPotential(YAMLRoot):
    """
    Potential used for lipid molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["potentials/LipidPotential"]
    class_class_curie: ClassVar[str] = "biosim_schema:potentials/LipidPotential"
    class_name: ClassVar[str] = "LipidPotential"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.LipidPotential

    lipid_potential_name: Optional[Union[str, "LipidPotentialName"]] = None
    modified: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.lipid_potential_name is not None and not isinstance(self.lipid_potential_name, LipidPotentialName):
            self.lipid_potential_name = LipidPotentialName(self.lipid_potential_name)

        if self.modified is not None and not isinstance(self.modified, Bool):
            self.modified = Bool(self.modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NucleicPotential(YAMLRoot):
    """
    Potential used for nucleic acid molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["potentials/NucleicPotential"]
    class_class_curie: ClassVar[str] = "biosim_schema:potentials/NucleicPotential"
    class_name: ClassVar[str] = "NucleicPotential"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.NucleicPotential

    nucleic_potential_name: Optional[Union[str, "NucleicPotentialName"]] = None
    modified: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.nucleic_potential_name is not None and not isinstance(self.nucleic_potential_name, NucleicPotentialName):
            self.nucleic_potential_name = NucleicPotentialName(self.nucleic_potential_name)

        if self.modified is not None and not isinstance(self.modified, Bool):
            self.modified = Bool(self.modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CarbohydratePotential(YAMLRoot):
    """
    Potential used for carbohydrate molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["potentials/CarbohydratePotential"]
    class_class_curie: ClassVar[str] = "biosim_schema:potentials/CarbohydratePotential"
    class_name: ClassVar[str] = "CarbohydratePotential"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.CarbohydratePotential

    carbohydrate_potential_name: Optional[Union[str, "CarbohydratePotentialName"]] = None
    modified: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.carbohydrate_potential_name is not None and not isinstance(self.carbohydrate_potential_name, CarbohydratePotentialName):
            self.carbohydrate_potential_name = CarbohydratePotentialName(self.carbohydrate_potential_name)

        if self.modified is not None and not isinstance(self.modified, Bool):
            self.modified = Bool(self.modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PolymerPotential(YAMLRoot):
    """
    Potential used for polymers molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["potentials/PolymerPotential"]
    class_class_curie: ClassVar[str] = "biosim_schema:potentials/PolymerPotential"
    class_name: ClassVar[str] = "PolymerPotential"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.PolymerPotential

    polymer_potential_name: Optional[Union[str, "PolymerPotentialName"]] = None
    modified: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.polymer_potential_name is not None and not isinstance(self.polymer_potential_name, PolymerPotentialName):
            self.polymer_potential_name = PolymerPotentialName(self.polymer_potential_name)

        if self.modified is not None and not isinstance(self.modified, Bool):
            self.modified = Bool(self.modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneralPotential(YAMLRoot):
    """
    Potential used for molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["potentials/GeneralPotential"]
    class_class_curie: ClassVar[str] = "biosim_schema:potentials/GeneralPotential"
    class_name: ClassVar[str] = "GeneralPotential"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.GeneralPotential

    general_potential_name: Optional[Union[str, "GeneralPotentialName"]] = None
    modified: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.general_potential_name is not None and not isinstance(self.general_potential_name, GeneralPotentialName):
            self.general_potential_name = GeneralPotentialName(self.general_potential_name)

        if self.modified is not None and not isinstance(self.modified, Bool):
            self.modified = Bool(self.modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MachineLearnedPotential(YAMLRoot):
    """
    Machine learned potential used for molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["potentials/MachineLearnedPotential"]
    class_class_curie: ClassVar[str] = "biosim_schema:potentials/MachineLearnedPotential"
    class_name: ClassVar[str] = "MachineLearnedPotential"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.MachineLearnedPotential

    machine_learned_potential_name: Optional[Union[str, "MachineLearnedPotentialName"]] = None
    modified: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.machine_learned_potential_name is not None and not isinstance(self.machine_learned_potential_name, MachineLearnedPotentialName):
            self.machine_learned_potential_name = MachineLearnedPotentialName(self.machine_learned_potential_name)

        if self.modified is not None and not isinstance(self.modified, Bool):
            self.modified = Bool(self.modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputationalEnvironment(YAMLRoot):
    """
    Computational environment used to perform simulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["compute/ComputationalEnvironment"]
    class_class_curie: ClassVar[str] = "biosim_schema:compute/ComputationalEnvironment"
    class_name: ClassVar[str] = "ComputationalEnvironment"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.ComputationalEnvironment

    hardware: Optional[Union[dict, "Hardware"]] = None
    software: Optional[Union[dict, "Software"]] = None
    performance: Optional[Union[dict, "Performance"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.hardware is not None and not isinstance(self.hardware, Hardware):
            self.hardware = Hardware(**as_dict(self.hardware))

        if self.software is not None and not isinstance(self.software, Software):
            self.software = Software(**as_dict(self.software))

        if self.performance is not None and not isinstance(self.performance, Performance):
            self.performance = Performance(**as_dict(self.performance))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hardware(YAMLRoot):
    """
    Computer hardware used to perform simulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["compute/Hardware"]
    class_class_curie: ClassVar[str] = "biosim_schema:compute/Hardware"
    class_name: ClassVar[str] = "Hardware"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Hardware

    execution_platform: Optional[Union[str, "ExecutionPlatform"]] = None
    node_type: Optional[Union[str, "NodeType"]] = None
    node_count: Optional[int] = None
    CPU_vendor: Optional[Union[str, "CpuVendor"]] = None
    CPU_architecture: Optional[Union[str, "CpuArchitecture"]] = None
    sockets_per_node: Optional[int] = None
    cores_per_socket: Optional[int] = None
    threads_per_core: Optional[int] = None
    GPU_vendor: Optional[Union[str, "GpuVendor"]] = None
    GPUs_per_node: Optional[int] = None
    memory_per_node: Optional[Union[dict, ByteQuantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.execution_platform is not None and not isinstance(self.execution_platform, ExecutionPlatform):
            self.execution_platform = ExecutionPlatform(self.execution_platform)

        if self.node_type is not None and not isinstance(self.node_type, NodeType):
            self.node_type = NodeType(self.node_type)

        if self.node_count is not None and not isinstance(self.node_count, int):
            self.node_count = int(self.node_count)

        if self.CPU_vendor is not None and not isinstance(self.CPU_vendor, CpuVendor):
            self.CPU_vendor = CpuVendor(self.CPU_vendor)

        if self.CPU_architecture is not None and not isinstance(self.CPU_architecture, CpuArchitecture):
            self.CPU_architecture = CpuArchitecture(self.CPU_architecture)

        if self.sockets_per_node is not None and not isinstance(self.sockets_per_node, int):
            self.sockets_per_node = int(self.sockets_per_node)

        if self.cores_per_socket is not None and not isinstance(self.cores_per_socket, int):
            self.cores_per_socket = int(self.cores_per_socket)

        if self.threads_per_core is not None and not isinstance(self.threads_per_core, int):
            self.threads_per_core = int(self.threads_per_core)

        if self.GPU_vendor is not None and not isinstance(self.GPU_vendor, GpuVendor):
            self.GPU_vendor = GpuVendor(self.GPU_vendor)

        if self.GPUs_per_node is not None and not isinstance(self.GPUs_per_node, int):
            self.GPUs_per_node = int(self.GPUs_per_node)

        if self.memory_per_node is not None and not isinstance(self.memory_per_node, ByteQuantity):
            self.memory_per_node = ByteQuantity(**as_dict(self.memory_per_node))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Software(YAMLRoot):
    """
    Computer software used to perform simulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["compute/Software"]
    class_class_curie: ClassVar[str] = "biosim_schema:compute/Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Software

    operating_system: Optional[Union[str, "OperatingSystem"]] = None
    scheduler: Optional[Union[str, "Scheduler"]] = None
    MPI_library: Optional[Union[str, "MPILibrary"]] = None
    container_runtime: Optional[Union[str, "ContainerRuntime"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.operating_system is not None and not isinstance(self.operating_system, OperatingSystem):
            self.operating_system = OperatingSystem(self.operating_system)

        if self.scheduler is not None and not isinstance(self.scheduler, Scheduler):
            self.scheduler = Scheduler(self.scheduler)

        if self.MPI_library is not None and not isinstance(self.MPI_library, MPILibrary):
            self.MPI_library = MPILibrary(self.MPI_library)

        if self.container_runtime is not None and not isinstance(self.container_runtime, ContainerRuntime):
            self.container_runtime = ContainerRuntime(self.container_runtime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Performance(YAMLRoot):
    """
    Compute performance during simulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["compute/Performance"]
    class_class_curie: ClassVar[str] = "biosim_schema:compute/Performance"
    class_name: ClassVar[str] = "Performance"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.Performance

    wall_time: Optional[Union[dict, TimeQuantity]] = None
    energy_consumption: Optional[Union[dict, EnergyQuantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.wall_time is not None and not isinstance(self.wall_time, TimeQuantity):
            self.wall_time = TimeQuantity(**as_dict(self.wall_time))

        if self.energy_consumption is not None and not isinstance(self.energy_consumption, EnergyQuantity):
            self.energy_consumption = EnergyQuantity(**as_dict(self.energy_consumption))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FileMetadata(YAMLRoot):
    """
    Metadata about uploaded or referenced files.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSIM_SCHEMA["files/FileMetadata"]
    class_class_curie: ClassVar[str] = "biosim_schema:files/FileMetadata"
    class_name: ClassVar[str] = "FileMetadata"
    class_model_uri: ClassVar[URIRef] = BIOSIM_SCHEMA.FileMetadata

    file_name: str = None
    file_size: Optional[Union[dict, ByteQuantity]] = None
    file_hash: Optional[str] = None
    file_hash_algorithm: Optional[Union[str, "FileHashAlgorithm"]] = None
    file_role: Optional[Union[str, "FileRole"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.file_size is not None and not isinstance(self.file_size, ByteQuantity):
            self.file_size = ByteQuantity(**as_dict(self.file_size))

        if self.file_hash is not None and not isinstance(self.file_hash, str):
            self.file_hash = str(self.file_hash)

        if self.file_hash_algorithm is not None and not isinstance(self.file_hash_algorithm, FileHashAlgorithm):
            self.file_hash_algorithm = FileHashAlgorithm(self.file_hash_algorithm)

        if self.file_role is not None and not isinstance(self.file_role, FileRole):
            self.file_role = FileRole(self.file_role)

        super().__post_init__(**kwargs)


# Enumerations
class LengthUnit(EnumDefinitionImpl):
    """
    Units for length quantity.
    """
    Å = PermissibleValue(
        text="Å",
        description="Length units in Angstrom.",
        meaning=QUDT["ANGSTROM"])
    nm = PermissibleValue(
        text="nm",
        description="Length units in nanometers.",
        meaning=QUDT["NanoM"])

    _defn = EnumDefinition(
        name="LengthUnit",
        description="Units for length quantity.",
    )

class VolumeUnit(EnumDefinitionImpl):
    """
    Units for volume quantity.
    """
    _defn = EnumDefinition(
        name="VolumeUnit",
        description="Units for volume quantity.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Å³",
            PermissibleValue(
                text="Å³",
                description="Volume units in Angstrom^3.",
                meaning=QUDT["ANGSTROM3"]))
        setattr(cls, "nm³",
            PermissibleValue(
                text="nm³",
                description="Volume units in nanometer^3."))

class ConcentrationUnit(EnumDefinitionImpl):
    """
    Units for concentration quantity.
    """
    M = PermissibleValue(
        text="M",
        description="Molar concentration",
        meaning=QUDT["MOL-PER-M3"])

    _defn = EnumDefinition(
        name="ConcentrationUnit",
        description="Units for concentration quantity.",
    )

class ChargeUnit(EnumDefinitionImpl):
    """
    Units for charge quantity.
    """
    e = PermissibleValue(
        text="e",
        description="Electric charge carried by a single proton or by a single electron.",
        meaning=QUDT["E"])
    C = PermissibleValue(
        text="C",
        description="""The SI unit of electric charge. One coulomb is the amount of charge accumulated in one second by a current of one ampere.""",
        meaning=QUDT["C"])

    _defn = EnumDefinition(
        name="ChargeUnit",
        description="Units for charge quantity.",
    )

class TimeUnit(EnumDefinitionImpl):
    """
    Units used to describe time.
    """
    s = PermissibleValue(
        text="s",
        description="Time units in seconds.",
        meaning=QUDT["SEC"])
    ms = PermissibleValue(
        text="ms",
        description="Time units in milliseconds.",
        meaning=QUDT["MilliSEC"])
    μs = PermissibleValue(
        text="μs",
        description="Time units in microseconds.",
        meaning=QUDT["MicroSEC"])
    ns = PermissibleValue(
        text="ns",
        description="Time units in nanoseconds.",
        meaning=QUDT["NanoSEC"])
    ps = PermissibleValue(
        text="ps",
        description="Time units in picoseconds.",
        meaning=QUDT["PicoSEC"])
    fs = PermissibleValue(
        text="fs",
        description="Time units in femtoseconds.")

    _defn = EnumDefinition(
        name="TimeUnit",
        description="Units used to describe time.",
    )

class FrequencyUnit(EnumDefinitionImpl):
    """
    Units used to describe frequency.
    """
    _defn = EnumDefinition(
        name="FrequencyUnit",
        description="Units used to describe frequency.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1/ps",
            PermissibleValue(
                text="1/ps",
                description="Frequncy units in reciprocal picoseconds."))

class FrictionCoefficientUnit(EnumDefinitionImpl):
    """
    Relationship between applied forces and the resulting resistance to motion.
    """
    _defn = EnumDefinition(
        name="FrictionCoefficientUnit",
        description="Relationship between applied forces and the resulting resistance to motion.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "a/ps",
            PermissibleValue(
                text="a/ps",
                description="atomic mass unit per picosecond"))
        setattr(cls, "kg/s",
            PermissibleValue(
                text="kg/s",
                description="kilograms per second"))

class TemperatureUnit(EnumDefinitionImpl):
    """
    Units to describe temperature.
    """
    K = PermissibleValue(
        text="K",
        description="Kelvin")

    _defn = EnumDefinition(
        name="TemperatureUnit",
        description="Units to describe temperature.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "°C",
            PermissibleValue(
                text="°C",
                description="degrees Celcius."))
        setattr(cls, "°F",
            PermissibleValue(
                text="°F",
                description="degrees Fahrenheit."))

class PressureUnit(EnumDefinitionImpl):
    """
    Units to describe pressure.
    """
    bar = PermissibleValue(
        text="bar",
        description="bar")
    Pa = PermissibleValue(
        text="Pa",
        description="Pascal")

    _defn = EnumDefinition(
        name="PressureUnit",
        description="Units to describe pressure.",
    )

class CompressibilityUnit(EnumDefinitionImpl):
    """
    measures how the system volume responds to pressure changes.
    """
    _defn = EnumDefinition(
        name="CompressibilityUnit",
        description="measures how the system volume responds to pressure changes.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1/bar",
            PermissibleValue(
                text="1/bar",
                description="reciprocal bar",
                meaning=QUDT["PER-BAR"]))
        setattr(cls, "1/Pa",
            PermissibleValue(
                text="1/Pa",
                description="reciprocal Pascal",
                meaning=QUDT["PER-PA"]))

class AngleUnit(EnumDefinitionImpl):
    """
    Units for angles.
    """
    degree = PermissibleValue(
        text="degree",
        description="Angle units in degree.",
        meaning=QUDT["DEG"])
    radian = PermissibleValue(
        text="radian",
        description="Angle units in radian.",
        meaning=QUDT["RAD"])

    _defn = EnumDefinition(
        name="AngleUnit",
        description="Units for angles.",
    )

class MolarEnergyUnit(EnumDefinitionImpl):
    """
    Units for molar energy.
    """
    _defn = EnumDefinition(
        name="MolarEnergyUnit",
        description="Units for molar energy.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "kcal/mol",
            PermissibleValue(
                text="kcal/mol",
                description="kcal/mol",
                meaning=QUDT["KiloCAL-PER-MOL"]))
        setattr(cls, "kJ/mol",
            PermissibleValue(
                text="kJ/mol",
                description="kJ/mol",
                meaning=QUDT["KiloJ-PER-MOL"]))

class EnergyUnit(EnumDefinitionImpl):
    """
    Units for energy.
    """
    kWh = PermissibleValue(
        text="kWh",
        description="kilowatt-hour",
        meaning=QUDT["KiloW-HR"])

    _defn = EnumDefinition(
        name="EnergyUnit",
        description="Units for energy.",
    )

class ForceUnit(EnumDefinitionImpl):
    """
    Units for force.
    """
    _defn = EnumDefinition(
        name="ForceUnit",
        description="Units for force.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "kJ/mol/nm",
            PermissibleValue(
                text="kJ/mol/nm",
                description="kilojoules per mole per nanometer",
                meaning=QUDT["KiloJoulePerMoleNanometer"]))
        setattr(cls, "kcal/mol/Å",
            PermissibleValue(
                text="kcal/mol/Å",
                description="kilocalories per mole per angstrom",
                meaning=QUDT["KiloCAL-PER-MOL-ANGSTROM"]))

class MassUnit(EnumDefinitionImpl):
    """
    Units for mass/molecular weight
    """
    Da = PermissibleValue(
        text="Da",
        description="Dalton",
        meaning=QUDT["Dalton"])

    _defn = EnumDefinition(
        name="MassUnit",
        description="Units for mass/molecular weight",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "g/mol",
            PermissibleValue(
                text="g/mol",
                description="grams per mole",
                meaning=QUDT["GramPerMole"]))

class ByteUnit(EnumDefinitionImpl):
    """
    Units for Bytes.
    """
    GB = PermissibleValue(
        text="GB",
        description="Digital information storage units in GB.",
        meaning=QUDT["GigaBYTE"])
    MB = PermissibleValue(
        text="MB",
        description="Digital information storage units in MB.",
        meaning=QUDT["MegaBYTE"])

    _defn = EnumDefinition(
        name="ByteUnit",
        description="Units for Bytes.",
    )

class SetupTool(EnumDefinitionImpl):
    """
    Tool used to setup a system for simulation.
    """
    pdb4amber = PermissibleValue(
        text="pdb4amber",
        description="Helps in preparing pdb-format files coming from other places to be compatible with LEaP.")
    prepareforleap = PermissibleValue(
        text="prepareforleap",
        description="""An action inside cpptraj, that also helps make pdb-format files compatible with LEaP. It is particularly useful for carbohydrates.""")
    packmol = PermissibleValue(
        text="packmol",
        description="""PACKMOL creates an initial point for molecular dynamics simulations by packing molecules in defined regions of space.""")
    packmol_memgen = PermissibleValue(
        text="packmol_memgen",
        description="""Packmol-memgen provides a way to generate membrane systems, with or without protein, by orienting input proteins with Memembed and using Packmol as the packing engine.""")
    LEaP = PermissibleValue(
        text="LEaP",
        description="The primary program to create a new system in Amber, or to modify existing systems.")
    antechamber = PermissibleValue(
        text="antechamber",
        description="""The main program to develop force fields for small organic molecules using a version of the general Amber force field (GAFF).""")
    pyMSMT = PermissibleValue(
        text="pyMSMT",
        description="""A way to build, prototype and validate MM models of metalloproteins and organometallic compounds.""")
    mdgx = PermissibleValue(
        text="mdgx",
        description="""Allows the generation of bonded force field parameters for any molecule by fitting to quantum data.""")
    parmed = PermissibleValue(
        text="parmed",
        description="Provides a way to extract information about parameters defined in a parameter-topology file.")

    _defn = EnumDefinition(
        name="SetupTool",
        description="Tool used to setup a system for simulation.",
    )

class MinimisationAlgorithm(EnumDefinitionImpl):
    """
    Algorithm used to minimise particle interactions.
    """
    XMIN = PermissibleValue(
        text="XMIN",
        description="""Minimization algorithm used to relax molecular structures to their lowest potential energy state, particularly for finding very deep local minima. It is a quasi-Newton method that typically provides quadratically convergent minimization.""")
    LMOD = PermissibleValue(
        text="LMOD",
        description="""LMOD (Low-Mode) minimization is a specialized conformational search and energy minimization method designed to efficiently find low-energy structures by navigating along the low-frequency vibrational modes of a system.""")

    _defn = EnumDefinition(
        name="MinimisationAlgorithm",
        description="Algorithm used to minimise particle interactions.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Steepest Descent",
            PermissibleValue(
                text="Steepest Descent",
                description="Moves atoms in the opposite direction of the energy gradient (forces)."))
        setattr(cls, "Conjugate Gradient",
            PermissibleValue(
                text="Conjugate Gradient",
                description="""Uses both current gradient information and previous search directions to find a more efficient path to the minimum."""))
        setattr(cls, "L-BFGS",
            PermissibleValue(
                text="L-BFGS",
                description="""L-BFGS (Limited-memory Broyden–Fletcher–Goldfarb–Shanno) approximates the inverse Hessian matrix (second derivatives) using a limited number of previous steps, making it memory-efficient."""))
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No minimisation."))

class SimulationMethod(EnumDefinitionImpl):
    """
    Options for simulation methods.
    """
    Metadynamics = PermissibleValue(
        text="Metadynamics",
        description="""An enhanced sampling technique that adds a history-dependent bias to the potential energy surface, encouraging the system to escape local minima and explore new configurations, often used to reconstruct free energy landscapes.""")

    _defn = EnumDefinition(
        name="SimulationMethod",
        description="Options for simulation methods.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Self-guided Langevin Dynamics",
            PermissibleValue(
                text="Self-guided Langevin Dynamics",
                description="Method that accelerates low frequency motion to enhance conformational sampling."))
        setattr(cls, "Accelerated Molecular Dynamics",
            PermissibleValue(
                text="Accelerated Molecular Dynamics",
                description="""Method where a bias potential that reduces the height of local barriers, allowing the faster evolution of a calculation."""))
        setattr(cls, "Gaussian Accelerated Molecular Dynamics",
            PermissibleValue(
                text="Gaussian Accelerated Molecular Dynamics",
                description="""Method that adds a harmonic boost potential (following a Gaussian distribution) to smooth the system potential energy surface."""))
        setattr(cls, "Targeted Molecular Dynamics",
            PermissibleValue(
                text="Targeted Molecular Dynamics",
                description="""Method that adds an additional term to the energy function based on the mass-wieghted root mean square deviation of a set of atoms in the current structure compared to a reference structure."""))
        setattr(cls, "Nudged Elastic Band Calculations",
            PermissibleValue(
                text="Nudged Elastic Band Calculations",
                description="""Method where the path for a conformational change is approximated with a series of images describing the molecule at discrete points along the path."""))
        setattr(cls, "Adaptive String Method",
            PermissibleValue(
                text="Adaptive String Method",
                description="""Method to find the Minimum Free Energy Path (MFEP) in the space of selected collective variables connecting initial and final stages of a given process."""))
        setattr(cls, "LMOD method",
            PermissibleValue(
                text="LMOD method",
                description="""Conformational search algorithm based on eigenvector following of low frequency vibrational modes."""))
        setattr(cls, "DL-FIND Optimization",
            PermissibleValue(
                text="DL-FIND Optimization",
                description="""Method to search for potential energy stationary points along a chemical reaction in a QM/MM simulation."""))
        setattr(cls, "Thermodynamic Integration (TI)",
            PermissibleValue(
                text="Thermodynamic Integration (TI)",
                description="""Method to calculate ensemble-averaged energies \"on-the-fly\" along a path as the simulation progresses between two states."""))
        setattr(cls, "Linear Interaction Energies (LIE)",
            PermissibleValue(
                text="Linear Interaction Energies (LIE)",
                description="Method to compute binding free energies using the linear interaction energy model."))
        setattr(cls, "Replica Exchange Molecular Dynamics (REMD)",
            PermissibleValue(
                text="Replica Exchange Molecular Dynamics (REMD)",
                description="""An expanded ensemble energy method that samples from an ensemble larger than a typical statistical mechanical ensemble defined by the Hamiltonian governing the system."""))
        setattr(cls, "Adaptively Biased Molecular Dynamics (ABMD)",
            PermissibleValue(
                text="Adaptively Biased Molecular Dynamics (ABMD)",
                description="""Method for calculating free energy landscapes as a function of a small number of collective variables."""))
        setattr(cls, "Steered Molecular Dynamics (SMD)",
            PermissibleValue(
                text="Steered Molecular Dynamics (SMD)",
                description="""Method that applies an external force onto a physical system, and drives a change in coordinates within a certain time. The moethod should be thought of as umbrella sampling where the center of the restraint is time-dependent."""))
        setattr(cls, "Umbrella Sampling",
            PermissibleValue(
                text="Umbrella Sampling",
                description="""A method that enhances sampling of rare events by applying a biasing potential to restrain the system along a chosen coordinate, allowing for the calculation of free energy profiles."""))
        setattr(cls, "Swarms of Trajectories String Method",
            PermissibleValue(
                text="Swarms of Trajectories String Method",
                description="""A version of the string method, a path-finding algorithm that refines a punative transition pathway iteratively until the path is deemed to have been converged."""))
        setattr(cls, "Constant pH Molecular Dynamics",
            PermissibleValue(
                text="Constant pH Molecular Dynamics",
                description="""Method that uses Monte Carlo sampling of the Boltzmann distribution of discrete protonation states concurrent with the molecular dynamics simulation."""))
        setattr(cls, "Constant Redox Potential Molecular Dynamics",
            PermissibleValue(
                text="Constant Redox Potential Molecular Dynamics",
                description="""Method that uses Monte Carlo sampling of the Boltzmann distribution of discrete redox sates concurrent with the molecular dynamics simulation."""))
        setattr(cls, "Continuous Constant pH Molecular Dynamics",
            PermissibleValue(
                text="Continuous Constant pH Molecular Dynamics",
                description="""A method that is an alternative to the Monte-Carlo based constant pH methods where particles with fictitious mass and coordinates bound between 0 (protonated) and 1 (deprotonated) are added to the system to present protonation states of titratable sites."""))
        setattr(cls, "NMR Refinement",
            PermissibleValue(
                text="NMR Refinement",
                description="""Method to incorporate a variety of restraints (e.g. NMR restraints derived from NOE and J-coupling data) into an optimization procedure."""))
        setattr(cls, "X-ray and CryoEM Refinement",
            PermissibleValue(
                text="X-ray and CryoEM Refinement",
                description="""Method to incorporate electron microscopy (EM) image information into macromolecular structure determination, by applying restraints for rigid and flexible fitting into EM maps."""))
        setattr(cls, "Locally Enhanced Sampling",
            PermissibleValue(
                text="Locally Enhanced Sampling",
                description="""A method to allow for multiple local copies of regions within a larger biomolecule, e.g. to allow sidechains in a protein to be \"disordered\", while the backbone is represented as a single configuration."""))

class SimulationTool(EnumDefinitionImpl):
    """
    Tools/utility used within simulation engines to perform simulations.
    """
    sander = PermissibleValue(
        text="sander",
        description="A tool with AmberTools that is a basic energy minimizer and molecular dynamics program.")
    pmemd = PermissibleValue(
        text="pmemd",
        description="""Part of Amber and is a version of the sander simulation tool that is optimized for speed and for parallel scaling.""")
    mdrun = PermissibleValue(
        text="mdrun",
        description="""The main molecular dynamics engine of GROMACS, used to perform energy minimization, molecular dynamics simulations, and analysis. It executes the simulation based on input files prepared by other GROMACS tools, supporting a wide range of simulation types and parallelization options.""")

    _defn = EnumDefinition(
        name="SimulationTool",
        description="Tools/utility used within simulation engines to perform simulations.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "gem.pmemd",
            PermissibleValue(
                text="gem.pmemd",
                description="""gem.pmemd is a part of AmberTools that is a CPI-only variant of the pmemd program that is designed for calculations using \"advanced\" force fields, such as AMOEBA and GEM."""))

class SimulationSoftware(EnumDefinitionImpl):
    """
    Simulation software used to perform molecular dynamics simulations and related functions.
    """
    Amber = PermissibleValue(
        text="Amber",
        description="""A collective name for a suite of programs that allo users to carry out molecular dynamics simulations, particulary on biomolecules.""")
    GROMACS = PermissibleValue(
        text="GROMACS",
        description="""GROMACS (GROningen Machine for Chemical Simulations) is a free, open-source, high-performance MD software package designed for simulating biochemical molecules like proteins, lipids, and nucleic acids.""")
    LAMMPS = PermissibleValue(
        text="LAMMPS",
        description="""LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) is an open-source classical molecular dynamics code designed for material modeling, including solids, soft matter, and coarse-grained systems.""")
    NAMD = PermissibleValue(
        text="NAMD",
        description="""NAMD (Nanoscale Molecular Dynamics, formerly Not Another Molecular Dynamics Program) is computer software for molecular dynamics simulation, written using the Charm++ parallel programming model.""")
    OpenMM = PermissibleValue(
        text="OpenMM",
        description="""OpenMM is a library for performing molecular dynamics simulations on a wide variety of hardware architectures.""")
    CHARMM = PermissibleValue(
        text="CHARMM",
        description="""CHARMM (Chemistry at HARvard Macromolecular Mechanics) is a molecular simulation program with broad application to many-particle systems with a comprehensive set of energy functions, a variety of enhanced sampling methods, and support for multi-scale techniques including QM/MM, MM/CG, and a range of implicit solvent models.""")
    DL_POLY = PermissibleValue(
        text="DL_POLY",
        description="""DL_POLY is a general purpose classical molecular dynamics (MD) simulation software developed at Daresbury Laboratory since 1992.""")
    Desmond = PermissibleValue(
        text="Desmond",
        description="""Desmond is a software package developed at D. E. Shaw Research to perform high-speed molecular dynamics simulations of biological systems on conventional computer clusters.""")
    ACEMD = PermissibleValue(
        text="ACEMD",
        description="A software framework for molecular dynamics-based discovery.")
    CP2K = PermissibleValue(
        text="CP2K",
        description="""CP2K is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.""")

    _defn = EnumDefinition(
        name="SimulationSoftware",
        description="Simulation software used to perform molecular dynamics simulations and related functions.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "HOOMD-blue",
            PermissibleValue(
                text="HOOMD-blue",
                description="""HOOMD-blue is a Python package that runs simulations of particle systems on CPUs and GPUs."""))

class AnalysisTool(EnumDefinitionImpl):
    """
    Tools used to analyse simulation outputs.
    """
    ambpdb = PermissibleValue(
        text="ambpdb",
        description="Convert amber-format coordinate files to pdb format.")
    CPPTRAJ = PermissibleValue(
        text="CPPTRAJ",
        description="Main program in Amber for processing coordinate trajectories and data files.")
    PYTRAJ = PermissibleValue(
        text="PYTRAJ",
        description="The Python front end of cpptraj.")
    edgember = PermissibleValue(
        text="edgember",
        description="""Calculates the free energy of an alchemical transformation in 1- or 2-environments using the MBAR and thermodynamic integration methods.""")
    MoFT = PermissibleValue(
        text="MoFT",
        description="""A series of computational programs and libraries for analysis of volumentric data generated by theoretical models (MD, MC simulations, 3D-RISM, NLPB) or derived from experimental measurement (e.g X-ray crystallography, cryo-EM).""")
    ndfes = PermissibleValue(
        text="ndfes",
        description="""Program that reads an input file that describes the biased umbrella sampling, performs the variational free energy profile (vFEP), multistate Bennett acceptance ratio (MBAR), weighted thermodynamic perturbation theory (wTP), or generalized weighted thermodynamic perturbation theory (gwTP) methods to obtain an unbiased free energy surface (FES).""")
    PLUMED = PermissibleValue(
        text="PLUMED",
        description="""PLUMED is an open-source, community-developed library used in Molecular Dynamics (MD) to perform free-energy calculations, enhance sampling algorithms, and analyze simulation trajectories. It acts as a plugin or standalone engine to manipulate forces and biases on the fly.""")
    MDanalysis = PermissibleValue(
        text="MDanalysis",
        description="""MDAnalysis is an object-oriented Python library for structural and temporal analysis of molecular dynamics (MD) simulation trajectories.""")

    _defn = EnumDefinition(
        name="AnalysisTool",
        description="Tools used to analyse simulation outputs.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mdout_analyzer.py",
            PermissibleValue(
                text="mdout_analyzer.py",
                description="""A Python script designed to help parse and analyze the energy components printed in the output files from sander and pmemd."""))
        setattr(cls, "MMPBSA.py",
            PermissibleValue(
                text="MMPBSA.py",
                description="""Molecular Mechanics / Poisson Boltzmann (or Generalized Born) Surface Area (MM/PB(GB)SA) calculations is a Python-based post-processing method, where representative snapshots from an ensemble of conformations are used to calculate the free energy change between two states."""))
        setattr(cls, "Free Energy Workflow (FEW)",
            PermissibleValue(
                text="Free Energy Workflow (FEW)",
                description="""The Free Energy Workflow (FEW) is a tool for automated calculation of the binding free energy of a set of ligands binding to the same receptor using modules provided in the AMBER suite of programs."""))
        setattr(cls, "SAX-RISM",
            PermissibleValue(
                text="SAX-RISM",
                description="""Calculates small angle X-ray scattering (SAXS) from distribution function of solvent in grid format (dx files) from 3D-RISM."""))
        setattr(cls, "SAX-MD",
            PermissibleValue(
                text="SAX-MD",
                description="""Takes input as two sets of coordinates extracted from snapshots of \"sample\" and \"blank\" MD simulations (the “sample” MD contains the biomolecule plus water and ions, while the “blank” MD only has pure water + salt)."""))

class AnalysisSoftware(EnumDefinitionImpl):
    """
    Software used to analyse simulation outputs.
    """
    PyMOL = PermissibleValue(
        text="PyMOL",
        description="""PyMOL is an advanced molecular visualization and structural analysis software used extensively in biochemistry, pharmacology, and structural biology.""")
    Avogadro = PermissibleValue(
        text="Avogadro",
        description="""Avogadro is an advanced, free, and open-source 3D molecular editor and visualization tool designed for computational chemistry, bioinformatics, and materials science.""")

    _defn = EnumDefinition(
        name="AnalysisSoftware",
        description="Software used to analyse simulation outputs.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Visual Molecular Dynamics (VMD)",
            PermissibleValue(
                text="Visual Molecular Dynamics (VMD)",
                description="""VMD is a molecular visualization program for displaying, animating, and analyzing large biomolecular systems using 3-D graphics and built-in scripting."""))
        setattr(cls, "Schrödinger Maestro",
            PermissibleValue(
                text="Schrödinger Maestro",
                description="""Schrödinger Maestro is the primary graphical user interface (GUI) and workspace for the Schrödinger computational suite. It allows scientists to build, visualize, and analyze 3D molecular structures"""))

class AnalysisMethod(EnumDefinitionImpl):
    """
    Methods used to analyse simulation outputs.
    """
    RMSD = PermissibleValue(
        text="RMSD",
        description="""Calculate the root mean square deviation (RMSD) between distance pairs within selected points, perform best of fit of coordinates to a reference first.""")
    DSSP = PermissibleValue(
        text="DSSP",
        description="""Calculate the secondary structure content using the Define Secondary Structure of Proteins (DSSP) algorithm.""")
    GIST = PermissibleValue(
        text="GIST",
        description="""Perform the grid inhomogenous solvation theory (GIST), a method for analyzing the strutre and dyanmics of solvent in the vicinity of a solute molecule.""")

    _defn = EnumDefinition(
        name="AnalysisMethod",
        description="Methods used to analyse simulation outputs.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hydrogen Bonds",
            PermissibleValue(
                text="Hydrogen Bonds",
                description="Calculate hydrogen bonds using geometric criteria."))
        setattr(cls, "Connolly surface",
            PermissibleValue(
                text="Connolly surface",
                description="Calculate the Connolly surface area of specified atoms."))
        setattr(cls, "Radius of Gyration",
            PermissibleValue(
                text="Radius of Gyration",
                description="Calculate the radius of gyration for specified atoms."))
        setattr(cls, "BAR/PBSA",
            PermissibleValue(
                text="BAR/PBSA",
                description="""BAR/PBSA is a method developed to address inability of alchemical simulations to handle elecronic polarization effects upon ligand transfer from water to the protein interior. Used to post-process alchemical simulation trajectories to incorporate the polarization effects in a continuum manner."""))

class LongRangeInteractionMethod(EnumDefinitionImpl):
    """
    Method used to implement long-range interactions of point charges in the simulation.
    """
    Cutoff = PermissibleValue(
        text="Cutoff",
        description="Plain cut-off used to implement electrostatics.")
    Ewald = PermissibleValue(
        text="Ewald",
        description="""Classical Ewald sum electrostatics. Ewald scales as O(N3/2) and is thus extremely slow for large systems. In most cases PME will perform much better.""")
    PME = PermissibleValue(
        text="PME",
        description="""Particle Mesh Ewald (PME) accelerates the traditional Ewald sum by calculating reciprocal space sums on a mesh grid using fast Fourier transforms (FFTs), yielding complexity.""")
    P3M = PermissibleValue(
        text="P3M",
        description="""Particle-Particle Particle-Mesh (P3M) is faster, more flexible alternative to PME that uses a numerical particle mesh for long-range and direct summation for short-ranges.""")
    FMM = PermissibleValue(
        text="FMM",
        description="""Fast Multipole (FMM) is a highly scalable, linear complexity method that groups distant particles together, allowing the approximation of their interactions via multipole expansions.""")
    RF = PermissibleValue(
        text="RF",
        description="""Reaction Field (RF) is simpler, faster approach that approximates the effect of the long-range environment by treating it as a continuous dielectric medium beyond a certain cutoff, suitable for homogeneous systems.""")

    _defn = EnumDefinition(
        name="LongRangeInteractionMethod",
        description="Method used to implement long-range interactions of point charges in the simulation.",
    )

class IntegratorAlgorithm(EnumDefinitionImpl):
    """
    Algorithm used to integrate the simulation.
    """
    Verlet = PermissibleValue(
        text="Verlet",
        description="""A simple, stable algorithm that uses positions at a timestep and the previous timestep to calculate the next position.""")
    Euler = PermissibleValue(
        text="Euler",
        description="An Euler integrator for Brownian or position Langevin dynamics.")

    _defn = EnumDefinition(
        name="IntegratorAlgorithm",
        description="Algorithm used to integrate the simulation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Velocity-Verlet",
            PermissibleValue(
                text="Velocity-Verlet",
                description="""Directly computes positions, velocities, and accelerations at the same time, facilitating kinetic energy calculation."""))
        setattr(cls, "Leap-frog",
            PermissibleValue(
                text="Leap-frog",
                description="""Updates velocities at half-integer time steps and positions at integer time steps, equivalent to Verlet but with better velocity management."""))

class PressureCouplingType(EnumDefinitionImpl):
    """
    Coupling type for adjusting box vectors.
    """
    isotropic = PermissibleValue(
        text="isotropic",
        description="Standard for liquids; adjusts all box vectors equally.")
    anisotropic = PermissibleValue(
        text="anisotropic",
        description="Allows individual box vector scaling, often needed for solids.")

    _defn = EnumDefinition(
        name="PressureCouplingType",
        description="Coupling type for adjusting box vectors.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "semi-isotropic",
            PermissibleValue(
                text="semi-isotropic",
                description="Used for membrane simulations to allow different scaling for and axes."))
        setattr(cls, "surface tension",
            PermissibleValue(
                text="surface tension",
                description="Surface tension coupling for surfaces parallel to the xy-plane."))

class BarostatAlgorithm(EnumDefinitionImpl):
    """
    Barostat algorithm used to set the pressure in a simulation.
    """
    Berendsen = PermissibleValue(
        text="Berendsen",
        description="""Rescales the system volume and (optionally) the atoms coordinates within the simulation box every timestep via weak coupling between the internal pressure and pressure.""")
    Andersen = PermissibleValue(
        text="Andersen",
        description="""Includes an additional degree of freedom, the volume of a simulation cell. Volume adjusts itself to equalize the internal and external pressure.""")

    _defn = EnumDefinition(
        name="BarostatAlgorithm",
        description="Barostat algorithm used to set the pressure in a simulation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Parrinello-Rahman",
            PermissibleValue(
                text="Parrinello-Rahman",
                description="Extension of the Andersen method allowing changes in the shape of the simulation cell."))
        setattr(cls, "Nose-Hoover",
            PermissibleValue(
                text="Nose-Hoover",
                description="""Couples the system to a virtual \"pressure bath\" to control the simulation volume using extended Lagrangian dynamics."""))
        setattr(cls, "Monte Carlo",
            PermissibleValue(
                text="Monte Carlo",
                description="""Maintain constant pressure by periodically attempting to scale the simulation box size using random numbers."""))
        setattr(cls, "Martyna-Tuckerman-Tobias-Klein",
            PermissibleValue(
                text="Martyna-Tuckerman-Tobias-Klein",
                description="""The MTTK barostat is an extension of the Nose-Hoover and Nose-Hoover chain thermostat, acting as a modified Andersen barostat to control pressure by coupling the system to a virtual volume bath."""))

class ThermostatAlgorithm(EnumDefinitionImpl):
    """
    Thermostat algorithm used to set the temperature in a simulation.
    """
    Langevin = PermissibleValue(
        text="Langevin",
        description="""A Langevin thermostat is a molecular dynamics algorithm that maintains a constant temperature (canonical ensemble, NVT) by adding a viscous friction force and a random noise force to Newton's equations of motion. It simulates interaction with a heat bath, where the damping term removes energy and the random force inputs energy to reach equilibrium.""")
    Berendsen = PermissibleValue(
        text="Berendsen",
        description="""Rescales particle velocities by a factor at each step to bring the system toward the target temperature.""")
    Andersen = PermissibleValue(
        text="Andersen",
        description="""Stochastic approach that periodically reassigns particle velocities from a Maxwell-Boltzmann distribution, simulating collisions with a heat bath.""")
    Bussi = PermissibleValue(
        text="Bussi",
        description="""The Bussi-Donadio-Parrinello (CSVR) is a stochastic velocity rescaling thermostat that corrects the pitfalls of the Berendsen thermostat, accurately sampling the canonical ensemble while maintaining correct dynamics.""")

    _defn = EnumDefinition(
        name="ThermostatAlgorithm",
        description="Thermostat algorithm used to set the temperature in a simulation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Nose-Hoover",
            PermissibleValue(
                text="Nose-Hoover",
                description="""A deterministic method that introduces a fictitious friction variable into the system's dynamics to achieve the desired temperature (NVT ensemble)."""))

class BondLengthConstraintsAlgorithm(EnumDefinitionImpl):
    """
    Fix specific molecular degrees of freedom—typically fast bond vibrations involving hydrogen atoms. By eliminating
    these high-frequency motions, constraints allow for larger integration time steps (e.g., 2 fs instead of 0.5 fs),
    significantly speeding up simulations without disrupting system dynamics.
    """
    SHAKE = PermissibleValue(
        text="SHAKE",
        description="""An iterative method that works with the Verlet algorithm to satisfy constraints on bond lengths, ensuring the distance between mass points remains constant.""")
    RATTLE = PermissibleValue(
        text="RATTLE",
        description="""A velocity-friendly version of SHAKE used to maintain constraints in velocity Verlet integrators.""")
    SETTLE = PermissibleValue(
        text="SETTLE",
        description="""An analytical constraint algorithm used in molecular dynamics (specifically GROMACS) to maintain rigid water models (like TIP3P, TIP4P) by fixing bond lengths and angles. It is faster and more stable than iterative methods like SHAKE, operating in constant time without calculating centers of mass, reducing rounding errors.""")
    LINCS = PermissibleValue(
        text="LINCS",
        description="""LINCS (Linear Constraint Solver) is a fast, stable algorithm that breaks constraints into two steps; removing projections of new bond lengths on old bonds and correcting for bond lengthening due to rotation""")
    CCMA = PermissibleValue(
        text="CCMA",
        description="""The Constant Constraint Matrix Approximation (CCMA) is a fast, stable algorithm designed to handle geometric constraints in molecular simulations, particularly effective for macromolecules like proteins.""")

    _defn = EnumDefinition(
        name="BondLengthConstraintsAlgorithm",
        description="""Fix specific molecular degrees of freedom—typically fast bond vibrations involving hydrogen atoms. By eliminating these high-frequency motions, constraints allow for larger integration time steps (e.g., 2 fs instead of 0.5 fs), significantly speeding up simulations without disrupting system dynamics.""",
    )

class EnsembleType(EnumDefinitionImpl):
    """
    Ensemble used in a simulation
    """
    NPT = PermissibleValue(
        text="NPT",
        description="""Isothermal-isothermic ensemble (NPT) with a constant number of particles, pressure and temperature.""")
    NVT = PermissibleValue(
        text="NVT",
        description="Canonical ensemble (NVT) with a constant number of particles, volume and temperature.")
    NVE = PermissibleValue(
        text="NVE",
        description="Microcanonical ensemble (NVE) with a constant number of particles, volume and energy.")
    μVT = PermissibleValue(
        text="μVT",
        description="Grand canonical ensemble (μVT) with constant chemical potential, volume and temperature.")

    _defn = EnumDefinition(
        name="EnsembleType",
        description="Ensemble used in a simulation",
    )

class ModelResolution(EnumDefinitionImpl):
    """
    Resolution of simulated molecules.
    """
    Mesoscale = PermissibleValue(
        text="Mesoscale",
        description="Larger beads of grouped molecules represented as a single entity.")

    _defn = EnumDefinition(
        name="ModelResolution",
        description="Resolution of simulated molecules.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "All Atom",
            PermissibleValue(
                text="All Atom",
                description="All atom dynamics modelled in the simulation."))
        setattr(cls, "United Atom",
            PermissibleValue(
                text="United Atom",
                description="Treats non-polar hydrogen atoms as part of the heavier atoms they are bonded to."))
        setattr(cls, "Coarse-Grained",
            PermissibleValue(
                text="Coarse-Grained",
                description="Groups atoms into beads (often 4:1 mapping) as a single entity."))

class PeriodicBoundaryConditions(EnumDefinitionImpl):
    """
    What directions in a simulation cell periodic boundaries are set if they are turned on.
    """
    xyz = PermissibleValue(
        text="xyz",
        description="all axes")
    xy = PermissibleValue(
        text="xy",
        description="only xy plane")
    xz = PermissibleValue(
        text="xz",
        description="only xz plane")
    yz = PermissibleValue(
        text="yz",
        description="only yz plane")

    _defn = EnumDefinition(
        name="PeriodicBoundaryConditions",
        description="What directions in a simulation cell periodic boundaries are set if they are turned on.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No PBC"))

class BoxType(EnumDefinitionImpl):
    """
    Types of box used to simulate the system.
    """
    Cubic = PermissibleValue(
        text="Cubic",
        description="3D rectangular prism where all sides are equal in length")
    Tetragonal = PermissibleValue(
        text="Tetragonal",
        description="""Simulation boundaries form a rectangular prism, where two sides are equal (a = b ≠ c) and all angles are exactly 90°.""")
    Orthorhombic = PermissibleValue(
        text="Orthorhombic",
        description="""3D unit cell defined by three mutually perpendicular axes of unequal length (a ≠ b ≠ c), where all angles are exactly 90°""")
    Triclinic = PermissibleValue(
        text="Triclinic",
        description="""Non-orthogonal simulation cell defined by three arbitrary, non-coplanar vectors. Unlike standard cubic or orthorhombic boxes (which have 90° angles), triclinic boxes can have arbitrary angles and varying edge lengths to model sheared systems, complex crystal lattices, and anisotropic stress tensors""")

    _defn = EnumDefinition(
        name="BoxType",
        description="Types of box used to simulate the system.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Truncated Octahedron",
            PermissibleValue(
                text="Truncated Octahedron",
                description="""A 14-sided 3D shape (8 hexagonal and 6 square faces) used as a simulation cell in molecular dynamics. Because its geometry closely approximates a sphere, it is ideal for solvating roughly spherical or globular proteins"""))

class WaterPotentialName(EnumDefinitionImpl):
    """
    Force fields used to parametrize water molecules in a simulation.
    """
    OPC = PermissibleValue(
        text="OPC",
        description="Parameters for a water model. It is a non-polarizable, 4-point, 3-charge rigid water model.")
    OPC3 = PermissibleValue(
        text="OPC3",
        description="""Parameters for a water model. It is a 3-point rigid non-polarizable water model – as of Amber24, is the latest addition to the OPC family, constructed using the same philosophy as OPC.""")
    OPC3POL = PermissibleValue(
        text="OPC3POL",
        description="""Parameters for a water model. It is a new classical 3-point water model that explicitly accounts for electronic polarizability with minimal impact on computational efficiency.""")
    POL3 = PermissibleValue(
        text="POL3",
        description="Parameters for a water model.")
    TIP3P = PermissibleValue(
        text="TIP3P",
        description="Parameters for the force balance 3-point water model.")
    TIP3PFB = PermissibleValue(
        text="TIP3PFB",
        description="Parameters for a water model.")
    TIP4PFB = PermissibleValue(
        text="TIP4PFB",
        description="Parameters for a water model.")
    TIP4P = PermissibleValue(
        text="TIP4P",
        description="Parameters for a water model.")
    TIP5P = PermissibleValue(
        text="TIP5P",
        description="Parameters for a water model.")
    TIP4PEW = PermissibleValue(
        text="TIP4PEW",
        description="Parameters for a water model.")
    SPCE = PermissibleValue(
        text="SPCE",
        description="Parameters for a water model.")
    SPCEB = PermissibleValue(
        text="SPCEB",
        description="Parameters for a water model.")

    _defn = EnumDefinition(
        name="WaterPotentialName",
        description="Force fields used to parametrize water molecules in a simulation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SPC/Fw",
            PermissibleValue(
                text="SPC/Fw",
                description="""SPC/Fw parameters for flexible water models, for classical dynamics. Also known as SPF."""))
        setattr(cls, "q-SPC/Fw",
            PermissibleValue(
                text="q-SPC/Fw",
                description="qSPC/Fw parameters for flexible water models, for path-integral MD. Also know as SPG"))

class ProteinPotentialName(EnumDefinitionImpl):
    """
    Force fields used to parametrize amino acids in proteins in a simulation.
    """
    ff19SB = PermissibleValue(
        text="ff19SB",
        description="""As of Amber24, ff19SB is the latest model of SB protein force fields and has shown to improve amino acid-dependent properties such as helical propensities and reproduces the differences in amino acid-specific PDB Ramachandran maps.""")
    ff99SB = PermissibleValue(
        text="ff99SB",
        description="""All-atom molecular mechanics force field specifically designed to simulate proteins and peptides""")
    ff14SB = PermissibleValue(
        text="ff14SB",
        description="""Older version of the SB protein force fields that utilizes uncoupled phi/psi dihedral parameters for the protein backbone, and every amino acid except for glycine used the backbone dihedral parameters fit using alanine.""")
    ff14SBonlysc = PermissibleValue(
        text="ff14SBonlysc",
        description="""Includes the ff99SB backbone parameters with updated side chain (sc) parameters that were derived from ab initio quantum mechanics calculations.""")
    ff15ipq = PermissibleValue(
        text="ff15ipq",
        description="""Continues the development begun with the ff14ipq force field for proteins, but offers new parameter choices, data fitting and validation.""")
    fb15 = PermissibleValue(
        text="fb15",
        description="The force balance (fb) protein force field that can be used for protein-water simulations.")
    ff03 = PermissibleValue(
        text="ff03",
        description="""A modified version of ff99, where charges are derived from quantum calculations that ise a continuum dielectric to mimic solvent polarization.""")
    ff03ua = PermissibleValue(
        text="ff03ua",
        description="""The united-atom counterpart of ff03, which uses the dame charging scheme as ff03, but the aliphatic hydrogen atoms on all amino acid side-chains are united to their corresponding carbon atoms.""")
    phosaa10 = PermissibleValue(
        text="phosaa10",
        description="Force field for phosphorylated amino acids.")
    phosaa14SB = PermissibleValue(
        text="phosaa14SB",
        description="Force field for phosphorylated amino acids with ff14SB.")
    phosaa19SB = PermissibleValue(
        text="phosaa19SB",
        description="Force field for phosphorylated amino acids with ff19SB.")
    ff14SB_modAA = PermissibleValue(
        text="ff14SB_modAA",
        description="""Force field with ff14SB for modified amino acids like selenomethionine, cyano-phenylalanine, and azido-phenylalanine, acetylated lysine and for the nitroxide spin-label methanesulfonothioate (MTSL).""")
    ff19SB_modAA = PermissibleValue(
        text="ff19SB_modAA",
        description="""Force field with ff19SB for modified amino acids like selenomethionine, cyano-phenylalanine, and azido-phenylalanine, acetylated lysine and for the nitroxide spin-label methanesulfonothioate (MTSL).""")

    _defn = EnumDefinition(
        name="ProteinPotentialName",
        description="Force fields used to parametrize amino acids in proteins in a simulation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ff99SB-ILDN",
            PermissibleValue(
                text="ff99SB-ILDN",
                description="""Refined extension of the foundational Amber ff99SB model, specifically optimized to fix errors in side-chain rotamer distributions."""))
        setattr(cls, "ff99SB-disp",
            PermissibleValue(
                text="ff99SB-disp",
                description="""Optimized by D.E. Shaw Research to accurately simulate both folded, structured proteins and intrinsically disordered proteins (IDPs) or highly flexible peptide states."""))

class NucleicPotentialName(EnumDefinitionImpl):
    """
    Force fields used to parametrize nucleic acids in a simulation.
    """
    ff99OL3 = PermissibleValue(
        text="ff99OL3",
        description="""Force field for RNA, where quantum mechanics methods at various levels were employed to improve the chi angle distribution using relevant model systems.""")
    LJbb = PermissibleValue(
        text="LJbb",
        description="""RNA force field with modified phosphate parameters (from OL force field) and an improved water model (OPC), which has better agreement with NMR data for RNA tetranucleotide populations.""")
    ROC = PermissibleValue(
        text="ROC",
        description="Force field with alternative set of torsions for RNA, fit to quantum calculations.")
    Shaw = PermissibleValue(
        text="Shaw",
        description="RNA force field with more extensive modifications.")
    OL15 = PermissibleValue(
        text="OL15",
        description="Force field for DNA, with a combination of three dihedral updates.")
    OL21 = PermissibleValue(
        text="OL21",
        description="""DNA force field that adds some new torsion modifications, aimed at non-B double helices, as of Amber24, is the current recommended DNA force field.""")
    OL24 = PermissibleValue(
        text="OL24",
        description="OL24 is a 2024 DNA force field tested on both canonical and non-canonical DNA.")
    OL3 = PermissibleValue(
        text="OL3",
        description="The Amber OL3 force field is a parameter set for simulations of RNA.")
    bsc1 = PermissibleValue(
        text="bsc1",
        description="""Updated version of bsc0 force field for DNA, using an implicit solvation model and a rigorous quantum mechanics methodology.""")
    terminal_monophosphate = PermissibleValue(
        text="terminal_monophosphate",
        description="""Force field library for the 5\’ end of many DNA and RNA chains have one or more phosphate groups.""")

    _defn = EnumDefinition(
        name="NucleicPotentialName",
        description="Force fields used to parametrize nucleic acids in a simulation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ff99-bsc0",
            PermissibleValue(
                text="ff99-bsc0",
                description="""Force field for nucliec acids. High level quantum mechanics calculations were perfomed on models of sugars and phosphates, specifically a sugar-phosphate model and a sugar-phosphate-sugar model."""))

class CarbohydratePotentialName(EnumDefinitionImpl):
    """
    Force fields used to parametrize carbohydrates in a simulation.
    """
    GLYCAM06 = PermissibleValue(
        text="GLYCAM06",
        description="Parameter set for modeling carbohydrates and glycoconjugates.")
    GLYCAM_06EP = PermissibleValue(
        text="GLYCAM_06EP",
        description="""GLYCAM-06EP parameter set for modeling carbohydrates and glycoconjugates. Extends GLYCAM to simulations employing the TIP-5P water model, an additional set of carbohydrate parameters, GLYCAM-06EP.""")

    _defn = EnumDefinition(
        name="CarbohydratePotentialName",
        description="Force fields used to parametrize carbohydrates in a simulation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "GLYCAM_06j-1",
            PermissibleValue(
                text="GLYCAM_06j-1",
                description="""An empirical biomolecular force field designed primarily for carbohydrates and complex glycans."""))

class LipidPotentialName(EnumDefinitionImpl):
    """
    Force fields used to parametrize lipids in a simulation.
    """
    LIPID21 = PermissibleValue(
        text="LIPID21",
        description="""An Amber lipid force field building on the modular nature of LIPID11, LIPID 14 and LIPID 17 to allow for tensionless lipid bilayer simulations in Amber.""")

    _defn = EnumDefinition(
        name="LipidPotentialName",
        description="Force fields used to parametrize lipids in a simulation.",
    )

class PolymerPotentialName(EnumDefinitionImpl):
    """
    Force fields used to parametrize polymers in a simulation.
    """
    LignAmb25 = PermissibleValue(
        text="LignAmb25",
        description="""Force field that includes parameters for all common monolignol units and their associated linkages along with less commonly encountered units.""")

    _defn = EnumDefinition(
        name="PolymerPotentialName",
        description="Force fields used to parametrize polymers in a simulation.",
    )

class GeneralPotentialName(EnumDefinitionImpl):
    """
    Force fields used to parametrize molecules in a simulation.
    """
    GAFF = PermissibleValue(
        text="GAFF",
        description="""Provides parameters for small molecules and drug-like ligands that are fully compatible with standard macromolecular AMBER force fields used for proteins and nucleic acids.""")
    GAFF2 = PermissibleValue(
        text="GAFF2",
        description="The second generation of GAFF for small molecules and drug-like ligands.")
    OPLS = PermissibleValue(
        text="OPLS",
        description="""OPLS (Optimized Potential for Liquid Simulations) is a set of force fields developed by Prof. William L. Jorgensen for condensed phase simulations.""")
    GROMOS = PermissibleValue(
        text="GROMOS",
        description="""GROMOS is is a general-purpose molecular dynamics computer simulation package for the study of biomolecular systems. It also incorporates its own force field covering proteins, nucleotides, sugars etc. and can be applied to chemical and physical systems ranging from glasses and liquid crystals, to polymers and crystals and solutions of biomolecules.""")
    CHARMM = PermissibleValue(
        text="CHARMM",
        description="""CHARMM (Chemistry at HARvard Macromolecular Mechanics) is a both a set of force fields and a software package for molecular dynamics simulations and analysis. Includes united atom (CHARMM19) and all atom (CHARMM22, CHARMM27, CHARMM36) force fields.""")

    _defn = EnumDefinition(
        name="GeneralPotentialName",
        description="Force fields used to parametrize molecules in a simulation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "gem.pmemd",
            PermissibleValue(
                text="gem.pmemd",
                description="""The Amoeba force field in a multiploar/polarizable force field with parameters for water, univalent ions, small organic molecules, proteins, nucliec acids and ionic liquids."""))

class MachineLearnedPotentialName(EnumDefinitionImpl):
    """
    Machine learned potentials.
    """
    MACE = PermissibleValue(
        text="MACE",
        description="""Utilizes high-body-order expansions and provides exceptional force accuracy, excelling at capturing anharmonic dynamics in organic and macromolecular systems.""")
    ANI = PermissibleValue(
        text="ANI",
        description="""Neural network potentials specifically parameterized for organic and small-molecule drug-like spaces (covering H, C, N, O).""")
    NequIP = PermissibleValue(
        text="NequIP",
        description="E(3)-equivariant network that models local atomic environments as tensors.")
    UMA = PermissibleValue(
        text="UMA",
        description="""Large-scale framework spanning half a billion atomic structures, and generalizes across different chemical environments.""")
    AceFF = PermissibleValue(
        text="AceFF",
        description="Specifically optimized for small molecule drug discovery")

    _defn = EnumDefinition(
        name="MachineLearnedPotentialName",
        description="Machine learned potentials.",
    )

class OperatingSystem(EnumDefinitionImpl):
    """
    List of operating systems installed on the hardware used to perform the simulation.
    """
    Linux = PermissibleValue(
        text="Linux",
        description="""Unix-like operating systems commonly used for molecular dynamics on workstations, HPC clusters, and cloud environments.""")
    macOS = PermissibleValue(
        text="macOS",
        description="""Apple Unix-based operating system, often used for local development, testing, and smaller-scale molecular dynamics workflows.""")
    Windows = PermissibleValue(
        text="Windows",
        description="""Microsoft operating system used for desktop workflows; molecular dynamics tools are often run via native builds, virtual machines, or Linux compatibility layers.""")

    _defn = EnumDefinition(
        name="OperatingSystem",
        description="List of operating systems installed on the hardware used to perform the simulation.",
    )

class Scheduler(EnumDefinitionImpl):
    """
    Job scheduler used for simulation execution.
    """
    SLURM = PermissibleValue(
        text="SLURM",
        description="Slurm Workload Manager.")
    PBS = PermissibleValue(
        text="PBS",
        description="Portable Batch System family (PBS Pro/OpenPBS).")
    LSF = PermissibleValue(
        text="LSF",
        description="IBM Spectrum LSF.")
    SGE = PermissibleValue(
        text="SGE",
        description="Sun/Grid Engine family.")

    _defn = EnumDefinition(
        name="Scheduler",
        description="Job scheduler used for simulation execution.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No batch scheduler used."))

class MPILibrary(EnumDefinitionImpl):
    """
    MPI implementation used for message passing.
    """
    OpenMPI = PermissibleValue(
        text="OpenMPI",
        description="Open source MPI implementation.")
    MPICH = PermissibleValue(
        text="MPICH",
        description="MPICH MPI implementation.")
    IntelMPI = PermissibleValue(
        text="IntelMPI",
        description="Intel MPI implementation.")
    MVAPICH2 = PermissibleValue(
        text="MVAPICH2",
        description="MVAPICH2 MPI implementation.")

    _defn = EnumDefinition(
        name="MPILibrary",
        description="MPI implementation used for message passing.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No MPI library used."))

class ContainerRuntime(EnumDefinitionImpl):
    """
    Container runtime used to package and run software.
    """
    Apptainer = PermissibleValue(
        text="Apptainer",
        description="Apptainer/Singularity runtime common on HPC systems.")
    Docker = PermissibleValue(
        text="Docker",
        description="Docker container runtime.")
    Podman = PermissibleValue(
        text="Podman",
        description="Podman container runtime.")

    _defn = EnumDefinition(
        name="ContainerRuntime",
        description="Container runtime used to package and run software.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No container runtime used."))

class ExecutionPlatform(EnumDefinitionImpl):
    """
    Type of platform used to run the simulation.
    """
    Local = PermissibleValue(
        text="Local",
        description="Local desktop, laptop or portable workstation.")

    _defn = EnumDefinition(
        name="ExecutionPlatform",
        description="Type of platform used to run the simulation.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "HPC Cluster",
            PermissibleValue(
                text="HPC Cluster",
                description="Shared high-performance computing cluster."))
        setattr(cls, "Cloud VM",
            PermissibleValue(
                text="Cloud VM",
                description="Cloud-hosted virtual machine."))

class NodeType(EnumDefinitionImpl):
    """
    Type of compute node used in the system.
    """
    _defn = EnumDefinition(
        name="NodeType",
        description="Type of compute node used in the system.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CPU only",
            PermissibleValue(
                text="CPU only",
                description="Node with CPUs only."))
        setattr(cls, "GPU Accelerated",
            PermissibleValue(
                text="GPU Accelerated",
                description="Node with one or more GPUs available."))
        setattr(cls, "Hybrid CPU GPU",
            PermissibleValue(
                text="Hybrid CPU GPU",
                description="Node combining CPU and GPU resources."))

class CpuVendor(EnumDefinitionImpl):
    """
    Vendor of the CPU used in the compute nodes.
    """
    AMD = PermissibleValue(
        text="AMD",
        description="AMD processor.")
    Intel = PermissibleValue(
        text="Intel",
        description="Intel processor.")
    ARM = PermissibleValue(
        text="ARM",
        description="ARM-based processor.")
    Other = PermissibleValue(
        text="Other",
        description="Other CPU vendor.")

    _defn = EnumDefinition(
        name="CpuVendor",
        description="Vendor of the CPU used in the compute nodes.",
    )

class CpuArchitecture(EnumDefinitionImpl):
    """
    CPU architecture used by the compute nodes.
    """
    x86 = PermissibleValue(
        text="x86",
        description="x86 architecture.")
    ARM = PermissibleValue(
        text="ARM",
        description="ARM architecture.")

    _defn = EnumDefinition(
        name="CpuArchitecture",
        description="CPU architecture used by the compute nodes.",
    )

class GpuVendor(EnumDefinitionImpl):
    """
    Vendor of the GPU used in the compute nodes.
    """
    Nvidia = PermissibleValue(
        text="Nvidia",
        description="Nvidia GPU.")
    AMD = PermissibleValue(
        text="AMD",
        description="AMD GPU.")
    Intel = PermissibleValue(
        text="Intel",
        description="Intel GPU.")

    _defn = EnumDefinition(
        name="GpuVendor",
        description="Vendor of the GPU used in the compute nodes.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No GPU present."))

class FileHashAlgorithm(EnumDefinitionImpl):

    sha256 = PermissibleValue(text="sha256")
    md5 = PermissibleValue(text="md5")

    _defn = EnumDefinition(
        name="FileHashAlgorithm",
    )

class FileRole(EnumDefinitionImpl):

    topology = PermissibleValue(text="topology")
    trajectory = PermissibleValue(text="trajectory")
    metadata = PermissibleValue(text="metadata")
    log = PermissibleValue(text="log")
    parameter = PermissibleValue(text="parameter")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="FileRole",
    )

# Slots
class slots:
    pass

slots.stages = Slot(uri=BIOSIM_SCHEMA.stages, name="stages", curie=BIOSIM_SCHEMA.curie('stages'),
                   model_uri=BIOSIM_SCHEMA.stages, domain=None, range=Optional[Union[dict, SimulationStages]])

slots.settings = Slot(uri=BIOSIM_SCHEMA.settings, name="settings", curie=BIOSIM_SCHEMA.curie('settings'),
                   model_uri=BIOSIM_SCHEMA.settings, domain=None, range=Optional[Union[dict, SimulationSettings]])

slots.composition = Slot(uri=BIOSIM_SCHEMA.composition, name="composition", curie=BIOSIM_SCHEMA.curie('composition'),
                   model_uri=BIOSIM_SCHEMA.composition, domain=None, range=Optional[Union[dict, SystemComposition]])

slots.observables = Slot(uri=BIOSIM_SCHEMA.observables, name="observables", curie=BIOSIM_SCHEMA.curie('observables'),
                   model_uri=BIOSIM_SCHEMA.observables, domain=None, range=Optional[Union[dict, SimulationObservables]])

slots.topology = Slot(uri=BIOSIM_SCHEMA.topology, name="topology", curie=BIOSIM_SCHEMA.curie('topology'),
                   model_uri=BIOSIM_SCHEMA.topology, domain=None, range=Optional[Union[dict, TopologyMetadata]])

slots.trajectory = Slot(uri=BIOSIM_SCHEMA.trajectory, name="trajectory", curie=BIOSIM_SCHEMA.curie('trajectory'),
                   model_uri=BIOSIM_SCHEMA.trajectory, domain=None, range=Optional[Union[dict, TrajectoryMetadata]])

slots.potentials = Slot(uri=BIOSIM_SCHEMA.potentials, name="potentials", curie=BIOSIM_SCHEMA.curie('potentials'),
                   model_uri=BIOSIM_SCHEMA.potentials, domain=None, range=Optional[Union[dict, PotentialMetadata]])

slots.compute = Slot(uri=BIOSIM_SCHEMA.compute, name="compute", curie=BIOSIM_SCHEMA.curie('compute'),
                   model_uri=BIOSIM_SCHEMA.compute, domain=None, range=Optional[Union[dict, ComputationalEnvironment]])

slots.files = Slot(uri=BIOSIM_SCHEMA.files, name="files", curie=BIOSIM_SCHEMA.curie('files'),
                   model_uri=BIOSIM_SCHEMA.files, domain=None, range=Optional[Union[Union[dict, FileMetadata], list[Union[dict, FileMetadata]]]])

slots.engine_mapping = Slot(uri=BIOSIM_SCHEMA.engine_mapping, name="engine_mapping", curie=BIOSIM_SCHEMA.curie('engine_mapping'),
                   model_uri=BIOSIM_SCHEMA.engine_mapping, domain=None, range=Optional[Union[str, list[str]]])

slots.value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.value, domain=None, range=Optional[float])

slots.value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.value_unit, domain=None, range=Optional[str])

slots.vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.vector_value, domain=None, range=Optional[str])

slots.setup = Slot(uri=BIOSIM_SCHEMA['stages/setup'], name="setup", curie=BIOSIM_SCHEMA.curie('stages/setup'),
                   model_uri=BIOSIM_SCHEMA.setup, domain=None, range=Optional[Union[dict, Setup]])

slots.minimisation = Slot(uri=BIOSIM_SCHEMA['stages/minimisation'], name="minimisation", curie=BIOSIM_SCHEMA.curie('stages/minimisation'),
                   model_uri=BIOSIM_SCHEMA.minimisation, domain=None, range=Optional[Union[dict, Minimisation]])

slots.number_of_minimisation_steps = Slot(uri=BIOSIM_SCHEMA['stages/number_of_minimisation_steps'], name="number_of_minimisation_steps", curie=BIOSIM_SCHEMA.curie('stages/number_of_minimisation_steps'),
                   model_uri=BIOSIM_SCHEMA.number_of_minimisation_steps, domain=None, range=Optional[int])

slots.equilibration = Slot(uri=BIOSIM_SCHEMA['stages/equilibration'], name="equilibration", curie=BIOSIM_SCHEMA.curie('stages/equilibration'),
                   model_uri=BIOSIM_SCHEMA.equilibration, domain=None, range=Optional[Union[dict, Equilibration]])

slots.production = Slot(uri=BIOSIM_SCHEMA['stages/production'], name="production", curie=BIOSIM_SCHEMA.curie('stages/production'),
                   model_uri=BIOSIM_SCHEMA.production, domain=None, range=Optional[Union[dict, Production]])

slots.analysis = Slot(uri=BIOSIM_SCHEMA['stages/analysis'], name="analysis", curie=BIOSIM_SCHEMA.curie('stages/analysis'),
                   model_uri=BIOSIM_SCHEMA.analysis, domain=None, range=Optional[Union[dict, Analysis]])

slots.setup_tool = Slot(uri=BIOSIM_SCHEMA['stages/setup_tool'], name="setup_tool", curie=BIOSIM_SCHEMA.curie('stages/setup_tool'),
                   model_uri=BIOSIM_SCHEMA.setup_tool, domain=None, range=Optional[Union[str, "SetupTool"]])

slots.energy_tolerance = Slot(uri=BIOSIM_SCHEMA['stages/energy_tolerance'], name="energy_tolerance", curie=BIOSIM_SCHEMA.curie('stages/energy_tolerance'),
                   model_uri=BIOSIM_SCHEMA.energy_tolerance, domain=None, range=Optional[Union[dict, ForceQuantity]])

slots.minimisation_distance_step_size = Slot(uri=BIOSIM_SCHEMA['stages/minimisation_distance_step_size'], name="minimisation_distance_step_size", curie=BIOSIM_SCHEMA.curie('stages/minimisation_distance_step_size'),
                   model_uri=BIOSIM_SCHEMA.minimisation_distance_step_size, domain=None, range=Optional[Union[dict, LengthQuantity]])

slots.minimisation_algorithm = Slot(uri=BIOSIM_SCHEMA['stages/minimisation_algorithm'], name="minimisation_algorithm", curie=BIOSIM_SCHEMA.curie('stages/minimisation_algorithm'),
                   model_uri=BIOSIM_SCHEMA.minimisation_algorithm, domain=None, range=Optional[Union[Union[str, "MinimisationAlgorithm"], list[Union[str, "MinimisationAlgorithm"]]]])

slots.simulation_software = Slot(uri=BIOSIM_SCHEMA['stages/simulation_software'], name="simulation_software", curie=BIOSIM_SCHEMA.curie('stages/simulation_software'),
                   model_uri=BIOSIM_SCHEMA.simulation_software, domain=None, range=Optional[Union[Union[str, "SimulationSoftware"], list[Union[str, "SimulationSoftware"]]]])

slots.simulation_software_version = Slot(uri=BIOSIM_SCHEMA['stages/simulation_software_version'], name="simulation_software_version", curie=BIOSIM_SCHEMA.curie('stages/simulation_software_version'),
                   model_uri=BIOSIM_SCHEMA.simulation_software_version, domain=None, range=Optional[str])

slots.simulation_method = Slot(uri=BIOSIM_SCHEMA['stages/simulation_method'], name="simulation_method", curie=BIOSIM_SCHEMA.curie('stages/simulation_method'),
                   model_uri=BIOSIM_SCHEMA.simulation_method, domain=None, range=Optional[Union[Union[str, "SimulationMethod"], list[Union[str, "SimulationMethod"]]]])

slots.simulation_tool = Slot(uri=BIOSIM_SCHEMA['stages/simulation_tool'], name="simulation_tool", curie=BIOSIM_SCHEMA.curie('stages/simulation_tool'),
                   model_uri=BIOSIM_SCHEMA.simulation_tool, domain=None, range=Optional[Union[Union[str, "SimulationTool"], list[Union[str, "SimulationTool"]]]])

slots.analysis_software = Slot(uri=BIOSIM_SCHEMA['stages/analysis_software'], name="analysis_software", curie=BIOSIM_SCHEMA.curie('stages/analysis_software'),
                   model_uri=BIOSIM_SCHEMA.analysis_software, domain=None, range=Optional[Union[Union[str, "AnalysisSoftware"], list[Union[str, "AnalysisSoftware"]]]])

slots.analysis_method = Slot(uri=BIOSIM_SCHEMA['stages/analysis_method'], name="analysis_method", curie=BIOSIM_SCHEMA.curie('stages/analysis_method'),
                   model_uri=BIOSIM_SCHEMA.analysis_method, domain=None, range=Optional[Union[Union[str, "AnalysisMethod"], list[Union[str, "AnalysisMethod"]]]])

slots.analysis_tool = Slot(uri=BIOSIM_SCHEMA['stages/analysis_tool'], name="analysis_tool", curie=BIOSIM_SCHEMA.curie('stages/analysis_tool'),
                   model_uri=BIOSIM_SCHEMA.analysis_tool, domain=None, range=Optional[Union[Union[str, "AnalysisTool"], list[Union[str, "AnalysisTool"]]]])

slots.ensemble = Slot(uri=BIOSIM_SCHEMA['settings/ensemble'], name="ensemble", curie=BIOSIM_SCHEMA.curie('settings/ensemble'),
                   model_uri=BIOSIM_SCHEMA.ensemble, domain=None, range=Optional[Union[dict, Ensemble]])

slots.interactions = Slot(uri=BIOSIM_SCHEMA['settings/interactions'], name="interactions", curie=BIOSIM_SCHEMA.curie('settings/interactions'),
                   model_uri=BIOSIM_SCHEMA.interactions, domain=None, range=Optional[Union[dict, Interactions]])

slots.integrator = Slot(uri=BIOSIM_SCHEMA['settings/integrator'], name="integrator", curie=BIOSIM_SCHEMA.curie('settings/integrator'),
                   model_uri=BIOSIM_SCHEMA.integrator, domain=None, range=Optional[Union[dict, Integrator]])

slots.barostat = Slot(uri=BIOSIM_SCHEMA['settings/barostat'], name="barostat", curie=BIOSIM_SCHEMA.curie('settings/barostat'),
                   model_uri=BIOSIM_SCHEMA.barostat, domain=None, range=Optional[Union[dict, Barostat]])

slots.thermostat = Slot(uri=BIOSIM_SCHEMA['settings/thermostat'], name="thermostat", curie=BIOSIM_SCHEMA.curie('settings/thermostat'),
                   model_uri=BIOSIM_SCHEMA.thermostat, domain=None, range=Optional[Union[dict, Thermostat]])

slots.time_step = Slot(uri=BIOSIM_SCHEMA['settings/time_step'], name="time_step", curie=BIOSIM_SCHEMA.curie('settings/time_step'),
                   model_uri=BIOSIM_SCHEMA.time_step, domain=None, range=Optional[Union[dict, TimeQuantity]])

slots.frame_step = Slot(uri=BIOSIM_SCHEMA['settings/frame_step'], name="frame_step", curie=BIOSIM_SCHEMA.curie('settings/frame_step'),
                   model_uri=BIOSIM_SCHEMA.frame_step, domain=None, range=Optional[Union[dict, TimeQuantity]])

slots.number_of_steps = Slot(uri=BIOSIM_SCHEMA['settings/number_of_steps'], name="number_of_steps", curie=BIOSIM_SCHEMA.curie('settings/number_of_steps'),
                   model_uri=BIOSIM_SCHEMA.number_of_steps, domain=None, range=Optional[int])

slots.simulation_time = Slot(uri=BIOSIM_SCHEMA['settings/simulation_time'], name="simulation_time", curie=BIOSIM_SCHEMA.curie('settings/simulation_time'),
                   model_uri=BIOSIM_SCHEMA.simulation_time, domain=None, range=Optional[Union[dict, TimeQuantity]])

slots.restraints = Slot(uri=BIOSIM_SCHEMA['settings/restraints'], name="restraints", curie=BIOSIM_SCHEMA.curie('settings/restraints'),
                   model_uri=BIOSIM_SCHEMA.restraints, domain=None, range=Optional[Union[bool, Bool]])

slots.integrator_algorithm = Slot(uri=BIOSIM_SCHEMA['settings/integrator_algorithm'], name="integrator_algorithm", curie=BIOSIM_SCHEMA.curie('settings/integrator_algorithm'),
                   model_uri=BIOSIM_SCHEMA.integrator_algorithm, domain=None, range=Optional[Union[str, "IntegratorAlgorithm"]])

slots.barostat_algorithm = Slot(uri=BIOSIM_SCHEMA['settings/barostat_algorithm'], name="barostat_algorithm", curie=BIOSIM_SCHEMA.curie('settings/barostat_algorithm'),
                   model_uri=BIOSIM_SCHEMA.barostat_algorithm, domain=None, range=Optional[Union[str, "BarostatAlgorithm"]])

slots.pressure_coupling_type = Slot(uri=BIOSIM_SCHEMA['settings/pressure_coupling_type'], name="pressure_coupling_type", curie=BIOSIM_SCHEMA.curie('settings/pressure_coupling_type'),
                   model_uri=BIOSIM_SCHEMA.pressure_coupling_type, domain=None, range=Optional[Union[str, "PressureCouplingType"]])

slots.pressure_coupling_frequency = Slot(uri=BIOSIM_SCHEMA['settings/pressure_coupling_frequency'], name="pressure_coupling_frequency", curie=BIOSIM_SCHEMA.curie('settings/pressure_coupling_frequency'),
                   model_uri=BIOSIM_SCHEMA.pressure_coupling_frequency, domain=None, range=Optional[Union[dict, FrequencyQuantity]])

slots.thermostat_algorithm = Slot(uri=BIOSIM_SCHEMA['settings/thermostat_algorithm'], name="thermostat_algorithm", curie=BIOSIM_SCHEMA.curie('settings/thermostat_algorithm'),
                   model_uri=BIOSIM_SCHEMA.thermostat_algorithm, domain=None, range=Optional[Union[str, "ThermostatAlgorithm"]])

slots.ensemble_type = Slot(uri=BIOSIM_SCHEMA['settings/ensemble_type'], name="ensemble_type", curie=BIOSIM_SCHEMA.curie('settings/ensemble_type'),
                   model_uri=BIOSIM_SCHEMA.ensemble_type, domain=None, range=Optional[Union[str, "EnsembleType"]])

slots.random_seed = Slot(uri=BIOSIM_SCHEMA['settings/random_seed'], name="random_seed", curie=BIOSIM_SCHEMA.curie('settings/random_seed'),
                   model_uri=BIOSIM_SCHEMA.random_seed, domain=None, range=Optional[int])

slots.temperature_time_constant = Slot(uri=BIOSIM_SCHEMA['settings/temperature_time_constant'], name="temperature_time_constant", curie=BIOSIM_SCHEMA.curie('settings/temperature_time_constant'),
                   model_uri=BIOSIM_SCHEMA.temperature_time_constant, domain=None, range=Optional[Union[dict, VectorTimeQuantity]])

slots.coupling_group = Slot(uri=BIOSIM_SCHEMA['settings/coupling_group'], name="coupling_group", curie=BIOSIM_SCHEMA.curie('settings/coupling_group'),
                   model_uri=BIOSIM_SCHEMA.coupling_group, domain=None, range=Optional[str])

slots.chain_length = Slot(uri=BIOSIM_SCHEMA['settings/chain_length'], name="chain_length", curie=BIOSIM_SCHEMA.curie('settings/chain_length'),
                   model_uri=BIOSIM_SCHEMA.chain_length, domain=None, range=Optional[int])

slots.friction_coefficient = Slot(uri=BIOSIM_SCHEMA['settings/friction_coefficient'], name="friction_coefficient", curie=BIOSIM_SCHEMA.curie('settings/friction_coefficient'),
                   model_uri=BIOSIM_SCHEMA.friction_coefficient, domain=None, range=Optional[Union[dict, FrictionCoefficientQuantity]])

slots.collision_frequency = Slot(uri=BIOSIM_SCHEMA['settings/collision_frequency'], name="collision_frequency", curie=BIOSIM_SCHEMA.curie('settings/collision_frequency'),
                   model_uri=BIOSIM_SCHEMA.collision_frequency, domain=None, range=Optional[Union[dict, FrequencyQuantity]])

slots.target_temperature = Slot(uri=BIOSIM_SCHEMA['settings/target_temperature'], name="target_temperature", curie=BIOSIM_SCHEMA.curie('settings/target_temperature'),
                   model_uri=BIOSIM_SCHEMA.target_temperature, domain=None, range=Optional[Union[dict, TemperatureQuantity]])

slots.target_temperature_vector = Slot(uri=BIOSIM_SCHEMA['settings/target_temperature_vector'], name="target_temperature_vector", curie=BIOSIM_SCHEMA.curie('settings/target_temperature_vector'),
                   model_uri=BIOSIM_SCHEMA.target_temperature_vector, domain=None, range=Optional[Union[dict, VectorTemperatureQuantity]])

slots.target_pressure_vector = Slot(uri=BIOSIM_SCHEMA['settings/target_pressure_vector'], name="target_pressure_vector", curie=BIOSIM_SCHEMA.curie('settings/target_pressure_vector'),
                   model_uri=BIOSIM_SCHEMA.target_pressure_vector, domain=None, range=Optional[Union[dict, MatrixPressureQuantity]])

slots.target_pressure = Slot(uri=BIOSIM_SCHEMA['settings/target_pressure'], name="target_pressure", curie=BIOSIM_SCHEMA.curie('settings/target_pressure'),
                   model_uri=BIOSIM_SCHEMA.target_pressure, domain=None, range=Optional[Union[dict, PressureQuantity]])

slots.compressibility_vector = Slot(uri=BIOSIM_SCHEMA['settings/compressibility_vector'], name="compressibility_vector", curie=BIOSIM_SCHEMA.curie('settings/compressibility_vector'),
                   model_uri=BIOSIM_SCHEMA.compressibility_vector, domain=None, range=Optional[Union[dict, MatrixCompressibilityQuantity]])

slots.compressibility = Slot(uri=BIOSIM_SCHEMA['settings/compressibility'], name="compressibility", curie=BIOSIM_SCHEMA.curie('settings/compressibility'),
                   model_uri=BIOSIM_SCHEMA.compressibility, domain=None, range=Optional[Union[dict, CompressibilityQuantity]])

slots.pressure_time_constant = Slot(uri=BIOSIM_SCHEMA['settings/pressure_time_constant'], name="pressure_time_constant", curie=BIOSIM_SCHEMA.curie('settings/pressure_time_constant'),
                   model_uri=BIOSIM_SCHEMA.pressure_time_constant, domain=None, range=Optional[Union[dict, TimeQuantity]])

slots.bond_length_constraints_algorithm = Slot(uri=BIOSIM_SCHEMA['settings/bond_length_constraints_algorithm'], name="bond_length_constraints_algorithm", curie=BIOSIM_SCHEMA.curie('settings/bond_length_constraints_algorithm'),
                   model_uri=BIOSIM_SCHEMA.bond_length_constraints_algorithm, domain=None, range=Optional[Union[str, "BondLengthConstraintsAlgorithm"]])

slots.electrostatic_cutoff_distance = Slot(uri=BIOSIM_SCHEMA['settings/electrostatic_cutoff_distance'], name="electrostatic_cutoff_distance", curie=BIOSIM_SCHEMA.curie('settings/electrostatic_cutoff_distance'),
                   model_uri=BIOSIM_SCHEMA.electrostatic_cutoff_distance, domain=None, range=Optional[Union[dict, LengthQuantity]])

slots.vdw_cutoff_distance = Slot(uri=BIOSIM_SCHEMA['settings/vdw_cutoff_distance'], name="vdw_cutoff_distance", curie=BIOSIM_SCHEMA.curie('settings/vdw_cutoff_distance'),
                   model_uri=BIOSIM_SCHEMA.vdw_cutoff_distance, domain=None, range=Optional[Union[dict, LengthQuantity]])

slots.long_range_interaction_method = Slot(uri=BIOSIM_SCHEMA['settings/long_range_interaction_method'], name="long_range_interaction_method", curie=BIOSIM_SCHEMA.curie('settings/long_range_interaction_method'),
                   model_uri=BIOSIM_SCHEMA.long_range_interaction_method, domain=None, range=Optional[Union[str, "LongRangeInteractionMethod"]])

slots.salt_concentration = Slot(uri=BIOSIM_SCHEMA['composition/salt_concentration'], name="salt_concentration", curie=BIOSIM_SCHEMA.curie('composition/salt_concentration'),
                   model_uri=BIOSIM_SCHEMA.salt_concentration, domain=None, range=Optional[Union[dict, ConcentrationQuantity]])

slots.total_atom_count = Slot(uri=BIOSIM_SCHEMA['composition/total_atom_count'], name="total_atom_count", curie=BIOSIM_SCHEMA.curie('composition/total_atom_count'),
                   model_uri=BIOSIM_SCHEMA.total_atom_count, domain=None, range=Optional[int])

slots.total_molecule_count = Slot(uri=BIOSIM_SCHEMA['composition/total_molecule_count'], name="total_molecule_count", curie=BIOSIM_SCHEMA.curie('composition/total_molecule_count'),
                   model_uri=BIOSIM_SCHEMA.total_molecule_count, domain=None, range=Optional[int])

slots.atom_count = Slot(uri=BIOSIM_SCHEMA['composition/atom_count'], name="atom_count", curie=BIOSIM_SCHEMA.curie('composition/atom_count'),
                   model_uri=BIOSIM_SCHEMA.atom_count, domain=None, range=Optional[int])

slots.molecule_count = Slot(uri=BIOSIM_SCHEMA['composition/molecule_count'], name="molecule_count", curie=BIOSIM_SCHEMA.curie('composition/molecule_count'),
                   model_uri=BIOSIM_SCHEMA.molecule_count, domain=None, range=Optional[int])

slots.monomer_count = Slot(uri=BIOSIM_SCHEMA['composition/monomer_count'], name="monomer_count", curie=BIOSIM_SCHEMA.curie('composition/monomer_count'),
                   model_uri=BIOSIM_SCHEMA.monomer_count, domain=None, range=Optional[int])

slots.molecular_weight = Slot(uri=BIOSIM_SCHEMA['composition/molecular_weight'], name="molecular_weight", curie=BIOSIM_SCHEMA.curie('composition/molecular_weight'),
                   model_uri=BIOSIM_SCHEMA.molecular_weight, domain=None, range=Optional[Union[dict, MassQuantity]])

slots.molecule_charge = Slot(uri=BIOSIM_SCHEMA['composition/molecule_charge'], name="molecule_charge", curie=BIOSIM_SCHEMA.curie('composition/molecule_charge'),
                   model_uri=BIOSIM_SCHEMA.molecule_charge, domain=None, range=Optional[Union[dict, ChargeQuantity]],
                   pattern=re.compile(r'^[+-]?\d+(\.\d+)?$'))

slots.unique_molecule_count = Slot(uri=BIOSIM_SCHEMA['composition/unique_molecule_count'], name="unique_molecule_count", curie=BIOSIM_SCHEMA.curie('composition/unique_molecule_count'),
                   model_uri=BIOSIM_SCHEMA.unique_molecule_count, domain=None, range=Optional[int])

slots.system_counts = Slot(uri=BIOSIM_SCHEMA['composition/system_counts'], name="system_counts", curie=BIOSIM_SCHEMA.curie('composition/system_counts'),
                   model_uri=BIOSIM_SCHEMA.system_counts, domain=None, range=Optional[Union[dict, SystemCounts]])

slots.molecule_ID = Slot(uri=BIOSIM_SCHEMA['composition/molecule_ID'], name="molecule_ID", curie=BIOSIM_SCHEMA.curie('composition/molecule_ID'),
                   model_uri=BIOSIM_SCHEMA.molecule_ID, domain=None, range=Optional[Union[Union[dict, MoleculeID], list[Union[dict, MoleculeID]]]])

slots.identifier = Slot(uri=SCHEMA.identifier, name="identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=BIOSIM_SCHEMA.identifier, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.PDB_ID = Slot(uri=BIOSIM_SCHEMA['composition/PDB_ID'], name="PDB_ID", curie=BIOSIM_SCHEMA.curie('composition/PDB_ID'),
                   model_uri=BIOSIM_SCHEMA.PDB_ID, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9A-Za-z]{4}$'))

slots.UNIPROT_ID = Slot(uri=BIOSIM_SCHEMA['composition/UNIPROT_ID'], name="UNIPROT_ID", curie=BIOSIM_SCHEMA.curie('composition/UNIPROT_ID'),
                   model_uri=BIOSIM_SCHEMA.UNIPROT_ID, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z0-9]{6,10}$'))

slots.EMDB_ID = Slot(uri=BIOSIM_SCHEMA['composition/EMDB_ID'], name="EMDB_ID", curie=BIOSIM_SCHEMA.curie('composition/EMDB_ID'),
                   model_uri=BIOSIM_SCHEMA.EMDB_ID, domain=None, range=Optional[str],
                   pattern=re.compile(r'^EMD-\d{4,5}$'))

slots.alphafold_ID = Slot(uri=BIOSIM_SCHEMA['composition/alphafold_ID'], name="alphafold_ID", curie=BIOSIM_SCHEMA.curie('composition/alphafold_ID'),
                   model_uri=BIOSIM_SCHEMA.alphafold_ID, domain=None, range=Optional[str],
                   pattern=re.compile(r'^AF-[A-Z0-9]+-F1$'))

slots.PubChem_CID = Slot(uri=BIOSIM_SCHEMA['composition/PubChem_CID'], name="PubChem_CID", curie=BIOSIM_SCHEMA.curie('composition/PubChem_CID'),
                   model_uri=BIOSIM_SCHEMA.PubChem_CID, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+$'))

slots.InChIKey = Slot(uri=BIOSIM_SCHEMA['composition/InChIKey'], name="InChIKey", curie=BIOSIM_SCHEMA.curie('composition/InChIKey'),
                   model_uri=BIOSIM_SCHEMA.InChIKey, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z]{14}-[A-Z]{10}(-[A-Z])?$'))

slots.SMILES = Slot(uri=BIOSIM_SCHEMA['composition/SMILES'], name="SMILES", curie=BIOSIM_SCHEMA.curie('composition/SMILES'),
                   model_uri=BIOSIM_SCHEMA.SMILES, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9@+\-\[\]()=#$:./\\%*]+$'))

slots.InChI = Slot(uri=BIOSIM_SCHEMA['composition/InChI'], name="InChI", curie=BIOSIM_SCHEMA.curie('composition/InChI'),
                   model_uri=BIOSIM_SCHEMA.InChI, domain=None, range=Optional[str],
                   pattern=re.compile(r'^InChI=1S?/[A-Za-z0-9.+\-]+(/[a-z][^/]*)*$'))

slots.molecular_formula = Slot(uri=BIOSIM_SCHEMA['composition/molecular_formula'], name="molecular_formula", curie=BIOSIM_SCHEMA.curie('composition/molecular_formula'),
                   model_uri=BIOSIM_SCHEMA.molecular_formula, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([A-Z][a-z]?\d*)+$'))

slots.predicted_structure = Slot(uri=BIOSIM_SCHEMA['composition/predicted_structure'], name="predicted_structure", curie=BIOSIM_SCHEMA.curie('composition/predicted_structure'),
                   model_uri=BIOSIM_SCHEMA.predicted_structure, domain=None, range=Optional[Union[bool, Bool]])

slots.modified = Slot(uri=BIOSIM_SCHEMA['composition/modified'], name="modified", curie=BIOSIM_SCHEMA.curie('composition/modified'),
                   model_uri=BIOSIM_SCHEMA.modified, domain=None, range=Optional[Union[bool, Bool]])

slots.protein_sequence = Slot(uri=BIOSIM_SCHEMA['composition/protein_sequence'], name="protein_sequence", curie=BIOSIM_SCHEMA.curie('composition/protein_sequence'),
                   model_uri=BIOSIM_SCHEMA.protein_sequence, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[ACDEFGHIKLMNPQRSTVWY]+$'))

slots.nucleic_sequence = Slot(uri=BIOSIM_SCHEMA['composition/nucleic_sequence'], name="nucleic_sequence", curie=BIOSIM_SCHEMA.curie('composition/nucleic_sequence'),
                   model_uri=BIOSIM_SCHEMA.nucleic_sequence, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[ACGTURYSWKMBDHVN]+$'))

slots.simulation_averages = Slot(uri=BIOSIM_SCHEMA['observables/simulation_averages'], name="simulation_averages", curie=BIOSIM_SCHEMA.curie('observables/simulation_averages'),
                   model_uri=BIOSIM_SCHEMA.simulation_averages, domain=None, range=Optional[Union[dict, SimulationAverages]])

slots.average_temperature = Slot(uri=BIOSIM_SCHEMA['observables/average_temperature'], name="average_temperature", curie=BIOSIM_SCHEMA.curie('observables/average_temperature'),
                   model_uri=BIOSIM_SCHEMA.average_temperature, domain=None, range=Optional[Union[dict, TemperatureQuantity]])

slots.average_pressure = Slot(uri=BIOSIM_SCHEMA['observables/average_pressure'], name="average_pressure", curie=BIOSIM_SCHEMA.curie('observables/average_pressure'),
                   model_uri=BIOSIM_SCHEMA.average_pressure, domain=None, range=Optional[Union[dict, PressureQuantity]])

slots.average_volume = Slot(uri=BIOSIM_SCHEMA['observables/average_volume'], name="average_volume", curie=BIOSIM_SCHEMA.curie('observables/average_volume'),
                   model_uri=BIOSIM_SCHEMA.average_volume, domain=None, range=Optional[Union[dict, VolumeQuantity]])

slots.average_volume_vector = Slot(uri=BIOSIM_SCHEMA['observables/average_volume_vector'], name="average_volume_vector", curie=BIOSIM_SCHEMA.curie('observables/average_volume_vector'),
                   model_uri=BIOSIM_SCHEMA.average_volume_vector, domain=None, range=Optional[Union[dict, VectorVolumeQuantity]])

slots.average_potential_energy = Slot(uri=BIOSIM_SCHEMA['observables/average_potential_energy'], name="average_potential_energy", curie=BIOSIM_SCHEMA.curie('observables/average_potential_energy'),
                   model_uri=BIOSIM_SCHEMA.average_potential_energy, domain=None, range=Optional[Union[dict, MolarEnergyQuantity]])

slots.average_kinetic_energy = Slot(uri=BIOSIM_SCHEMA['observables/average_kinetic_energy'], name="average_kinetic_energy", curie=BIOSIM_SCHEMA.curie('observables/average_kinetic_energy'),
                   model_uri=BIOSIM_SCHEMA.average_kinetic_energy, domain=None, range=Optional[Union[dict, MolarEnergyQuantity]])

slots.average_enthalpy = Slot(uri=BIOSIM_SCHEMA['observables/average_enthalpy'], name="average_enthalpy", curie=BIOSIM_SCHEMA.curie('observables/average_enthalpy'),
                   model_uri=BIOSIM_SCHEMA.average_enthalpy, domain=None, range=Optional[Union[dict, MolarEnergyQuantity]])

slots.connectivity = Slot(uri=BIOSIM_SCHEMA['topology/connectivity'], name="connectivity", curie=BIOSIM_SCHEMA.curie('topology/connectivity'),
                   model_uri=BIOSIM_SCHEMA.connectivity, domain=None, range=Optional[Union[dict, Connectivity]])

slots.particles = Slot(uri=BIOSIM_SCHEMA['topology/particles'], name="particles", curie=BIOSIM_SCHEMA.curie('topology/particles'),
                   model_uri=BIOSIM_SCHEMA.particles, domain=None, range=Optional[Union[dict, Particles]])

slots.masses = Slot(uri=BIOSIM_SCHEMA['topology/masses'], name="masses", curie=BIOSIM_SCHEMA.curie('topology/masses'),
                   model_uri=BIOSIM_SCHEMA.masses, domain=None, range=Optional[Union[bool, Bool]])

slots.bonds = Slot(uri=BIOSIM_SCHEMA['topology/bonds'], name="bonds", curie=BIOSIM_SCHEMA.curie('topology/bonds'),
                   model_uri=BIOSIM_SCHEMA.bonds, domain=None, range=Optional[Union[bool, Bool]])

slots.dihedrals = Slot(uri=BIOSIM_SCHEMA['topology/dihedrals'], name="dihedrals", curie=BIOSIM_SCHEMA.curie('topology/dihedrals'),
                   model_uri=BIOSIM_SCHEMA.dihedrals, domain=None, range=Optional[Union[bool, Bool]])

slots.fixed_charges = Slot(uri=BIOSIM_SCHEMA['topology/fixed_charges'], name="fixed_charges", curie=BIOSIM_SCHEMA.curie('topology/fixed_charges'),
                   model_uri=BIOSIM_SCHEMA.fixed_charges, domain=None, range=Optional[Union[bool, Bool]])

slots.coarse_grained = Slot(uri=BIOSIM_SCHEMA['topology/coarse_grained'], name="coarse_grained", curie=BIOSIM_SCHEMA.curie('topology/coarse_grained'),
                   model_uri=BIOSIM_SCHEMA.coarse_grained, domain=None, range=Optional[Union[bool, Bool]])

slots.system_charge = Slot(uri=BIOSIM_SCHEMA['topology/system_charge'], name="system_charge", curie=BIOSIM_SCHEMA.curie('topology/system_charge'),
                   model_uri=BIOSIM_SCHEMA.system_charge, domain=None, range=Optional[Union[dict, ChargeQuantity]],
                   pattern=re.compile(r'^[+-]?\d+(\.\d+)?$'))

slots.resolution = Slot(uri=BIOSIM_SCHEMA['topology/resolution'], name="resolution", curie=BIOSIM_SCHEMA.curie('topology/resolution'),
                   model_uri=BIOSIM_SCHEMA.resolution, domain=None, range=Optional[Union[str, "ModelResolution"]])

slots.simulation_box = Slot(uri=BIOSIM_SCHEMA['trajectory/simulation_box'], name="simulation_box", curie=BIOSIM_SCHEMA.curie('trajectory/simulation_box'),
                   model_uri=BIOSIM_SCHEMA.simulation_box, domain=None, range=Optional[Union[dict, SimulationBox]])

slots.trajectory_output = Slot(uri=BIOSIM_SCHEMA['trajectory/trajectory_output'], name="trajectory_output", curie=BIOSIM_SCHEMA.curie('trajectory/trajectory_output'),
                   model_uri=BIOSIM_SCHEMA.trajectory_output, domain=None, range=Optional[Union[dict, Trajectories]])

slots.frame_count = Slot(uri=BIOSIM_SCHEMA['trajectory/frame_count'], name="frame_count", curie=BIOSIM_SCHEMA.curie('trajectory/frame_count'),
                   model_uri=BIOSIM_SCHEMA.frame_count, domain=None, range=Optional[int])

slots.periodic_boundary_conditions = Slot(uri=BIOSIM_SCHEMA['trajectory/periodic_boundary_conditions'], name="periodic_boundary_conditions", curie=BIOSIM_SCHEMA.curie('trajectory/periodic_boundary_conditions'),
                   model_uri=BIOSIM_SCHEMA.periodic_boundary_conditions, domain=None, range=Optional[Union[str, "PeriodicBoundaryConditions"]])

slots.box_dimensions = Slot(uri=BIOSIM_SCHEMA['trajectory/box_dimensions'], name="box_dimensions", curie=BIOSIM_SCHEMA.curie('trajectory/box_dimensions'),
                   model_uri=BIOSIM_SCHEMA.box_dimensions, domain=None, range=Optional[Union[dict, VectorLengthQuantity]])

slots.box_angles = Slot(uri=BIOSIM_SCHEMA['trajectory/box_angles'], name="box_angles", curie=BIOSIM_SCHEMA.curie('trajectory/box_angles'),
                   model_uri=BIOSIM_SCHEMA.box_angles, domain=None, range=Optional[Union[dict, VectorAngleQuantity]])

slots.box_type = Slot(uri=BIOSIM_SCHEMA['trajectory/box_type'], name="box_type", curie=BIOSIM_SCHEMA.curie('trajectory/box_type'),
                   model_uri=BIOSIM_SCHEMA.box_type, domain=None, range=Optional[Union[str, "BoxType"]])

slots.positions = Slot(uri=BIOSIM_SCHEMA['trajectory/positions'], name="positions", curie=BIOSIM_SCHEMA.curie('trajectory/positions'),
                   model_uri=BIOSIM_SCHEMA.positions, domain=None, range=Optional[Union[bool, Bool]])

slots.forces = Slot(uri=BIOSIM_SCHEMA['trajectory/forces'], name="forces", curie=BIOSIM_SCHEMA.curie('trajectory/forces'),
                   model_uri=BIOSIM_SCHEMA.forces, domain=None, range=Optional[Union[bool, Bool]])

slots.velocities = Slot(uri=BIOSIM_SCHEMA['trajectory/velocities'], name="velocities", curie=BIOSIM_SCHEMA.curie('trajectory/velocities'),
                   model_uri=BIOSIM_SCHEMA.velocities, domain=None, range=Optional[Union[bool, Bool]])

slots.energies = Slot(uri=BIOSIM_SCHEMA['trajectory/energies'], name="energies", curie=BIOSIM_SCHEMA.curie('trajectory/energies'),
                   model_uri=BIOSIM_SCHEMA.energies, domain=None, range=Optional[Union[bool, Bool]])

slots.polarizable_charges = Slot(uri=BIOSIM_SCHEMA['trajectory/polarizable_charges'], name="polarizable_charges", curie=BIOSIM_SCHEMA.curie('trajectory/polarizable_charges'),
                   model_uri=BIOSIM_SCHEMA.polarizable_charges, domain=None, range=Optional[Union[bool, Bool]])

slots.water = Slot(uri=BIOSIM_SCHEMA['trajectory/water'], name="water", curie=BIOSIM_SCHEMA.curie('trajectory/water'),
                   model_uri=BIOSIM_SCHEMA.water, domain=None, range=Optional[Union[bool, Bool]])

slots.replica = Slot(uri=BIOSIM_SCHEMA['trajectory/replica'], name="replica", curie=BIOSIM_SCHEMA.curie('trajectory/replica'),
                   model_uri=BIOSIM_SCHEMA.replica, domain=None, range=Optional[Union[bool, Bool]])

slots.water_potential = Slot(uri=BIOSIM_SCHEMA['potentials/water_potential'], name="water_potential", curie=BIOSIM_SCHEMA.curie('potentials/water_potential'),
                   model_uri=BIOSIM_SCHEMA.water_potential, domain=None, range=Optional[Union[dict, WaterPotential]])

slots.water_potential_name = Slot(uri=BIOSIM_SCHEMA['potentials/water_potential_name'], name="water_potential_name", curie=BIOSIM_SCHEMA.curie('potentials/water_potential_name'),
                   model_uri=BIOSIM_SCHEMA.water_potential_name, domain=None, range=Optional[Union[str, "WaterPotentialName"]])

slots.protein_potential = Slot(uri=BIOSIM_SCHEMA['potentials/protein_potential'], name="protein_potential", curie=BIOSIM_SCHEMA.curie('potentials/protein_potential'),
                   model_uri=BIOSIM_SCHEMA.protein_potential, domain=None, range=Optional[Union[dict, ProteinPotential]])

slots.protein_potential_name = Slot(uri=BIOSIM_SCHEMA['potentials/protein_potential_name'], name="protein_potential_name", curie=BIOSIM_SCHEMA.curie('potentials/protein_potential_name'),
                   model_uri=BIOSIM_SCHEMA.protein_potential_name, domain=None, range=Optional[Union[str, "ProteinPotentialName"]])

slots.lipid_potential = Slot(uri=BIOSIM_SCHEMA['potentials/lipid_potential'], name="lipid_potential", curie=BIOSIM_SCHEMA.curie('potentials/lipid_potential'),
                   model_uri=BIOSIM_SCHEMA.lipid_potential, domain=None, range=Optional[Union[dict, LipidPotential]])

slots.lipid_potential_name = Slot(uri=BIOSIM_SCHEMA['potentials/lipid_potential_name'], name="lipid_potential_name", curie=BIOSIM_SCHEMA.curie('potentials/lipid_potential_name'),
                   model_uri=BIOSIM_SCHEMA.lipid_potential_name, domain=None, range=Optional[Union[str, "LipidPotentialName"]])

slots.nucleic_potential = Slot(uri=BIOSIM_SCHEMA['potentials/nucleic_potential'], name="nucleic_potential", curie=BIOSIM_SCHEMA.curie('potentials/nucleic_potential'),
                   model_uri=BIOSIM_SCHEMA.nucleic_potential, domain=None, range=Optional[Union[dict, NucleicPotential]])

slots.nucleic_potential_name = Slot(uri=BIOSIM_SCHEMA['potentials/nucleic_potential_name'], name="nucleic_potential_name", curie=BIOSIM_SCHEMA.curie('potentials/nucleic_potential_name'),
                   model_uri=BIOSIM_SCHEMA.nucleic_potential_name, domain=None, range=Optional[Union[str, "NucleicPotentialName"]])

slots.carbohydrate_potential = Slot(uri=BIOSIM_SCHEMA['potentials/carbohydrate_potential'], name="carbohydrate_potential", curie=BIOSIM_SCHEMA.curie('potentials/carbohydrate_potential'),
                   model_uri=BIOSIM_SCHEMA.carbohydrate_potential, domain=None, range=Optional[Union[dict, CarbohydratePotential]])

slots.carbohydrate_potential_name = Slot(uri=BIOSIM_SCHEMA['potentials/carbohydrate_potential_name'], name="carbohydrate_potential_name", curie=BIOSIM_SCHEMA.curie('potentials/carbohydrate_potential_name'),
                   model_uri=BIOSIM_SCHEMA.carbohydrate_potential_name, domain=None, range=Optional[Union[str, "CarbohydratePotentialName"]])

slots.polymer_potential = Slot(uri=BIOSIM_SCHEMA['potentials/polymer_potential'], name="polymer_potential", curie=BIOSIM_SCHEMA.curie('potentials/polymer_potential'),
                   model_uri=BIOSIM_SCHEMA.polymer_potential, domain=None, range=Optional[Union[dict, PolymerPotential]])

slots.polymer_potential_name = Slot(uri=BIOSIM_SCHEMA['potentials/polymer_potential_name'], name="polymer_potential_name", curie=BIOSIM_SCHEMA.curie('potentials/polymer_potential_name'),
                   model_uri=BIOSIM_SCHEMA.polymer_potential_name, domain=None, range=Optional[Union[str, "PolymerPotentialName"]])

slots.general_potential = Slot(uri=BIOSIM_SCHEMA['potentials/general_potential'], name="general_potential", curie=BIOSIM_SCHEMA.curie('potentials/general_potential'),
                   model_uri=BIOSIM_SCHEMA.general_potential, domain=None, range=Optional[Union[dict, GeneralPotential]])

slots.general_potential_name = Slot(uri=BIOSIM_SCHEMA['potentials/general_potential_name'], name="general_potential_name", curie=BIOSIM_SCHEMA.curie('potentials/general_potential_name'),
                   model_uri=BIOSIM_SCHEMA.general_potential_name, domain=None, range=Optional[Union[str, "GeneralPotentialName"]])

slots.machine_learned_potential = Slot(uri=BIOSIM_SCHEMA['potentials/machine_learned_potential'], name="machine_learned_potential", curie=BIOSIM_SCHEMA.curie('potentials/machine_learned_potential'),
                   model_uri=BIOSIM_SCHEMA.machine_learned_potential, domain=None, range=Optional[Union[dict, MachineLearnedPotential]])

slots.machine_learned_potential_name = Slot(uri=BIOSIM_SCHEMA['potentials/machine_learned_potential_name'], name="machine_learned_potential_name", curie=BIOSIM_SCHEMA.curie('potentials/machine_learned_potential_name'),
                   model_uri=BIOSIM_SCHEMA.machine_learned_potential_name, domain=None, range=Optional[Union[str, "MachineLearnedPotentialName"]])

slots.hardware = Slot(uri=BIOSIM_SCHEMA['compute/hardware'], name="hardware", curie=BIOSIM_SCHEMA.curie('compute/hardware'),
                   model_uri=BIOSIM_SCHEMA.hardware, domain=None, range=Optional[Union[dict, Hardware]])

slots.software = Slot(uri=BIOSIM_SCHEMA['compute/software'], name="software", curie=BIOSIM_SCHEMA.curie('compute/software'),
                   model_uri=BIOSIM_SCHEMA.software, domain=None, range=Optional[Union[dict, Software]])

slots.performance = Slot(uri=BIOSIM_SCHEMA['compute/performance'], name="performance", curie=BIOSIM_SCHEMA.curie('compute/performance'),
                   model_uri=BIOSIM_SCHEMA.performance, domain=None, range=Optional[Union[dict, Performance]])

slots.operating_system = Slot(uri=BIOSIM_SCHEMA['compute/operating_system'], name="operating_system", curie=BIOSIM_SCHEMA.curie('compute/operating_system'),
                   model_uri=BIOSIM_SCHEMA.operating_system, domain=None, range=Optional[Union[str, "OperatingSystem"]])

slots.scheduler = Slot(uri=BIOSIM_SCHEMA['compute/scheduler'], name="scheduler", curie=BIOSIM_SCHEMA.curie('compute/scheduler'),
                   model_uri=BIOSIM_SCHEMA.scheduler, domain=None, range=Optional[Union[str, "Scheduler"]])

slots.MPI_library = Slot(uri=BIOSIM_SCHEMA['compute/MPI_library'], name="MPI_library", curie=BIOSIM_SCHEMA.curie('compute/MPI_library'),
                   model_uri=BIOSIM_SCHEMA.MPI_library, domain=None, range=Optional[Union[str, "MPILibrary"]])

slots.container_runtime = Slot(uri=BIOSIM_SCHEMA['compute/container_runtime'], name="container_runtime", curie=BIOSIM_SCHEMA.curie('compute/container_runtime'),
                   model_uri=BIOSIM_SCHEMA.container_runtime, domain=None, range=Optional[Union[str, "ContainerRuntime"]])

slots.wall_time = Slot(uri=BIOSIM_SCHEMA['compute/wall_time'], name="wall_time", curie=BIOSIM_SCHEMA.curie('compute/wall_time'),
                   model_uri=BIOSIM_SCHEMA.wall_time, domain=None, range=Optional[Union[dict, TimeQuantity]])

slots.energy_consumption = Slot(uri=BIOSIM_SCHEMA['compute/energy_consumption'], name="energy_consumption", curie=BIOSIM_SCHEMA.curie('compute/energy_consumption'),
                   model_uri=BIOSIM_SCHEMA.energy_consumption, domain=None, range=Optional[Union[dict, EnergyQuantity]])

slots.execution_platform = Slot(uri=BIOSIM_SCHEMA['compute/execution_platform'], name="execution_platform", curie=BIOSIM_SCHEMA.curie('compute/execution_platform'),
                   model_uri=BIOSIM_SCHEMA.execution_platform, domain=None, range=Optional[Union[str, "ExecutionPlatform"]])

slots.node_type = Slot(uri=BIOSIM_SCHEMA['compute/node_type'], name="node_type", curie=BIOSIM_SCHEMA.curie('compute/node_type'),
                   model_uri=BIOSIM_SCHEMA.node_type, domain=None, range=Optional[Union[str, "NodeType"]])

slots.node_count = Slot(uri=BIOSIM_SCHEMA['compute/node_count'], name="node_count", curie=BIOSIM_SCHEMA.curie('compute/node_count'),
                   model_uri=BIOSIM_SCHEMA.node_count, domain=None, range=Optional[int])

slots.CPU_vendor = Slot(uri=BIOSIM_SCHEMA['compute/CPU_vendor'], name="CPU_vendor", curie=BIOSIM_SCHEMA.curie('compute/CPU_vendor'),
                   model_uri=BIOSIM_SCHEMA.CPU_vendor, domain=None, range=Optional[Union[str, "CpuVendor"]])

slots.CPU_architecture = Slot(uri=BIOSIM_SCHEMA['compute/CPU_architecture'], name="CPU_architecture", curie=BIOSIM_SCHEMA.curie('compute/CPU_architecture'),
                   model_uri=BIOSIM_SCHEMA.CPU_architecture, domain=None, range=Optional[Union[str, "CpuArchitecture"]])

slots.sockets_per_node = Slot(uri=BIOSIM_SCHEMA['compute/sockets_per_node'], name="sockets_per_node", curie=BIOSIM_SCHEMA.curie('compute/sockets_per_node'),
                   model_uri=BIOSIM_SCHEMA.sockets_per_node, domain=None, range=Optional[int])

slots.cores_per_socket = Slot(uri=BIOSIM_SCHEMA['compute/cores_per_socket'], name="cores_per_socket", curie=BIOSIM_SCHEMA.curie('compute/cores_per_socket'),
                   model_uri=BIOSIM_SCHEMA.cores_per_socket, domain=None, range=Optional[int])

slots.threads_per_core = Slot(uri=BIOSIM_SCHEMA['compute/threads_per_core'], name="threads_per_core", curie=BIOSIM_SCHEMA.curie('compute/threads_per_core'),
                   model_uri=BIOSIM_SCHEMA.threads_per_core, domain=None, range=Optional[int])

slots.GPU_vendor = Slot(uri=BIOSIM_SCHEMA['compute/GPU_vendor'], name="GPU_vendor", curie=BIOSIM_SCHEMA.curie('compute/GPU_vendor'),
                   model_uri=BIOSIM_SCHEMA.GPU_vendor, domain=None, range=Optional[Union[str, "GpuVendor"]])

slots.GPUs_per_node = Slot(uri=BIOSIM_SCHEMA['compute/GPUs_per_node'], name="GPUs_per_node", curie=BIOSIM_SCHEMA.curie('compute/GPUs_per_node'),
                   model_uri=BIOSIM_SCHEMA.GPUs_per_node, domain=None, range=Optional[int])

slots.memory_per_node = Slot(uri=BIOSIM_SCHEMA['compute/memory_per_node'], name="memory_per_node", curie=BIOSIM_SCHEMA.curie('compute/memory_per_node'),
                   model_uri=BIOSIM_SCHEMA.memory_per_node, domain=None, range=Optional[Union[dict, ByteQuantity]])

slots.file_name = Slot(uri=BIOSIM_SCHEMA['files/file_name'], name="file_name", curie=BIOSIM_SCHEMA.curie('files/file_name'),
                   model_uri=BIOSIM_SCHEMA.file_name, domain=None, range=str)

slots.file_size = Slot(uri=BIOSIM_SCHEMA['files/file_size'], name="file_size", curie=BIOSIM_SCHEMA.curie('files/file_size'),
                   model_uri=BIOSIM_SCHEMA.file_size, domain=None, range=Optional[Union[dict, ByteQuantity]])

slots.file_hash = Slot(uri=BIOSIM_SCHEMA['files/file_hash'], name="file_hash", curie=BIOSIM_SCHEMA.curie('files/file_hash'),
                   model_uri=BIOSIM_SCHEMA.file_hash, domain=None, range=Optional[str])

slots.file_hash_algorithm = Slot(uri=BIOSIM_SCHEMA['files/file_hash_algorithm'], name="file_hash_algorithm", curie=BIOSIM_SCHEMA.curie('files/file_hash_algorithm'),
                   model_uri=BIOSIM_SCHEMA.file_hash_algorithm, domain=None, range=Optional[Union[str, "FileHashAlgorithm"]])

slots.file_role = Slot(uri=BIOSIM_SCHEMA['files/file_role'], name="file_role", curie=BIOSIM_SCHEMA.curie('files/file_role'),
                   model_uri=BIOSIM_SCHEMA.file_role, domain=None, range=Optional[Union[str, "FileRole"]])

slots.lengthQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="lengthQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.lengthQuantity__value, domain=None, range=Optional[float])

slots.lengthQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="lengthQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.lengthQuantity__value_unit, domain=None, range=Optional[Union[str, "LengthUnit"]])

slots.volumeQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="volumeQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.volumeQuantity__value, domain=None, range=Optional[float])

slots.volumeQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="volumeQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.volumeQuantity__value_unit, domain=None, range=Optional[Union[str, "VolumeUnit"]])

slots.timeQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="timeQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.timeQuantity__value, domain=None, range=Optional[float])

slots.timeQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="timeQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.timeQuantity__value_unit, domain=None, range=Optional[Union[str, "TimeUnit"]])

slots.frequencyQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="frequencyQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.frequencyQuantity__value, domain=None, range=Optional[float])

slots.frequencyQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="frequencyQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.frequencyQuantity__value_unit, domain=None, range=Optional[Union[str, "FrequencyUnit"]])

slots.frictionCoefficientQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="frictionCoefficientQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.frictionCoefficientQuantity__value, domain=None, range=Optional[float])

slots.frictionCoefficientQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="frictionCoefficientQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.frictionCoefficientQuantity__value_unit, domain=None, range=Optional[Union[str, "FrictionCoefficientUnit"]])

slots.molarEnergyQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="molarEnergyQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.molarEnergyQuantity__value, domain=None, range=Optional[float],
                   pattern=re.compile(r'^[+-]?\d+(\.\d+)?$'))

slots.molarEnergyQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="molarEnergyQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.molarEnergyQuantity__value_unit, domain=None, range=Optional[Union[str, "MolarEnergyUnit"]])

slots.energyQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="energyQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.energyQuantity__value, domain=None, range=Optional[float])

slots.energyQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="energyQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.energyQuantity__value_unit, domain=None, range=Optional[Union[str, "EnergyUnit"]])

slots.temperatureQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="temperatureQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.temperatureQuantity__value, domain=None, range=Optional[float])

slots.temperatureQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="temperatureQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.temperatureQuantity__value_unit, domain=None, range=Optional[Union[str, "TemperatureUnit"]])

slots.pressureQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="pressureQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.pressureQuantity__value, domain=None, range=Optional[float])

slots.pressureQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="pressureQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.pressureQuantity__value_unit, domain=None, range=Optional[Union[str, "PressureUnit"]])

slots.compressibilityQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="compressibilityQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.compressibilityQuantity__value, domain=None, range=Optional[float])

slots.compressibilityQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="compressibilityQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.compressibilityQuantity__value_unit, domain=None, range=Optional[Union[str, "CompressibilityUnit"]])

slots.massQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="massQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.massQuantity__value, domain=None, range=Optional[float])

slots.massQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="massQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.massQuantity__value_unit, domain=None, range=Optional[Union[str, "MassUnit"]])

slots.concentrationQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="concentrationQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.concentrationQuantity__value, domain=None, range=Optional[float])

slots.concentrationQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="concentrationQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.concentrationQuantity__value_unit, domain=None, range=Optional[Union[str, "ConcentrationUnit"]])

slots.forceQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="forceQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.forceQuantity__value, domain=None, range=Optional[float],
                   pattern=re.compile(r'^[+-]?\d+(\.\d+)?$'))

slots.forceQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="forceQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.forceQuantity__value_unit, domain=None, range=Optional[Union[str, "ForceUnit"]])

slots.chargeQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="chargeQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.chargeQuantity__value, domain=None, range=Optional[float])

slots.chargeQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="chargeQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.chargeQuantity__value_unit, domain=None, range=Optional[Union[str, "ChargeUnit"]])

slots.angleQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="angleQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.angleQuantity__value, domain=None, range=Optional[float])

slots.angleQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="angleQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.angleQuantity__value_unit, domain=None, range=Optional[Union[str, "AngleUnit"]])

slots.byteQuantity__value = Slot(uri=BIOSIM_SCHEMA['quantities/value'], name="byteQuantity__value", curie=BIOSIM_SCHEMA.curie('quantities/value'),
                   model_uri=BIOSIM_SCHEMA.byteQuantity__value, domain=None, range=Optional[float])

slots.byteQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="byteQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.byteQuantity__value_unit, domain=None, range=Optional[Union[str, "ByteUnit"]])

slots.vectorLengthQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="vectorLengthQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.vectorLengthQuantity__vector_value, domain=None, range=Optional[Union[float, list[float]]])

slots.vectorLengthQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="vectorLengthQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.vectorLengthQuantity__value_unit, domain=None, range=Optional[Union[str, "LengthUnit"]])

slots.vectorAngleQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="vectorAngleQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.vectorAngleQuantity__vector_value, domain=None, range=Optional[Union[float, list[float]]])

slots.vectorAngleQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="vectorAngleQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.vectorAngleQuantity__value_unit, domain=None, range=Optional[Union[str, "AngleUnit"]])

slots.vectorVolumeQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="vectorVolumeQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.vectorVolumeQuantity__vector_value, domain=None, range=Optional[Union[float, list[float]]])

slots.vectorVolumeQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="vectorVolumeQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.vectorVolumeQuantity__value_unit, domain=None, range=Optional[Union[str, "LengthUnit"]])

slots.vectorCompressibilityQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="vectorCompressibilityQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.vectorCompressibilityQuantity__vector_value, domain=None, range=Optional[float])

slots.vectorCompressibilityQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="vectorCompressibilityQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.vectorCompressibilityQuantity__value_unit, domain=None, range=Optional[Union[str, "CompressibilityUnit"]])

slots.vectorPressureQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="vectorPressureQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.vectorPressureQuantity__vector_value, domain=None, range=Optional[Union[float, list[float]]])

slots.vectorPressureQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="vectorPressureQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.vectorPressureQuantity__value_unit, domain=None, range=Optional[Union[str, "PressureUnit"]])

slots.vectorTemperatureQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="vectorTemperatureQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.vectorTemperatureQuantity__vector_value, domain=None, range=Optional[Union[float, list[float]]])

slots.vectorTemperatureQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="vectorTemperatureQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.vectorTemperatureQuantity__value_unit, domain=None, range=Optional[Union[str, "TemperatureUnit"]])

slots.vectorTimeQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="vectorTimeQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.vectorTimeQuantity__vector_value, domain=None, range=Optional[Union[float, list[float]]])

slots.vectorTimeQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="vectorTimeQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.vectorTimeQuantity__value_unit, domain=None, range=Optional[Union[str, "TimeUnit"]])

slots.matrixPressureQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="matrixPressureQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.matrixPressureQuantity__vector_value, domain=None, range=Optional[Union[float, list[float]]])

slots.matrixPressureQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="matrixPressureQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.matrixPressureQuantity__value_unit, domain=None, range=Optional[Union[str, "PressureUnit"]])

slots.matrixCompressibilityQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="matrixCompressibilityQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.matrixCompressibilityQuantity__vector_value, domain=None, range=Optional[Union[float, list[float]]])

slots.matrixCompressibilityQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="matrixCompressibilityQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.matrixCompressibilityQuantity__value_unit, domain=None, range=Optional[Union[str, "CompressibilityUnit"]])

slots.matrixQuantity__vector_value = Slot(uri=BIOSIM_SCHEMA['quantities/vector_value'], name="matrixQuantity__vector_value", curie=BIOSIM_SCHEMA.curie('quantities/vector_value'),
                   model_uri=BIOSIM_SCHEMA.matrixQuantity__vector_value, domain=None, range=Optional[Union[float, list[float]]])

slots.matrixQuantity__value_unit = Slot(uri=BIOSIM_SCHEMA['quantities/value_unit'], name="matrixQuantity__value_unit", curie=BIOSIM_SCHEMA.curie('quantities/value_unit'),
                   model_uri=BIOSIM_SCHEMA.matrixQuantity__value_unit, domain=None, range=Optional[str])
