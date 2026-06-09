---
search:
  boost: 10.0
---

# Class: Software

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Software](https://CCPBioSim.ac.uk/biosim-schema/Software)





```{mermaid}
 classDiagram
    class Software
    click Software href "../../classes/Software/"
      Software : container_runtime





        Software --> "0..1" ContainerRuntime : container_runtime
        click ContainerRuntime href "../../enums/ContainerRuntime/"



      Software : MPI_library





        Software --> "0..1" MPILibrary : MPI_library
        click MPILibrary href "../../enums/MPILibrary/"



      Software : operating_system





        Software --> "0..1" OperatingSystem : operating_system
        click OperatingSystem href "../../enums/OperatingSystem/"



      Software : scheduler





        Software --> "0..1" Scheduler : scheduler
        click Scheduler href "../../enums/Scheduler/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [operating_system](../slots/operating_system.md) | 0..1 <br/> [OperatingSystem](../enums/OperatingSystem.md) | Operating system installed on the hardware used to perform the simulation | direct |
| [scheduler](../slots/scheduler.md) | 0..1 <br/> [Scheduler](../enums/Scheduler.md) | Workload manager or job scheduler used to launch the simulation | direct |
| [MPI_library](../slots/MPI_library.md) | 0..1 <br/> [MPILibrary](../enums/MPILibrary.md) | MPI implementation used for distributed parallel execution | direct |
| [container_runtime](../slots/container_runtime.md) | 0..1 <br/> [ContainerRuntime](../enums/ContainerRuntime.md) | Container runtime used to execute the simulation environment, if any | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ComputationalEnvironment](../classes/ComputationalEnvironment.md) | [software](../slots/software.md) | range | [Software](../classes/Software.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Software |
| native | https://CCPBioSim.ac.uk/biosim-schema/Software |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Software
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- operating_system
- scheduler
- MPI_library
- container_runtime

```
</details>

### Induced

<details>
```yaml
name: Software
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  operating_system:
    name: operating_system
    description: Operating system installed on the hardware used to perform the simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Software
    domain_of:
    - Software
    range: OperatingSystem
  scheduler:
    name: scheduler
    description: Workload manager or job scheduler used to launch the simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Software
    domain_of:
    - Software
    range: Scheduler
  MPI_library:
    name: MPI_library
    description: MPI implementation used for distributed parallel execution.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Software
    domain_of:
    - Software
    range: MPILibrary
  container_runtime:
    name: container_runtime
    description: Container runtime used to execute the simulation environment, if
      any.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Software
    domain_of:
    - Software
    range: ContainerRuntime

```
</details></div>
