---
search:
  boost: 10.0
---

# Class: VectorVolumeQuantity

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/VectorVolumeQuantity](https://CCPBioSim.ac.uk/biosim-schema/VectorVolumeQuantity)





```{mermaid}
 classDiagram
    class VectorVolumeQuantity
    click VectorVolumeQuantity href "../../classes/VectorVolumeQuantity/"
      VectorVolumeQuantity : value_unit





        VectorVolumeQuantity --> "0..1" LengthUnit : value_unit
        click LengthUnit href "../../enums/LengthUnit/"



      VectorVolumeQuantity : vector_value


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [vector_value](../slots/vector_value.md) | 3 <br/> [float](../types/float.md) |  | direct |
| [value_unit](../slots/value_unit.md) | 0..1 <br/> [LengthUnit](../enums/LengthUnit.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationAverages](../classes/SimulationAverages.md) | [average_volume_vector](../slots/average_volume_vector.md) | range | [VectorVolumeQuantity](../classes/VectorVolumeQuantity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/VectorVolumeQuantity |
| native | https://CCPBioSim.ac.uk/biosim-schema/VectorVolumeQuantity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VectorVolumeQuantity
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  vector_value:
    name: vector_value
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    domain_of:
    - VectorLengthQuantity
    - VectorAngleQuantity
    - VectorVolumeQuantity
    - VectorCompressibilityQuantity
    - VectorPressureQuantity
    - VectorTemperatureQuantity
    - VectorTimeQuantity
    - MatrixPressureQuantity
    - MatrixCompressibilityQuantity
    - MatrixQuantity
    range: float
    multivalued: true
    exact_cardinality: 3
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(nm)
    domain_of:
    - LengthQuantity
    - VolumeQuantity
    - TimeQuantity
    - FrequencyQuantity
    - FrictionCoefficientQuantity
    - MolarEnergyQuantity
    - EnergyQuantity
    - TemperatureQuantity
    - PressureQuantity
    - MassQuantity
    - ConcentrationQuantity
    - ForceQuantity
    - ChargeQuantity
    - AngleQuantity
    - ByteQuantity
    - VectorLengthQuantity
    - VectorAngleQuantity
    - VectorVolumeQuantity
    - VectorCompressibilityQuantity
    - VectorPressureQuantity
    - VectorTemperatureQuantity
    - VectorTimeQuantity
    - MatrixPressureQuantity
    - MatrixCompressibilityQuantity
    - MatrixQuantity
    range: LengthUnit

```
</details>

### Induced

<details>
```yaml
name: VectorVolumeQuantity
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  vector_value:
    name: vector_value
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    owner: VectorVolumeQuantity
    domain_of:
    - VectorLengthQuantity
    - VectorAngleQuantity
    - VectorVolumeQuantity
    - VectorCompressibilityQuantity
    - VectorPressureQuantity
    - VectorTemperatureQuantity
    - VectorTimeQuantity
    - MatrixPressureQuantity
    - MatrixCompressibilityQuantity
    - MatrixQuantity
    range: float
    multivalued: true
    exact_cardinality: 3
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(nm)
    owner: VectorVolumeQuantity
    domain_of:
    - LengthQuantity
    - VolumeQuantity
    - TimeQuantity
    - FrequencyQuantity
    - FrictionCoefficientQuantity
    - MolarEnergyQuantity
    - EnergyQuantity
    - TemperatureQuantity
    - PressureQuantity
    - MassQuantity
    - ConcentrationQuantity
    - ForceQuantity
    - ChargeQuantity
    - AngleQuantity
    - ByteQuantity
    - VectorLengthQuantity
    - VectorAngleQuantity
    - VectorVolumeQuantity
    - VectorCompressibilityQuantity
    - VectorPressureQuantity
    - VectorTemperatureQuantity
    - VectorTimeQuantity
    - MatrixPressureQuantity
    - MatrixCompressibilityQuantity
    - MatrixQuantity
    range: LengthUnit

```
</details></div>
