---
search:
  boost: 10.0
---

# Class: LipidPotential

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/LipidPotential](https://CCPBioSim.ac.uk/biosim-schema/LipidPotential)





```{mermaid}
 classDiagram
    class LipidPotential
    click LipidPotential href "../../classes/LipidPotential/"
      LipidPotential : lipid_potential_name





        LipidPotential --> "0..1" LipidPotentialName : lipid_potential_name
        click LipidPotentialName href "../../enums/LipidPotentialName/"



      LipidPotential : modified


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [lipid_potential_name](../slots/lipid_potential_name.md) | 0..1 <br/> [LipidPotentialName](../enums/LipidPotentialName.md) | Force field used to describe lipids | direct |
| [modified](../slots/modified.md) | 0..1 <br/> [boolean](../types/boolean.md) | Has the initial model been modified from the original? | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PotentialMetadata](../classes/PotentialMetadata.md) | [lipid_potential](../slots/lipid_potential.md) | range | [LipidPotential](../classes/LipidPotential.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/LipidPotential |
| native | https://CCPBioSim.ac.uk/biosim-schema/LipidPotential |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LipidPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- lipid_potential_name
- modified

```
</details>

### Induced

<details>
```yaml
name: LipidPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  lipid_potential_name:
    name: lipid_potential_name
    description: Force field used to describe lipids.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: LipidPotential
    domain_of:
    - LipidPotential
    range: LipidPotentialName
  modified:
    name: modified
    description: Has the initial model been modified from the original?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: LipidPotential
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
