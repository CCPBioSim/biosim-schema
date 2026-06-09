---
search:
  boost: 10.0
---

# Class: Connectivity

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Connectivity](https://CCPBioSim.ac.uk/biosim-schema/Connectivity)





```{mermaid}
 classDiagram
    class Connectivity
    click Connectivity href "../../classes/Connectivity/"
      Connectivity : bonds

      Connectivity : dihedrals


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [bonds](../slots/bonds.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are bond parameters present in the topology? | direct |
| [dihedrals](../slots/dihedrals.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are dihedral parameters present in the topology? | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TopologyMetadata](../classes/TopologyMetadata.md) | [connectivity](../slots/connectivity.md) | range | [Connectivity](../classes/Connectivity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Connectivity |
| native | https://CCPBioSim.ac.uk/biosim-schema/Connectivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Connectivity
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- bonds
- dihedrals

```
</details>

### Induced

<details>
```yaml
name: Connectivity
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  bonds:
    name: bonds
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: bonds
    description: Are bond parameters present in the topology?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Connectivity
    domain_of:
    - Connectivity
    range: boolean
  dihedrals:
    name: dihedrals
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: dihedrals
    description: Are dihedral parameters present in the topology?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Connectivity
    domain_of:
    - Connectivity
    range: boolean

```
</details></div>
