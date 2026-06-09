---
search:
  boost: 10.0
---

# Class: Ensemble

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Ensemble](https://CCPBioSim.ac.uk/biosim-schema/Ensemble)





```{mermaid}
 classDiagram
    class Ensemble
    click Ensemble href "../../classes/Ensemble/"
      Ensemble : ensemble_type





        Ensemble --> "0..1" EnsembleType : ensemble_type
        click EnsembleType href "../../enums/EnsembleType/"



      Ensemble : random_seed


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ensemble_type](../slots/ensemble_type.md) | 0..1 <br/> [EnsembleType](../enums/EnsembleType.md) | List of ensemble types used in the simulation | direct |
| [random_seed](../slots/random_seed.md) | 0..1 <br/> [integer](../types/integer.md) | Random number used to set (a) distribution of velocities across particles at ... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationSettings](../classes/SimulationSettings.md) | [ensemble](../slots/ensemble.md) | range | [Ensemble](../classes/Ensemble.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Ensemble |
| native | https://CCPBioSim.ac.uk/biosim-schema/Ensemble |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Ensemble
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- ensemble_type
- random_seed

```
</details>

### Induced

<details>
```yaml
name: Ensemble
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  ensemble_type:
    name: ensemble_type
    description: List of ensemble types used in the simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Ensemble
    domain_of:
    - Ensemble
    range: EnsembleType
  random_seed:
    name: random_seed
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: ig
        - engine: gromacs
          key: ld-seed
    description: Random number used to set (a) distribution of velocities across particles
      at the start of a simulation and (b) pseudo-random values for dynamics/couplings,
      given as an integer.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Ensemble
    domain_of:
    - Ensemble
    range: integer

```
</details></div>
