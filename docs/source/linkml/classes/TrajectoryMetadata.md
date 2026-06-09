---
search:
  boost: 10.0
---

# Class: TrajectoryMetadata

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/TrajectoryMetadata](https://CCPBioSim.ac.uk/biosim-schema/TrajectoryMetadata)





```{mermaid}
 classDiagram
    class TrajectoryMetadata
    click TrajectoryMetadata href "../../classes/TrajectoryMetadata/"
      TrajectoryMetadata : simulation_box





        TrajectoryMetadata --> "0..1" SimulationBox : simulation_box
        click SimulationBox href "../../classes/SimulationBox/"



      TrajectoryMetadata : trajectory_output





        TrajectoryMetadata --> "0..1" Trajectories : trajectory_output
        click Trajectories href "../../classes/Trajectories/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [simulation_box](../slots/simulation_box.md) | 0..1 <br/> [SimulationBox](../classes/SimulationBox.md) | Information about the simulation box | direct |
| [trajectory_output](../slots/trajectory_output.md) | 0..1 <br/> [Trajectories](../classes/Trajectories.md) | Information included in trajectory files | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationMetadata](../classes/SimulationMetadata.md) | [trajectory](../slots/trajectory.md) | range | [TrajectoryMetadata](../classes/TrajectoryMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/TrajectoryMetadata |
| native | https://CCPBioSim.ac.uk/biosim-schema/TrajectoryMetadata |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TrajectoryMetadata
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- simulation_box
- trajectory_output

```
</details>

### Induced

<details>
```yaml
name: TrajectoryMetadata
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  simulation_box:
    name: simulation_box
    description: Information about the simulation box.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: TrajectoryMetadata
    domain_of:
    - TrajectoryMetadata
    range: SimulationBox
  trajectory_output:
    name: trajectory_output
    description: Information included in trajectory files.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: TrajectoryMetadata
    domain_of:
    - TrajectoryMetadata
    range: Trajectories

```
</details></div>
