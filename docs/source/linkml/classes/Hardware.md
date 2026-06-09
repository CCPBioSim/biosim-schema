---
search:
  boost: 10.0
---

# Class: Hardware

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Hardware](https://CCPBioSim.ac.uk/biosim-schema/Hardware)





```{mermaid}
 classDiagram
    class Hardware
    click Hardware href "../../classes/Hardware/"
      Hardware : cores_per_socket

      Hardware : CPU_architecture





        Hardware --> "0..1" CpuArchitecture : CPU_architecture
        click CpuArchitecture href "../../enums/CpuArchitecture/"



      Hardware : CPU_vendor





        Hardware --> "0..1" CpuVendor : CPU_vendor
        click CpuVendor href "../../enums/CpuVendor/"



      Hardware : execution_platform





        Hardware --> "0..1" ExecutionPlatform : execution_platform
        click ExecutionPlatform href "../../enums/ExecutionPlatform/"



      Hardware : GPU_vendor





        Hardware --> "0..1" GpuVendor : GPU_vendor
        click GpuVendor href "../../enums/GpuVendor/"



      Hardware : GPUs_per_node

      Hardware : memory_per_node





        Hardware --> "0..1" ByteQuantity : memory_per_node
        click ByteQuantity href "../../classes/ByteQuantity/"



      Hardware : node_count

      Hardware : node_type





        Hardware --> "0..1" NodeType : node_type
        click NodeType href "../../enums/NodeType/"



      Hardware : sockets_per_node

      Hardware : threads_per_core


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [execution_platform](../slots/execution_platform.md) | 0..1 <br/> [ExecutionPlatform](../enums/ExecutionPlatform.md) | Broad type of system used to run the simulation workload | direct |
| [node_type](../slots/node_type.md) | 0..1 <br/> [NodeType](../enums/NodeType.md) | Compute node profile used for the simulation run | direct |
| [node_count](../slots/node_count.md) | 0..1 <br/> [integer](../types/integer.md) | Number of compute nodes used for the run | direct |
| [CPU_vendor](../slots/CPU_vendor.md) | 0..1 <br/> [CpuVendor](../enums/CpuVendor.md) | CPU vendor used in the compute nodes | direct |
| [CPU_architecture](../slots/CPU_architecture.md) | 0..1 <br/> [CpuArchitecture](../enums/CpuArchitecture.md) | CPU instruction-set architecture of the compute nodes | direct |
| [sockets_per_node](../slots/sockets_per_node.md) | 0..1 <br/> [integer](../types/integer.md) | Number of physical CPU sockets in each compute node | direct |
| [cores_per_socket](../slots/cores_per_socket.md) | 0..1 <br/> [integer](../types/integer.md) | Number of physical CPU cores in each socket | direct |
| [threads_per_core](../slots/threads_per_core.md) | 0..1 <br/> [integer](../types/integer.md) | Number of hardware threads per physical core | direct |
| [GPU_vendor](../slots/GPU_vendor.md) | 0..1 <br/> [GpuVendor](../enums/GpuVendor.md) | GPU vendor used by the compute nodes, if applicable | direct |
| [GPUs_per_node](../slots/GPUs_per_node.md) | 0..1 <br/> [integer](../types/integer.md) | Number of GPUs present in each compute node | direct |
| [memory_per_node](../slots/memory_per_node.md) | 0..1 <br/> [ByteQuantity](../classes/ByteQuantity.md) | Amount of memory installed per compute node | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ComputationalEnvironment](../classes/ComputationalEnvironment.md) | [hardware](../slots/hardware.md) | range | [Hardware](../classes/Hardware.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Hardware |
| native | https://CCPBioSim.ac.uk/biosim-schema/Hardware |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Hardware
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- execution_platform
- node_type
- node_count
- CPU_vendor
- CPU_architecture
- sockets_per_node
- cores_per_socket
- threads_per_core
- GPU_vendor
- GPUs_per_node
- memory_per_node

```
</details>

### Induced

<details>
```yaml
name: Hardware
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  execution_platform:
    name: execution_platform
    description: Broad type of system used to run the simulation workload.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: ExecutionPlatform
  node_type:
    name: node_type
    description: Compute node profile used for the simulation run.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: NodeType
  node_count:
    name: node_count
    description: Number of compute nodes used for the run.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: integer
    minimum_value: 1
  CPU_vendor:
    name: CPU_vendor
    description: CPU vendor used in the compute nodes.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: CpuVendor
  CPU_architecture:
    name: CPU_architecture
    description: CPU instruction-set architecture of the compute nodes.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: CpuArchitecture
  sockets_per_node:
    name: sockets_per_node
    description: Number of physical CPU sockets in each compute node.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: integer
    minimum_value: 1
  cores_per_socket:
    name: cores_per_socket
    description: Number of physical CPU cores in each socket.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: integer
    minimum_value: 1
  threads_per_core:
    name: threads_per_core
    description: Number of hardware threads per physical core.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: integer
    minimum_value: 1
  GPU_vendor:
    name: GPU_vendor
    description: GPU vendor used by the compute nodes, if applicable.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: GpuVendor
  GPUs_per_node:
    name: GPUs_per_node
    description: Number of GPUs present in each compute node.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: integer
    minimum_value: 0
  memory_per_node:
    name: memory_per_node
    description: Amount of memory installed per compute node.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Hardware
    domain_of:
    - Hardware
    range: ByteQuantity

```
</details></div>
