---
search:
  boost: 10.0
---

# Class: MatrixCompressibilityQuantity

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/MatrixCompressibilityQuantity](https://CCPBioSim.ac.uk/biosim-schema/MatrixCompressibilityQuantity)





```{mermaid}
 classDiagram
    class MatrixCompressibilityQuantity
    click MatrixCompressibilityQuantity href "../../classes/MatrixCompressibilityQuantity/"
      MatrixCompressibilityQuantity : value_unit





        MatrixCompressibilityQuantity --> "0..1" CompressibilityUnit : value_unit
        click CompressibilityUnit href "../../enums/CompressibilityUnit/"



      MatrixCompressibilityQuantity : vector_value


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [vector_value](../slots/vector_value.md) | * <br/> [float](../types/float.md) |  | direct |
| [value_unit](../slots/value_unit.md) | 0..1 <br/> [CompressibilityUnit](../enums/CompressibilityUnit.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Barostat](../classes/Barostat.md) | [compressibility](../slots/compressibility.md) | range | [MatrixCompressibilityQuantity](../classes/MatrixCompressibilityQuantity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/MatrixCompressibilityQuantity |
| native | https://CCPBioSim.ac.uk/biosim-schema/MatrixCompressibilityQuantity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MatrixCompressibilityQuantity
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
    array:
      minimum_number_dimensions: 2
      maximum_number_dimensions: 2
      dimensions:
      - alias: row
        exact_cardinality: 3
      - alias: column
        exact_cardinality: 3
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(1/bar)
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
    range: CompressibilityUnit

```
</details>

### Induced

<details>
```yaml
name: MatrixCompressibilityQuantity
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  vector_value:
    name: vector_value
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    owner: MatrixCompressibilityQuantity
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
    array:
      minimum_number_dimensions: 2
      maximum_number_dimensions: 2
      dimensions:
      - alias: row
        exact_cardinality: 3
      - alias: column
        exact_cardinality: 3
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(1/bar)
    owner: MatrixCompressibilityQuantity
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
    range: CompressibilityUnit

```
</details></div>
