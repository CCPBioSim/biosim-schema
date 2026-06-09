---
search:
  boost: 2.0
---


# Enum: MPILibrary




_MPI implementation used for message passing._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/MPILibrary](https://CCPBioSim.ac.uk/biosim-schema/MPILibrary)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| OpenMPI | None | Open source MPI implementation |
| MPICH | None | MPICH MPI implementation |
| IntelMPI | None | Intel MPI implementation |
| MVAPICH2 | None | MVAPICH2 MPI implementation |
| None | None | No MPI library used |




## Slots

| Name | Description |
| ---  | --- |
| [MPI_library](../slots/MPI_library.md) | MPI implementation used for distributed parallel execution |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: MPILibrary
description: MPI implementation used for message passing.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  OpenMPI:
    text: OpenMPI
    description: Open source MPI implementation.
  MPICH:
    text: MPICH
    description: MPICH MPI implementation.
  IntelMPI:
    text: IntelMPI
    description: Intel MPI implementation.
  MVAPICH2:
    text: MVAPICH2
    description: MVAPICH2 MPI implementation.
  None:
    text: None
    description: No MPI library used.

```
</details>

</div>
