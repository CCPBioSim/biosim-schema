---
search:
  boost: 10.0
---

# Class: Integrator

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Integrator](https://CCPBioSim.ac.uk/biosim-schema/Integrator)





```{mermaid}
 classDiagram
    class Integrator
    click Integrator href "../../classes/Integrator/"
      Integrator : frame_step





        Integrator --> "0..1" TimeQuantity : frame_step
        click TimeQuantity href "../../classes/TimeQuantity/"



      Integrator : integrator_algorithm





        Integrator --> "0..1" IntegratorAlgorithm : integrator_algorithm
        click IntegratorAlgorithm href "../../enums/IntegratorAlgorithm/"



      Integrator : number_of_steps

      Integrator : simulation_time





        Integrator --> "0..1" TimeQuantity : simulation_time
        click TimeQuantity href "../../classes/TimeQuantity/"



      Integrator : time_step





        Integrator --> "0..1" TimeQuantity : time_step
        click TimeQuantity href "../../classes/TimeQuantity/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [integrator_algorithm](../slots/integrator_algorithm.md) | 0..1 <br/> [IntegratorAlgorithm](../enums/IntegratorAlgorithm.md) | List of integrator algorithms used to integrate the simulation | direct |
| [frame_step](../slots/frame_step.md) | 0..1 <br/> [TimeQuantity](../classes/TimeQuantity.md) | Time between saved snapshots/frames in a simulation, given as a float | direct |
| [time_step](../slots/time_step.md) | 0..1 <br/> [TimeQuantity](../classes/TimeQuantity.md) | Time between integration steps in a simulation, given as a float | direct |
| [number_of_steps](../slots/number_of_steps.md) | 0..1 <br/> [integer](../types/integer.md) | Number of integration steps performed in the simulation, given as an integer | direct |
| [simulation_time](../slots/simulation_time.md) | 0..1 <br/> [TimeQuantity](../classes/TimeQuantity.md) | Total time molecular dynamics have been sampled in a simulation trajectory, o... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationSettings](../classes/SimulationSettings.md) | [integrator](../slots/integrator.md) | range | [Integrator](../classes/Integrator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Integrator |
| native | https://CCPBioSim.ac.uk/biosim-schema/Integrator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Integrator
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- integrator_algorithm
- frame_step
- time_step
- number_of_steps
- simulation_time

```
</details>

### Induced

<details>
```yaml
name: Integrator
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  integrator_algorithm:
    name: integrator_algorithm
    description: List of integrator algorithms used to integrate the simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Integrator
    domain_of:
    - Integrator
    range: IntegratorAlgorithm
  frame_step:
    name: frame_step
    description: Time between saved snapshots/frames in a simulation, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Integrator
    domain_of:
    - Integrator
    range: TimeQuantity
  time_step:
    name: time_step
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: dt
          unit: ps
        - engine: gromacs
          key: dt
          unit: ps
        - engine: lammps
          key: timestep
          unit: fs
    description: Time between integration steps in a simulation, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - Integration Step
    - Time Step
    - dT
    rank: 1000
    owner: Integrator
    domain_of:
    - Integrator
    range: TimeQuantity
  number_of_steps:
    name: number_of_steps
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: nstlim
        - engine: gromacs
          key: nsteps
    description: Number of integration steps performed in the simulation, given as
      an integer.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Integrator
    domain_of:
    - Integrator
    range: integer
  simulation_time:
    name: simulation_time
    description: Total time molecular dynamics have been sampled in a simulation trajectory,
      often given by the number of integration steps multiplied by the simulation
      time step used by the integrator, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Integrator
    domain_of:
    - Integrator
    range: TimeQuantity

```
</details></div>
