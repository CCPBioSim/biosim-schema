---
search:
  boost: 10.0
---

# Class: Minimisation

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Minimisation](https://CCPBioSim.ac.uk/biosim-schema/Minimisation)





```{mermaid}
 classDiagram
    class Minimisation
    click Minimisation href "../../classes/Minimisation/"
      Minimisation : energy_tolerance





        Minimisation --> "0..1" ForceQuantity : energy_tolerance
        click ForceQuantity href "../../classes/ForceQuantity/"



      Minimisation : minimisation_algorithm





        Minimisation --> "*" MinimisationAlgorithm : minimisation_algorithm
        click MinimisationAlgorithm href "../../enums/MinimisationAlgorithm/"



      Minimisation : minimisation_distance_step_size





        Minimisation --> "0..1" LengthQuantity : minimisation_distance_step_size
        click LengthQuantity href "../../classes/LengthQuantity/"



      Minimisation : number_of_minimisation_steps

      Minimisation : simulation_software





        Minimisation --> "*" SimulationSoftware : simulation_software
        click SimulationSoftware href "../../enums/SimulationSoftware/"



      Minimisation : simulation_tool





        Minimisation --> "*" SimulationTool : simulation_tool
        click SimulationTool href "../../enums/SimulationTool/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [energy_tolerance](../slots/energy_tolerance.md) | 0..1 <br/> [ForceQuantity](../classes/ForceQuantity.md) | Tolerance energy for when minimization stops, this is when the maximum force ... | direct |
| [number_of_minimisation_steps](../slots/number_of_minimisation_steps.md) | 0..1 <br/> [integer](../types/integer.md) | Number of integration steps performed during minimisation of the system, give... | direct |
| [minimisation_distance_step_size](../slots/minimisation_distance_step_size.md) | 0..1 <br/> [LengthQuantity](../classes/LengthQuantity.md) | The distance the algorithm moves in a single step, controls how large a step ... | direct |
| [minimisation_algorithm](../slots/minimisation_algorithm.md) | * <br/> [MinimisationAlgorithm](../enums/MinimisationAlgorithm.md) | Name of the method used to minimise the molecular system | direct |
| [simulation_tool](../slots/simulation_tool.md) | * <br/> [SimulationTool](../enums/SimulationTool.md) | Tool used to perform simulation | direct |
| [simulation_software](../slots/simulation_software.md) | * <br/> [SimulationSoftware](../enums/SimulationSoftware.md) | Name of software used to perform simulation step | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationStages](../classes/SimulationStages.md) | [minimisation](../slots/minimisation.md) | range | [Minimisation](../classes/Minimisation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Minimisation |
| native | https://CCPBioSim.ac.uk/biosim-schema/Minimisation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Minimisation
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- energy_tolerance
- number_of_minimisation_steps
- minimisation_distance_step_size
- minimisation_algorithm
- simulation_tool
- simulation_software

```
</details>

### Induced

<details>
```yaml
name: Minimisation
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  energy_tolerance:
    name: energy_tolerance
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: emtol
          unit: kJ/mol/nm
        - engine: amber
          key: drms
          unit: 10−4 kcal/mol/Å
    description: Tolerance energy for when minimization stops, this is when the maximum
      force on any atom is less than this value (default is often 1000 kJ/mol/nm or
      10−4kcal), given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Minimisation
    domain_of:
    - Minimisation
    range: ForceQuantity
    minimum_value: 0
  number_of_minimisation_steps:
    name: number_of_minimisation_steps
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: maxcyc
        - engine: gromacs
          key: nsteps
    description: Number of integration steps performed during minimisation of the
      system, given as an integer.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Minimisation
    domain_of:
    - Minimisation
    range: integer
  minimisation_distance_step_size:
    name: minimisation_distance_step_size
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: dx0
          unit: Å
        - engine: gromacs
          key: emstep
          unit: nm
    description: The distance the algorithm moves in a single step, controls how large
      a step the optimizer takes during the initial phase of minimizing the potential
      energy of a structure, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Minimisation
    domain_of:
    - Minimisation
    range: LengthQuantity
    minimum_value: 0
  minimisation_algorithm:
    name: minimisation_algorithm
    description: Name of the method used to minimise the molecular system.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Minimisation
    domain_of:
    - Minimisation
    range: MinimisationAlgorithm
    multivalued: true
  simulation_tool:
    name: simulation_tool
    description: Tool used to perform simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Minimisation
    domain_of:
    - Minimisation
    - Equilibration
    - Production
    range: SimulationTool
    multivalued: true
  simulation_software:
    name: simulation_software
    description: Name of software used to perform simulation step.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Minimisation
    domain_of:
    - Minimisation
    - Equilibration
    - Production
    range: SimulationSoftware
    multivalued: true

```
</details></div>
