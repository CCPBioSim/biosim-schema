---
search:
  boost: 10.0
---

# Class: PolymerPotential

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/PolymerPotential](https://CCPBioSim.ac.uk/biosim-schema/PolymerPotential)





```{mermaid}
 classDiagram
    class PolymerPotential
    click PolymerPotential href "../../classes/PolymerPotential/"
      PolymerPotential : modified

      PolymerPotential : polymer_potential_name





        PolymerPotential --> "0..1" PolymerPotentialName : polymer_potential_name
        click PolymerPotentialName href "../../enums/PolymerPotentialName/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [polymer_potential_name](../slots/polymer_potential_name.md) | 0..1 <br/> [PolymerPotentialName](../enums/PolymerPotentialName.md) | Force field used to describe polymers (excluding proteins and nucleic acids) | direct |
| [modified](../slots/modified.md) | 0..1 <br/> [boolean](../types/boolean.md) | Has the initial model been modified from the original? | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PotentialMetadata](../classes/PotentialMetadata.md) | [polymer_potential](../slots/polymer_potential.md) | range | [PolymerPotential](../classes/PolymerPotential.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/PolymerPotential |
| native | https://CCPBioSim.ac.uk/biosim-schema/PolymerPotential |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PolymerPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- polymer_potential_name
- modified

```
</details>

### Induced

<details>
```yaml
name: PolymerPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  polymer_potential_name:
    name: polymer_potential_name
    description: Force field used to describe polymers (excluding proteins and nucleic
      acids).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PolymerPotential
    domain_of:
    - PolymerPotential
    range: PolymerPotentialName
  modified:
    name: modified
    description: Has the initial model been modified from the original?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PolymerPotential
    domain_of:
    - MoleculeID
    - WaterPotential
    - ProteinPotential
    - LipidPotential
    - NucleicPotential
    - CarbohydratePotential
    - PolymerPotential
    - GeneralPotential
    - MachineLearnedPotential
    range: boolean

```
</details></div>
