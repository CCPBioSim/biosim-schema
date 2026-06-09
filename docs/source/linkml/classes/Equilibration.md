---
search:
  boost: 10.0
---

# Class: Equilibration

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Equilibration](https://CCPBioSim.ac.uk/biosim-schema/Equilibration)





```{mermaid}
 classDiagram
    class Equilibration
    click Equilibration href "../../classes/Equilibration/"
      Equilibration : simulation_software





        Equilibration --> "*" SimulationSoftware : simulation_software
        click SimulationSoftware href "../../enums/SimulationSoftware/"



      Equilibration : simulation_tool





        Equilibration --> "*" SimulationTool : simulation_tool
        click SimulationTool href "../../enums/SimulationTool/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [simulation_tool](../slots/simulation_tool.md) | * <br/> [SimulationTool](../enums/SimulationTool.md) | Tool used to perform simulation | direct |
| [simulation_software](../slots/simulation_software.md) | * <br/> [SimulationSoftware](../enums/SimulationSoftware.md) | Name of software used to perform simulation step | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationStages](../classes/SimulationStages.md) | [equilibration](../slots/equilibration.md) | range | [Equilibration](../classes/Equilibration.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Equilibration |
| native | https://CCPBioSim.ac.uk/biosim-schema/Equilibration |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Equilibration
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- simulation_tool
- simulation_software

```
</details>

### Induced

<details>
```yaml
name: Equilibration
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  simulation_tool:
    name: simulation_tool
    description: Tool used to perform simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Equilibration
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
    owner: Equilibration
    domain_of:
    - Minimisation
    - Equilibration
    - Production
    range: SimulationSoftware
    multivalued: true

```
</details></div>
