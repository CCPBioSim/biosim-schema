---
search:
  boost: 10.0
---

# Class: CarbohydratePotential

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/CarbohydratePotential](https://CCPBioSim.ac.uk/biosim-schema/CarbohydratePotential)





```{mermaid}
 classDiagram
    class CarbohydratePotential
    click CarbohydratePotential href "../../classes/CarbohydratePotential/"
      CarbohydratePotential : carbohydrate_potential_name





        CarbohydratePotential --> "0..1" CarbohydratePotentialName : carbohydrate_potential_name
        click CarbohydratePotentialName href "../../enums/CarbohydratePotentialName/"



      CarbohydratePotential : modified


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [carbohydrate_potential_name](../slots/carbohydrate_potential_name.md) | 0..1 <br/> [CarbohydratePotentialName](../enums/CarbohydratePotentialName.md) | Force field used to describe carbohydrate | direct |
| [modified](../slots/modified.md) | 0..1 <br/> [boolean](../types/boolean.md) | Has the initial model been modified from the original? | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PotentialMetadata](../classes/PotentialMetadata.md) | [carbohydrate_potential](../slots/carbohydrate_potential.md) | range | [CarbohydratePotential](../classes/CarbohydratePotential.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/CarbohydratePotential |
| native | https://CCPBioSim.ac.uk/biosim-schema/CarbohydratePotential |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CarbohydratePotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- carbohydrate_potential_name
- modified

```
</details>

### Induced

<details>
```yaml
name: CarbohydratePotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  carbohydrate_potential_name:
    name: carbohydrate_potential_name
    description: Force field used to describe carbohydrate.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: CarbohydratePotential
    domain_of:
    - CarbohydratePotential
    range: CarbohydratePotentialName
  modified:
    name: modified
    description: Has the initial model been modified from the original?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: CarbohydratePotential
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
