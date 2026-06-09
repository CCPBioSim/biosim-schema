---
search:
  boost: 10.0
---

# Class: WaterPotential

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/WaterPotential](https://CCPBioSim.ac.uk/biosim-schema/WaterPotential)





```{mermaid}
 classDiagram
    class WaterPotential
    click WaterPotential href "../../classes/WaterPotential/"
      WaterPotential : modified

      WaterPotential : water_potential_name





        WaterPotential --> "0..1" WaterPotentialName : water_potential_name
        click WaterPotentialName href "../../enums/WaterPotentialName/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [water_potential_name](../slots/water_potential_name.md) | 0..1 <br/> [WaterPotentialName](../enums/WaterPotentialName.md) | Force field used to describe water molecules | direct |
| [modified](../slots/modified.md) | 0..1 <br/> [boolean](../types/boolean.md) | Has the initial model been modified from the original? | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PotentialMetadata](../classes/PotentialMetadata.md) | [water_potential](../slots/water_potential.md) | range | [WaterPotential](../classes/WaterPotential.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/WaterPotential |
| native | https://CCPBioSim.ac.uk/biosim-schema/WaterPotential |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WaterPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- water_potential_name
- modified

```
</details>

### Induced

<details>
```yaml
name: WaterPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  water_potential_name:
    name: water_potential_name
    description: Force field used to describe water molecules.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: WaterPotential
    domain_of:
    - WaterPotential
    range: WaterPotentialName
  modified:
    name: modified
    description: Has the initial model been modified from the original?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: WaterPotential
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
