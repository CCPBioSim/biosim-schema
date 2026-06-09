---
search:
  boost: 10.0
---

# Class: GeneralPotential

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/GeneralPotential](https://CCPBioSim.ac.uk/biosim-schema/GeneralPotential)





```{mermaid}
 classDiagram
    class GeneralPotential
    click GeneralPotential href "../../classes/GeneralPotential/"
      GeneralPotential : general_potential_name





        GeneralPotential --> "0..1" GeneralPotentialName : general_potential_name
        click GeneralPotentialName href "../../enums/GeneralPotentialName/"



      GeneralPotential : modified


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [general_potential_name](../slots/general_potential_name.md) | 0..1 <br/> [GeneralPotentialName](../enums/GeneralPotentialName.md) | Force field used to describe molecules | direct |
| [modified](../slots/modified.md) | 0..1 <br/> [boolean](../types/boolean.md) | Has the initial model been modified from the original? | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PotentialMetadata](../classes/PotentialMetadata.md) | [general_potential](../slots/general_potential.md) | range | [GeneralPotential](../classes/GeneralPotential.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/GeneralPotential |
| native | https://CCPBioSim.ac.uk/biosim-schema/GeneralPotential |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneralPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- general_potential_name
- modified

```
</details>

### Induced

<details>
```yaml
name: GeneralPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  general_potential_name:
    name: general_potential_name
    description: Force field used to describe molecules.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: GeneralPotential
    domain_of:
    - GeneralPotential
    range: GeneralPotentialName
  modified:
    name: modified
    description: Has the initial model been modified from the original?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: GeneralPotential
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
