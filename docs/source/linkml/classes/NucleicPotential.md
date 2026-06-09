---
search:
  boost: 10.0
---

# Class: NucleicPotential

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/NucleicPotential](https://CCPBioSim.ac.uk/biosim-schema/NucleicPotential)





```{mermaid}
 classDiagram
    class NucleicPotential
    click NucleicPotential href "../../classes/NucleicPotential/"
      NucleicPotential : modified

      NucleicPotential : nucleic_potential_name





        NucleicPotential --> "0..1" NucleicPotentialName : nucleic_potential_name
        click NucleicPotentialName href "../../enums/NucleicPotentialName/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [nucleic_potential_name](../slots/nucleic_potential_name.md) | 0..1 <br/> [NucleicPotentialName](../enums/NucleicPotentialName.md) | Force field used to describe nucleic acids | direct |
| [modified](../slots/modified.md) | 0..1 <br/> [boolean](../types/boolean.md) | Has the initial model been modified from the original? | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PotentialMetadata](../classes/PotentialMetadata.md) | [nucleic_potential](../slots/nucleic_potential.md) | range | [NucleicPotential](../classes/NucleicPotential.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/NucleicPotential |
| native | https://CCPBioSim.ac.uk/biosim-schema/NucleicPotential |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NucleicPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- nucleic_potential_name
- modified

```
</details>

### Induced

<details>
```yaml
name: NucleicPotential
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  nucleic_potential_name:
    name: nucleic_potential_name
    description: Force field used to describe nucleic acids.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: NucleicPotential
    domain_of:
    - NucleicPotential
    range: NucleicPotentialName
  modified:
    name: modified
    description: Has the initial model been modified from the original?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: NucleicPotential
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
