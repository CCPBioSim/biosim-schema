---
search:
  boost: 10.0
---

# Class: ChargeQuantity

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/ChargeQuantity](https://CCPBioSim.ac.uk/biosim-schema/ChargeQuantity)





```{mermaid}
 classDiagram
    class ChargeQuantity
    click ChargeQuantity href "../../classes/ChargeQuantity/"
      ChargeQuantity : value

      ChargeQuantity : value_unit





        ChargeQuantity --> "0..1" ChargeUnit : value_unit
        click ChargeUnit href "../../enums/ChargeUnit/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](../slots/value.md) | 0..1 <br/> [float](../types/float.md) |  | direct |
| [value_unit](../slots/value_unit.md) | 0..1 <br/> [ChargeUnit](../enums/ChargeUnit.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MoleculeID](../classes/MoleculeID.md) | [molecule_charge](../slots/molecule_charge.md) | range | [ChargeQuantity](../classes/ChargeQuantity.md) |
| [Particles](../classes/Particles.md) | [system_charge](../slots/system_charge.md) | range | [ChargeQuantity](../classes/ChargeQuantity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/ChargeQuantity |
| native | https://CCPBioSim.ac.uk/biosim-schema/ChargeQuantity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChargeQuantity
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
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(e)
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
    range: ChargeUnit

```
</details>

### Induced

<details>
```yaml
name: ChargeQuantity
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  value:
    name: value
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    owner: ChargeQuantity
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
  value_unit:
    name: value_unit
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/quantities
    ifabsent: string(e)
    owner: ChargeQuantity
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
    range: ChargeUnit

```
</details></div>
