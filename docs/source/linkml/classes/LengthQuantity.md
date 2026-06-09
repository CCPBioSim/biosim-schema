---
search:
  boost: 10.0
---

# Class: LengthQuantity

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/LengthQuantity](https://CCPBioSim.ac.uk/biosim-schema/LengthQuantity)





```{mermaid}
 classDiagram
    class LengthQuantity
    click LengthQuantity href "../../classes/LengthQuantity/"
      LengthQuantity : value

      LengthQuantity : value_unit





        LengthQuantity --> "0..1" LengthUnit : value_unit
        click LengthUnit href "../../enums/LengthUnit/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](../slots/value.md) | 0..1 <br/> [float](../types/float.md) |  | direct |
| [value_unit](../slots/value_unit.md) | 0..1 <br/> [LengthUnit](../enums/LengthUnit.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Minimisation](../classes/Minimisation.md) | [minimisation_distance_step_size](../slots/minimisation_distance_step_size.md) | range | [LengthQuantity](../classes/LengthQuantity.md) |
| [Interactions](../classes/Interactions.md) | [electrostatic_cutoff_distance](../slots/electrostatic_cutoff_distance.md) | range | [LengthQuantity](../classes/LengthQuantity.md) |
| [Interactions](../classes/Interactions.md) | [vdw_cutoff_distance](../slots/vdw_cutoff_distance.md) | range | [LengthQuantity](../classes/LengthQuantity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/LengthQuantity |
| native | https://CCPBioSim.ac.uk/biosim-schema/LengthQuantity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LengthQuantity
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  value:
    name: value
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
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
    range: float
    minimum_value: 0
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
name: LengthQuantity
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  value:
    name: value
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    owner: LengthQuantity
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
    range: float
    minimum_value: 0
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(nm)
    owner: LengthQuantity
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
