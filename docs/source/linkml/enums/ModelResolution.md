---
search:
  boost: 2.0
---


# Enum: ModelResolution




_Resolution of simulated molecules._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/ModelResolution](https://CCPBioSim.ac.uk/biosim-schema/ModelResolution)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| All Atom | None | All atom dynamics modelled in the simulation |
| United Atom | None | Treats non-polar hydrogen atoms as part of the heavier atoms they are bonded ... |
| Coarse-Grained | None | Groups atoms into beads (often 4:1 mapping) as a single entity |
| Mesoscale | None | Larger beads of grouped molecules represented as a single entity |




## Slots

| Name | Description |
| ---  | --- |
| [resolution](../slots/resolution.md) | Resolution of simulated system |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: ModelResolution
description: Resolution of simulated molecules.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  All Atom:
    text: All Atom
    description: All atom dynamics modelled in the simulation.
  United Atom:
    text: United Atom
    description: Treats non-polar hydrogen atoms as part of the heavier atoms they
      are bonded to.
  Coarse-Grained:
    text: Coarse-Grained
    description: Groups atoms into beads (often 4:1 mapping) as a single entity.
  Mesoscale:
    text: Mesoscale
    description: Larger beads of grouped molecules represented as a single entity.

```
</details>

</div>
