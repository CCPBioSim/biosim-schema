---
search:
  boost: 10.0
---

# Class: SystemCounts

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/SystemCounts](https://CCPBioSim.ac.uk/biosim-schema/SystemCounts)





```{mermaid}
 classDiagram
    class SystemCounts
    click SystemCounts href "../../classes/SystemCounts/"
      SystemCounts : salt_concentration





        SystemCounts --> "0..1" ConcentrationQuantity : salt_concentration
        click ConcentrationQuantity href "../../classes/ConcentrationQuantity/"



      SystemCounts : total_atom_count

      SystemCounts : total_molecule_count

      SystemCounts : unique_molecule_count


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [total_molecule_count](../slots/total_molecule_count.md) | 0..1 <br/> [integer](../types/integer.md) | Total number of simulated molecules, defined as bonded atoms or beads | direct |
| [total_atom_count](../slots/total_atom_count.md) | 0..1 <br/> [integer](../types/integer.md) | Total number of atoms in the simulation | direct |
| [unique_molecule_count](../slots/unique_molecule_count.md) | 0..1 <br/> [integer](../types/integer.md) | Number of unique simulated molecules, defined as bonded atoms or beads | direct |
| [salt_concentration](../slots/salt_concentration.md) | 0..1 <br/> [ConcentrationQuantity](../classes/ConcentrationQuantity.md) | Concentration of salt in the solution | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SystemComposition](../classes/SystemComposition.md) | [system_counts](../slots/system_counts.md) | range | [SystemCounts](../classes/SystemCounts.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/SystemCounts |
| native | https://CCPBioSim.ac.uk/biosim-schema/SystemCounts |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SystemCounts
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- total_molecule_count
- total_atom_count
- unique_molecule_count
- salt_concentration

```
</details>

### Induced

<details>
```yaml
name: SystemCounts
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  total_molecule_count:
    name: total_molecule_count
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: total_molecule_count
    description: Total number of simulated molecules, defined as bonded atoms or beads.
    examples:
    - value: '1'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SystemCounts
    domain_of:
    - SystemCounts
    range: integer
    minimum_value: 0
  total_atom_count:
    name: total_atom_count
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: total_atom_count
    description: Total number of atoms in the simulation.
    examples:
    - value: '1'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SystemCounts
    domain_of:
    - SystemCounts
    range: integer
    minimum_value: 0
  unique_molecule_count:
    name: unique_molecule_count
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: unique_molecule_count
    description: Number of unique simulated molecules, defined as bonded atoms or
      beads.
    examples:
    - value: '1'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SystemCounts
    domain_of:
    - SystemCounts
    range: integer
    minimum_value: 0
  salt_concentration:
    name: salt_concentration
    description: Concentration of salt in the solution.
    examples:
    - value: '1'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SystemCounts
    domain_of:
    - SystemCounts
    range: ConcentrationQuantity

```
</details></div>
