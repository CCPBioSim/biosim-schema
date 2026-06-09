---
search:
  boost: 10.0
---

# Class: PotentialMetadata

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/PotentialMetadata](https://CCPBioSim.ac.uk/biosim-schema/PotentialMetadata)





```{mermaid}
 classDiagram
    class PotentialMetadata
    click PotentialMetadata href "../../classes/PotentialMetadata/"
      PotentialMetadata : carbohydrate_potential





        PotentialMetadata --> "0..1" CarbohydratePotential : carbohydrate_potential
        click CarbohydratePotential href "../../classes/CarbohydratePotential/"



      PotentialMetadata : general_potential





        PotentialMetadata --> "0..1" GeneralPotential : general_potential
        click GeneralPotential href "../../classes/GeneralPotential/"



      PotentialMetadata : lipid_potential





        PotentialMetadata --> "0..1" LipidPotential : lipid_potential
        click LipidPotential href "../../classes/LipidPotential/"



      PotentialMetadata : machine_learned_potential





        PotentialMetadata --> "0..1" MachineLearnedPotential : machine_learned_potential
        click MachineLearnedPotential href "../../classes/MachineLearnedPotential/"



      PotentialMetadata : nucleic_potential





        PotentialMetadata --> "0..1" NucleicPotential : nucleic_potential
        click NucleicPotential href "../../classes/NucleicPotential/"



      PotentialMetadata : polymer_potential





        PotentialMetadata --> "0..1" PolymerPotential : polymer_potential
        click PolymerPotential href "../../classes/PolymerPotential/"



      PotentialMetadata : protein_potential





        PotentialMetadata --> "0..1" ProteinPotential : protein_potential
        click ProteinPotential href "../../classes/ProteinPotential/"



      PotentialMetadata : water_potential





        PotentialMetadata --> "0..1" WaterPotential : water_potential
        click WaterPotential href "../../classes/WaterPotential/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [water_potential](../slots/water_potential.md) | 0..1 <br/> [WaterPotential](../classes/WaterPotential.md) | Force field for water molecules | direct |
| [protein_potential](../slots/protein_potential.md) | 0..1 <br/> [ProteinPotential](../classes/ProteinPotential.md) | Force field for proteins | direct |
| [lipid_potential](../slots/lipid_potential.md) | 0..1 <br/> [LipidPotential](../classes/LipidPotential.md) | Force field for lipids | direct |
| [nucleic_potential](../slots/nucleic_potential.md) | 0..1 <br/> [NucleicPotential](../classes/NucleicPotential.md) | Force field for nucleic acids | direct |
| [carbohydrate_potential](../slots/carbohydrate_potential.md) | 0..1 <br/> [CarbohydratePotential](../classes/CarbohydratePotential.md) | Force field for carbohydrates | direct |
| [polymer_potential](../slots/polymer_potential.md) | 0..1 <br/> [PolymerPotential](../classes/PolymerPotential.md) | Force field for polymers (excluding proteins and nucleic acids) | direct |
| [general_potential](../slots/general_potential.md) | 0..1 <br/> [GeneralPotential](../classes/GeneralPotential.md) | Force field for molecules (in general) | direct |
| [machine_learned_potential](../slots/machine_learned_potential.md) | 0..1 <br/> [MachineLearnedPotential](../classes/MachineLearnedPotential.md) | ML force field for molecules (in general) | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationMetadata](../classes/SimulationMetadata.md) | [potentials](../slots/potentials.md) | range | [PotentialMetadata](../classes/PotentialMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/PotentialMetadata |
| native | https://CCPBioSim.ac.uk/biosim-schema/PotentialMetadata |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PotentialMetadata
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- water_potential
- protein_potential
- lipid_potential
- nucleic_potential
- carbohydrate_potential
- polymer_potential
- general_potential
- machine_learned_potential

```
</details>

### Induced

<details>
```yaml
name: PotentialMetadata
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  water_potential:
    name: water_potential
    description: Force field for water molecules.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PotentialMetadata
    domain_of:
    - PotentialMetadata
    range: WaterPotential
  protein_potential:
    name: protein_potential
    description: Force field for proteins.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PotentialMetadata
    domain_of:
    - PotentialMetadata
    range: ProteinPotential
  lipid_potential:
    name: lipid_potential
    description: Force field for lipids.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PotentialMetadata
    domain_of:
    - PotentialMetadata
    range: LipidPotential
  nucleic_potential:
    name: nucleic_potential
    description: Force field for nucleic acids.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PotentialMetadata
    domain_of:
    - PotentialMetadata
    range: NucleicPotential
  carbohydrate_potential:
    name: carbohydrate_potential
    description: Force field for carbohydrates.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PotentialMetadata
    domain_of:
    - PotentialMetadata
    range: CarbohydratePotential
  polymer_potential:
    name: polymer_potential
    description: Force field for polymers (excluding proteins and nucleic acids).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PotentialMetadata
    domain_of:
    - PotentialMetadata
    range: PolymerPotential
  general_potential:
    name: general_potential
    description: Force field for molecules (in general).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PotentialMetadata
    domain_of:
    - PotentialMetadata
    range: GeneralPotential
  machine_learned_potential:
    name: machine_learned_potential
    description: ML force field for molecules (in general).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: PotentialMetadata
    domain_of:
    - PotentialMetadata
    range: MachineLearnedPotential

```
</details></div>
