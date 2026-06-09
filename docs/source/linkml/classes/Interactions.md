---
search:
  boost: 10.0
---

# Class: Interactions

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Interactions](https://CCPBioSim.ac.uk/biosim-schema/Interactions)





```{mermaid}
 classDiagram
    class Interactions
    click Interactions href "../../classes/Interactions/"
      Interactions : bond_length_constraints_algorithm





        Interactions --> "0..1" BondLengthConstraintsAlgorithm : bond_length_constraints_algorithm
        click BondLengthConstraintsAlgorithm href "../../enums/BondLengthConstraintsAlgorithm/"



      Interactions : electrostatic_cutoff_distance





        Interactions --> "0..1" LengthQuantity : electrostatic_cutoff_distance
        click LengthQuantity href "../../classes/LengthQuantity/"



      Interactions : long_range_interaction_method





        Interactions --> "0..1" LongRangeInteractionMethod : long_range_interaction_method
        click LongRangeInteractionMethod href "../../enums/LongRangeInteractionMethod/"



      Interactions : restraints

      Interactions : vdw_cutoff_distance





        Interactions --> "0..1" LengthQuantity : vdw_cutoff_distance
        click LengthQuantity href "../../classes/LengthQuantity/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [restraints](../slots/restraints.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are any positional restraints applied to molecule dynamics? (Restraints usual... | direct |
| [electrostatic_cutoff_distance](../slots/electrostatic_cutoff_distance.md) | 0..1 <br/> [LengthQuantity](../classes/LengthQuantity.md) | Distance in Angstrom at which a electrostatic interaction is turned off and a... | direct |
| [vdw_cutoff_distance](../slots/vdw_cutoff_distance.md) | 0..1 <br/> [LengthQuantity](../classes/LengthQuantity.md) | Distance in Angstrom at which a Van der Waals interaction is turned off and a... | direct |
| [bond_length_constraints_algorithm](../slots/bond_length_constraints_algorithm.md) | 0..1 <br/> [BondLengthConstraintsAlgorithm](../enums/BondLengthConstraintsAlgorithm.md) | Constraints applied to bonds between two particles in the simulated system | direct |
| [long_range_interaction_method](../slots/long_range_interaction_method.md) | 0..1 <br/> [LongRangeInteractionMethod](../enums/LongRangeInteractionMethod.md) | Method used to describe long-range interactions between particles | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationSettings](../classes/SimulationSettings.md) | [interactions](../slots/interactions.md) | range | [Interactions](../classes/Interactions.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Interactions |
| native | https://CCPBioSim.ac.uk/biosim-schema/Interactions |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Interactions
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- restraints
- electrostatic_cutoff_distance
- vdw_cutoff_distance
- bond_length_constraints_algorithm
- long_range_interaction_method

```
</details>

### Induced

<details>
```yaml
name: Interactions
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  restraints:
    name: restraints
    description: Are any positional restraints applied to molecule dynamics? (Restraints
      usually use harmonic potentials to keep a value near a target).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Interactions
    domain_of:
    - Interactions
    range: boolean
  electrostatic_cutoff_distance:
    name: electrostatic_cutoff_distance
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: rcoulomb
          unit: nm
        - engine: amber
          key: cut
          unit: Å
    description: Distance in Angstrom at which a electrostatic interaction is turned
      off and a long-range non-bonded method is turned on, given as a float.
    examples:
    - value: 10 Å
    - value: 1.2 nm
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Interactions
    domain_of:
    - Interactions
    range: LengthQuantity
  vdw_cutoff_distance:
    name: vdw_cutoff_distance
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: rvdw
          unit: nm
    description: Distance in Angstrom at which a Van der Waals interaction is turned
      off and a long-range non-bonded method is turned on.
    examples:
    - value: 10 Å
    - value: 1.2 nm
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Interactions
    domain_of:
    - Interactions
    range: LengthQuantity
  bond_length_constraints_algorithm:
    name: bond_length_constraints_algorithm
    description: Constraints applied to bonds between two particles in the simulated
      system.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Interactions
    domain_of:
    - Interactions
    range: BondLengthConstraintsAlgorithm
  long_range_interaction_method:
    name: long_range_interaction_method
    description: Method used to describe long-range interactions between particles.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Interactions
    domain_of:
    - Interactions
    range: LongRangeInteractionMethod

```
</details></div>
