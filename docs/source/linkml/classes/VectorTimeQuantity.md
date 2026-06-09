---
search:
  boost: 10.0
---

# Class: VectorTimeQuantity


_Time values for multiple coupling groups_



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/VectorTimeQuantity](https://CCPBioSim.ac.uk/biosim-schema/VectorTimeQuantity)





```{mermaid}
 classDiagram
    class VectorTimeQuantity
    click VectorTimeQuantity href "../../classes/VectorTimeQuantity/"
      VectorTimeQuantity : value_unit





        VectorTimeQuantity --> "0..1" TimeUnit : value_unit
        click TimeUnit href "../../enums/TimeUnit/"



      VectorTimeQuantity : vector_value


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [vector_value](../slots/vector_value.md) | * <br/> [float](../types/float.md) |  | direct |
| [value_unit](../slots/value_unit.md) | 0..1 <br/> [TimeUnit](../enums/TimeUnit.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Thermostat](../classes/Thermostat.md) | [temperature_time_constant](../slots/temperature_time_constant.md) | range | [VectorTimeQuantity](../classes/VectorTimeQuantity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/VectorTimeQuantity |
| native | https://CCPBioSim.ac.uk/biosim-schema/VectorTimeQuantity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VectorTimeQuantity
description: Time values for multiple coupling groups
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
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(ns)
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
    range: TimeUnit

```
</details>

### Induced

<details>
```yaml
name: VectorTimeQuantity
description: Time values for multiple coupling groups
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  vector_value:
    name: vector_value
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    owner: VectorTimeQuantity
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
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(ns)
    owner: VectorTimeQuantity
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
    range: TimeUnit

```
</details></div>
