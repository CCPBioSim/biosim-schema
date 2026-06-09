---
search:
  boost: 2.0
---


# Enum: Scheduler




_Job scheduler used for simulation execution._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/Scheduler](https://CCPBioSim.ac.uk/biosim-schema/Scheduler)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SLURM | None | Slurm Workload Manager |
| PBS | None | Portable Batch System family (PBS Pro/OpenPBS) |
| LSF | None | IBM Spectrum LSF |
| SGE | None | Sun/Grid Engine family |
| None | None | No batch scheduler used |




## Slots

| Name | Description |
| ---  | --- |
| [scheduler](../slots/scheduler.md) | Workload manager or job scheduler used to launch the simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: Scheduler
description: Job scheduler used for simulation execution.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  SLURM:
    text: SLURM
    description: Slurm Workload Manager.
  PBS:
    text: PBS
    description: Portable Batch System family (PBS Pro/OpenPBS).
  LSF:
    text: LSF
    description: IBM Spectrum LSF.
  SGE:
    text: SGE
    description: Sun/Grid Engine family.
  None:
    text: None
    description: No batch scheduler used.

```
</details>

</div>
