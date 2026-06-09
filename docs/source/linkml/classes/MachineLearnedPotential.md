---
search:
  boost: 10.0
---

# Class: MachineLearnedPotential

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/MachineLearnedPotential](https://CCPBioSim.ac.uk/biosim-schema/MachineLearnedPotential)





```{mermaid}
 classDiagram
    class MachineLearnedPotential
    click MachineLearnedPotential href "../../classes/MachineLearnedPotential/"
      MachineLearnedPotential : machine_learned_potential_name





        MachineLearnedPotential --> "0..1" MachineLearnedPotentialName : machine_learned_potential_name
        click MachineLearnedPotentialName href "../../enums/MachineLearnedPotentialName/"



      MachineLearnedPotential : modified


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [machine_learned_potential_name](../slots/machine_learned_potential_name.md) | 0..1 <br/> [MachineLearnedPotentialName](../enums/MachineLearnedPotentialName.md) | ML force field used to describe molecules | direct |
| [modified](../slots/modified.md) | 0..1 <br/> [boolean](../types/boolean.md) | Has the initial model been modified from the original? | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PotentialMetadata](../classes/PotentialMetadata.md) | [machine_learned_potential](../slots/machine_learned_potential.md) | range | [MachineLearnedPotential](../classes/MachineLearnedPotential.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/MachineLearnedPotential |
| native | https://CCPBioSim.ac.uk/biosim-schema/MachineLearnedPotential |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MachineLearnedPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- machine_learned_potential_name
- modified

```
</details>

### Induced

<details>
```yaml
name: MachineLearnedPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  machine_learned_potential_name:
    name: machine_learned_potential_name
    description: ML force field used to describe molecules.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MachineLearnedPotential
    domain_of:
    - MachineLearnedPotential
    range: MachineLearnedPotentialName
  modified:
    name: modified
    description: Has the initial model been modified from the original?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MachineLearnedPotential
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
