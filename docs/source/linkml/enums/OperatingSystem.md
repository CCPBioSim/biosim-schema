---
search:
  boost: 2.0
---


# Enum: OperatingSystem




_List of operating systems installed on the hardware used to perform the simulation._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/OperatingSystem](https://CCPBioSim.ac.uk/biosim-schema/OperatingSystem)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Linux | None | Unix-like operating systems commonly used for molecular dynamics on workstati... |
| macOS | None | Apple Unix-based operating system, often used for local development, testing,... |
| Windows | None | Microsoft operating system used for desktop workflows; molecular dynamics too... |




## Slots

| Name | Description |
| ---  | --- |
| [operating_system](../slots/operating_system.md) | Operating system installed on the hardware used to perform the simulation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: OperatingSystem
description: List of operating systems installed on the hardware used to perform the
  simulation.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Linux:
    text: Linux
    description: Unix-like operating systems commonly used for molecular dynamics
      on workstations, HPC clusters, and cloud environments.
  macOS:
    text: macOS
    description: Apple Unix-based operating system, often used for local development,
      testing, and smaller-scale molecular dynamics workflows.
  Windows:
    text: Windows
    description: Microsoft operating system used for desktop workflows; molecular
      dynamics tools are often run via native builds, virtual machines, or Linux compatibility
      layers.

```
</details>

</div>
