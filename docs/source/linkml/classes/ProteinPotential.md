---
search:
  boost: 10.0
---

# Class: ProteinPotential

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/ProteinPotential](https://CCPBioSim.ac.uk/biosim-schema/ProteinPotential)





```{mermaid}
 classDiagram
    class ProteinPotential
    click ProteinPotential href "../../classes/ProteinPotential/"
      ProteinPotential : modified

      ProteinPotential : protein_potential_name





        ProteinPotential --> "0..1" ProteinPotentialName : protein_potential_name
        click ProteinPotentialName href "../../enums/ProteinPotentialName/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [protein_potential_name](../slots/protein_potential_name.md) | 0..1 <br/> [ProteinPotentialName](../enums/ProteinPotentialName.md) | Force field used to describe proteins | direct |
| [modified](../slots/modified.md) | 0..1 <br/> [boolean](../types/boolean.md) | Has the initial model been modified from the original? | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PotentialMetadata](../classes/PotentialMetadata.md) | [protein_potential](../slots/protein_potential.md) | range | [ProteinPotential](../classes/ProteinPotential.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/ProteinPotential |
| native | https://CCPBioSim.ac.uk/biosim-schema/ProteinPotential |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProteinPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- protein_potential_name
- modified

```
</details>

### Induced

<details>
```yaml
name: ProteinPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  protein_potential_name:
    name: protein_potential_name
    description: Force field used to describe proteins.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: ProteinPotential
    domain_of:
    - ProteinPotential
    range: ProteinPotentialName
  modified:
    name: modified
    description: Has the initial model been modified from the original?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: ProteinPotential
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
