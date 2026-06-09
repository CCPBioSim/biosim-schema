---
search:
  boost: 10.0
---

# Class: SimulationMetadata

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/SimulationMetadata](https://CCPBioSim.ac.uk/biosim-schema/SimulationMetadata)





```{mermaid}
 classDiagram
    class SimulationMetadata
    click SimulationMetadata href "../../classes/SimulationMetadata/"
      SimulationMetadata : composition





        SimulationMetadata --> "0..1" SystemComposition : composition
        click SystemComposition href "../../classes/SystemComposition/"



      SimulationMetadata : compute





        SimulationMetadata --> "0..1" ComputationalEnvironment : compute
        click ComputationalEnvironment href "../../classes/ComputationalEnvironment/"



      SimulationMetadata : observables





        SimulationMetadata --> "0..1" SimulationObservables : observables
        click SimulationObservables href "../../classes/SimulationObservables/"



      SimulationMetadata : potentials





        SimulationMetadata --> "0..1" PotentialMetadata : potentials
        click PotentialMetadata href "../../classes/PotentialMetadata/"



      SimulationMetadata : settings





        SimulationMetadata --> "0..1" SimulationSettings : settings
        click SimulationSettings href "../../classes/SimulationSettings/"



      SimulationMetadata : stages





        SimulationMetadata --> "0..1" SimulationStages : stages
        click SimulationStages href "../../classes/SimulationStages/"



      SimulationMetadata : topology





        SimulationMetadata --> "0..1" TopologyMetadata : topology
        click TopologyMetadata href "../../classes/TopologyMetadata/"



      SimulationMetadata : trajectory





        SimulationMetadata --> "0..1" TrajectoryMetadata : trajectory
        click TrajectoryMetadata href "../../classes/TrajectoryMetadata/"




```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Tree Root | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [stages](../slots/stages.md) | 0..1 <br/> [SimulationStages](../classes/SimulationStages.md) |  | direct |
| [settings](../slots/settings.md) | 0..1 <br/> [SimulationSettings](../classes/SimulationSettings.md) |  | direct |
| [observables](../slots/observables.md) | 0..1 <br/> [SimulationObservables](../classes/SimulationObservables.md) |  | direct |
| [topology](../slots/topology.md) | 0..1 <br/> [TopologyMetadata](../classes/TopologyMetadata.md) |  | direct |
| [trajectory](../slots/trajectory.md) | 0..1 <br/> [TrajectoryMetadata](../classes/TrajectoryMetadata.md) |  | direct |
| [composition](../slots/composition.md) | 0..1 <br/> [SystemComposition](../classes/SystemComposition.md) |  | direct |
| [potentials](../slots/potentials.md) | 0..1 <br/> [PotentialMetadata](../classes/PotentialMetadata.md) |  | direct |
| [compute](../slots/compute.md) | 0..1 <br/> [ComputationalEnvironment](../classes/ComputationalEnvironment.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/SimulationMetadata |
| native | https://CCPBioSim.ac.uk/biosim-schema/SimulationMetadata |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SimulationMetadata
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- stages
- settings
- observables
- topology
- trajectory
- composition
- potentials
- compute
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: SimulationMetadata
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  stages:
    name: stages
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationMetadata
    domain_of:
    - SimulationMetadata
    range: SimulationStages
  settings:
    name: settings
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationMetadata
    domain_of:
    - SimulationMetadata
    range: SimulationSettings
  observables:
    name: observables
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationMetadata
    domain_of:
    - SimulationMetadata
    range: SimulationObservables
  topology:
    name: topology
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationMetadata
    domain_of:
    - SimulationMetadata
    range: TopologyMetadata
  trajectory:
    name: trajectory
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationMetadata
    domain_of:
    - SimulationMetadata
    range: TrajectoryMetadata
  composition:
    name: composition
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationMetadata
    domain_of:
    - SimulationMetadata
    range: SystemComposition
  potentials:
    name: potentials
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationMetadata
    domain_of:
    - SimulationMetadata
    range: PotentialMetadata
  compute:
    name: compute
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationMetadata
    domain_of:
    - SimulationMetadata
    range: ComputationalEnvironment
tree_root: true

```
</details></div>
