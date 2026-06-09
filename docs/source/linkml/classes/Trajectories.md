---
search:
  boost: 10.0
---

# Class: Trajectories

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Trajectories](https://CCPBioSim.ac.uk/biosim-schema/Trajectories)





```{mermaid}
 classDiagram
    class Trajectories
    click Trajectories href "../../classes/Trajectories/"
      Trajectories : energies

      Trajectories : forces

      Trajectories : frame_count

      Trajectories : polarizable_charges

      Trajectories : positions

      Trajectories : replica

      Trajectories : velocities

      Trajectories : water


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [positions](../slots/positions.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are per-frame positions included in the trajectory? | direct |
| [forces](../slots/forces.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are per-frame forces included in the trajectory? | direct |
| [velocities](../slots/velocities.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are per-frame velocities included in the trajectory? | direct |
| [polarizable_charges](../slots/polarizable_charges.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are per-frame polarizable charges included in the trajectory? | direct |
| [energies](../slots/energies.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are per-frame energies included in the trajectory? | direct |
| [water](../slots/water.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are water molecules included in the trajectory? | direct |
| [replica](../slots/replica.md) | 0..1 <br/> [boolean](../types/boolean.md) | Is this trajectory a replica of another provided trajectory? | direct |
| [frame_count](../slots/frame_count.md) | 0..1 <br/> [integer](../types/integer.md) | Total number of snapshots that make up a trajectory | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TrajectoryMetadata](../classes/TrajectoryMetadata.md) | [trajectory_output](../slots/trajectory_output.md) | range | [Trajectories](../classes/Trajectories.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Trajectories |
| native | https://CCPBioSim.ac.uk/biosim-schema/Trajectories |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Trajectories
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- positions
- forces
- velocities
- polarizable_charges
- energies
- water
- replica
- frame_count

```
</details>

### Induced

<details>
```yaml
name: Trajectories
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  positions:
    name: positions
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: positions
    description: Are per-frame positions included in the trajectory?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Trajectories
    domain_of:
    - Trajectories
    range: boolean
  forces:
    name: forces
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: forces
    description: Are per-frame forces included in the trajectory?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Trajectories
    domain_of:
    - Trajectories
    range: boolean
  velocities:
    name: velocities
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: velocities
    description: Are per-frame velocities included in the trajectory?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Trajectories
    domain_of:
    - Trajectories
    range: boolean
  polarizable_charges:
    name: polarizable_charges
    description: Are per-frame polarizable charges included in the trajectory?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Trajectories
    domain_of:
    - Trajectories
    range: boolean
  energies:
    name: energies
    description: Are per-frame energies included in the trajectory?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Trajectories
    domain_of:
    - Trajectories
    range: boolean
  water:
    name: water
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: water
    description: Are water molecules included in the trajectory?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Trajectories
    domain_of:
    - Trajectories
    range: boolean
  replica:
    name: replica
    description: Is this trajectory a replica of another provided trajectory?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Trajectories
    domain_of:
    - Trajectories
    range: boolean
  frame_count:
    name: frame_count
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: frame_count
    description: Total number of snapshots that make up a trajectory.
    examples:
    - value: '1'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Trajectories
    domain_of:
    - Trajectories
    range: integer
    minimum_value: 0

```
</details></div>
