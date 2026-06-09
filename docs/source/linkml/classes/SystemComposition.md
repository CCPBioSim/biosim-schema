---
search:
  boost: 10.0
---

# Class: SystemComposition

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/SystemComposition](https://CCPBioSim.ac.uk/biosim-schema/SystemComposition)





```{mermaid}
 classDiagram
    class SystemComposition
    click SystemComposition href "../../classes/SystemComposition/"
      SystemComposition : molecule_ID





        SystemComposition --> "*" MoleculeID : molecule_ID
        click MoleculeID href "../../classes/MoleculeID/"



      SystemComposition : system_counts





        SystemComposition --> "0..1" SystemCounts : system_counts
        click SystemCounts href "../../classes/SystemCounts/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [system_counts](../slots/system_counts.md) | 0..1 <br/> [SystemCounts](../classes/SystemCounts.md) |  | direct |
| [molecule_ID](../slots/molecule_ID.md) | * <br/> [MoleculeID](../classes/MoleculeID.md) | Persistent identifier of a molecule being simulated | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationMetadata](../classes/SimulationMetadata.md) | [composition](../slots/composition.md) | range | [SystemComposition](../classes/SystemComposition.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/SystemComposition |
| native | https://CCPBioSim.ac.uk/biosim-schema/SystemComposition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SystemComposition
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- system_counts
- molecule_ID

```
</details>

### Induced

<details>
```yaml
name: SystemComposition
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  system_counts:
    name: system_counts
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - System Counts
    rank: 1000
    owner: SystemComposition
    domain_of:
    - SystemComposition
    range: SystemCounts
    inlined: true
  molecule_ID:
    name: molecule_ID
    description: Persistent identifier of a molecule being simulated.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - Molecule ID
    rank: 1000
    owner: SystemComposition
    domain_of:
    - SystemComposition
    range: MoleculeID
    multivalued: true
    inlined: true
    maximum_cardinality: 20

```
</details></div>
