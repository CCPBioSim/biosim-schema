---
search:
  boost: 2.0
---


# Enum: BoxType




_Types of box used to simulate the system._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/BoxType](https://CCPBioSim.ac.uk/biosim-schema/BoxType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Cubic | None |  |
| Tetragonal | None |  |
| Orthorhombic | None |  |
| Truncated Octahedron | None |  |
| Triclinic | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [box_type](../slots/box_type.md) | The type of box used to simuluate the system |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: BoxType
description: Types of box used to simulate the system.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  Cubic:
    text: Cubic
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: box_type
          value: cubic
    aliases:
    - Cubic
    - cubic
  Tetragonal:
    text: Tetragonal
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: box_type
          value: tetragonal
    aliases:
    - Tetragonal
    - tetragonal
  Orthorhombic:
    text: Orthorhombic
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: box_type
          value: orthorhombic
    aliases:
    - Orthorhombic
    - orthorhombic
  Truncated Octahedron:
    text: Truncated Octahedron
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: box_type
          value: truncated octahedron
    aliases:
    - Truncated Octahedron
    - truncated_octahedron
  Triclinic:
    text: Triclinic
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: box_type
          value: triclinic
    aliases:
    - Triclinic
    - triclinic

```
</details>

</div>
