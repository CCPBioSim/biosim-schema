---
search:
  boost: 10.0
---

# Class: VectorAngleQuantity


_A quantity representing 3D angles_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/VectorAngleQuantity](https://CCPBioSim.ac.uk/biosim-schema/VectorAngleQuantity)





```{mermaid}
 classDiagram
    class VectorAngleQuantity
    click VectorAngleQuantity href "../../classes/VectorAngleQuantity/"
      VectorAngleQuantity : value_unit





        VectorAngleQuantity --> "0..1" AngleUnit : value_unit
        click AngleUnit href "../../enums/AngleUnit/"



      VectorAngleQuantity : vector_value


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [vector_value](../slots/vector_value.md) | 3..* <br/> [float](../types/float.md) |  | direct |
| [value_unit](../slots/value_unit.md) | 0..1 <br/> [AngleUnit](../enums/AngleUnit.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationBox](../classes/SimulationBox.md) | [box_angles](../slots/box_angles.md) | range | [VectorAngleQuantity](../classes/VectorAngleQuantity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/VectorAngleQuantity |
| native | https://CCPBioSim.ac.uk/biosim-schema/VectorAngleQuantity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VectorAngleQuantity
description: A quantity representing 3D angles
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
    minimum_cardinality: 3
    maximum_cardinality: 3
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(degrees)
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
    range: AngleUnit

```
</details>

### Induced

<details>
```yaml
name: VectorAngleQuantity
description: A quantity representing 3D angles
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  vector_value:
    name: vector_value
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    owner: VectorAngleQuantity
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
    minimum_cardinality: 3
    maximum_cardinality: 3
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(degrees)
    owner: VectorAngleQuantity
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
    range: AngleUnit

```
</details></div>
