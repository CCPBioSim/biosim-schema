---
search:
  boost: 10.0
---

# Class: SimulationBox

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/SimulationBox](https://CCPBioSim.ac.uk/biosim-schema/SimulationBox)





```{mermaid}
 classDiagram
    class SimulationBox
    click SimulationBox href "../../classes/SimulationBox/"
      SimulationBox : box_angles





        SimulationBox --> "0..1" VectorAngleQuantity : box_angles
        click VectorAngleQuantity href "../../classes/VectorAngleQuantity/"



      SimulationBox : box_dimensions





        SimulationBox --> "0..1" VectorLengthQuantity : box_dimensions
        click VectorLengthQuantity href "../../classes/VectorLengthQuantity/"



      SimulationBox : box_type





        SimulationBox --> "0..1" BoxType : box_type
        click BoxType href "../../enums/BoxType/"



      SimulationBox : periodic_boundary_conditions





        SimulationBox --> "0..1" PeriodicBoundaryConditions : periodic_boundary_conditions
        click PeriodicBoundaryConditions href "../../enums/PeriodicBoundaryConditions/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [box_dimensions](../slots/box_dimensions.md) | 0..1 <br/> [VectorLengthQuantity](../classes/VectorLengthQuantity.md) | The lengths/dimensions of the box used to simulate the system | direct |
| [box_angles](../slots/box_angles.md) | 0..1 <br/> [VectorAngleQuantity](../classes/VectorAngleQuantity.md) | The angles of the box used to simulate the system | direct |
| [box_type](../slots/box_type.md) | 0..1 <br/> [BoxType](../enums/BoxType.md) | The type of box used to simuluate the system | direct |
| [periodic_boundary_conditions](../slots/periodic_boundary_conditions.md) | 0..1 <br/> [PeriodicBoundaryConditions](../enums/PeriodicBoundaryConditions.md) | What directions in a simulation cell periodic boundaries are set if they are ... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TrajectoryMetadata](../classes/TrajectoryMetadata.md) | [simulation_box](../slots/simulation_box.md) | range | [SimulationBox](../classes/SimulationBox.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/SimulationBox |
| native | https://CCPBioSim.ac.uk/biosim-schema/SimulationBox |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SimulationBox
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- box_dimensions
- box_angles
- box_type
- periodic_boundary_conditions

```
</details>

### Induced

<details>
```yaml
name: SimulationBox
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  box_dimensions:
    name: box_dimensions
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: box_dimensions
          unit: Ang
    description: The lengths/dimensions of the box used to simulate the system.
    examples:
    - value: '[10, 10, 10]'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationBox
    domain_of:
    - SimulationBox
    range: VectorLengthQuantity
  box_angles:
    name: box_angles
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: box_angles
          unit: degrees
    description: The angles of the box used to simulate the system.
    examples:
    - value: '[90, 90, 90]'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationBox
    domain_of:
    - SimulationBox
    range: VectorAngleQuantity
  box_type:
    name: box_type
    description: The type of box used to simuluate the system.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationBox
    domain_of:
    - SimulationBox
    range: BoxType
  periodic_boundary_conditions:
    name: periodic_boundary_conditions
    description: What directions in a simulation cell periodic boundaries are set
      if they are turned on.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationBox
    domain_of:
    - SimulationBox
    range: PeriodicBoundaryConditions

```
</details></div>
