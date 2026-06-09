---
search:
  boost: 10.0
---

# Class: VectorLengthQuantity


_A quantity representing 3D lengths/dimensions_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/VectorLengthQuantity](https://CCPBioSim.ac.uk/biosim-schema/VectorLengthQuantity)





```{mermaid}
 classDiagram
    class VectorLengthQuantity
    click VectorLengthQuantity href "../../classes/VectorLengthQuantity/"
      VectorLengthQuantity : value_unit





        VectorLengthQuantity --> "0..1" LengthUnit : value_unit
        click LengthUnit href "../../enums/LengthUnit/"



      VectorLengthQuantity : vector_value


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [vector_value](../slots/vector_value.md) | 3..* <br/> [float](../types/float.md) |  | direct |
| [value_unit](../slots/value_unit.md) | 0..1 <br/> [LengthUnit](../enums/LengthUnit.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationBox](../classes/SimulationBox.md) | [box_dimensions](../slots/box_dimensions.md) | range | [VectorLengthQuantity](../classes/VectorLengthQuantity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/VectorLengthQuantity |
| native | https://CCPBioSim.ac.uk/biosim-schema/VectorLengthQuantity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VectorLengthQuantity
description: A quantity representing 3D lengths/dimensions
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
name: VectorLengthQuantity
description: A quantity representing 3D lengths/dimensions
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  vector_value:
    name: vector_value
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    owner: VectorLengthQuantity
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
    ifabsent: string(nm)
    owner: VectorLengthQuantity
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
