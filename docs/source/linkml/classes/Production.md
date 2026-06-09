---
search:
  boost: 10.0
---

# Class: Production

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Production](https://CCPBioSim.ac.uk/biosim-schema/Production)





```{mermaid}
 classDiagram
    class Production
    click Production href "../../classes/Production/"
      Production : simulation_method





        Production --> "*" SimulationMethod : simulation_method
        click SimulationMethod href "../../enums/SimulationMethod/"



      Production : simulation_software





        Production --> "*" SimulationSoftware : simulation_software
        click SimulationSoftware href "../../enums/SimulationSoftware/"



      Production : simulation_software_version

      Production : simulation_tool





        Production --> "*" SimulationTool : simulation_tool
        click SimulationTool href "../../enums/SimulationTool/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [simulation_tool](../slots/simulation_tool.md) | * <br/> [SimulationTool](../enums/SimulationTool.md) | Tool used to perform simulation | direct |
| [simulation_software](../slots/simulation_software.md) | * <br/> [SimulationSoftware](../enums/SimulationSoftware.md) | Name of software used to perform simulation step | direct |
| [simulation_software_version](../slots/simulation_software_version.md) | 0..1 <br/> [string](../types/string.md) | Version of software used to perform simulation step | direct |
| [simulation_method](../slots/simulation_method.md) | * <br/> [SimulationMethod](../enums/SimulationMethod.md) | Method used to perform simulation | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationStages](../classes/SimulationStages.md) | [production](../slots/production.md) | range | [Production](../classes/Production.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Production |
| native | https://CCPBioSim.ac.uk/biosim-schema/Production |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Production
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- simulation_tool
- simulation_software
- simulation_software_version
- simulation_method

```
</details>

### Induced

<details>
```yaml
name: Production
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  simulation_tool:
    name: simulation_tool
    description: Tool used to perform simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Production
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
    owner: Production
    domain_of:
    - Minimisation
    - Equilibration
    - Production
    range: SimulationSoftware
    multivalued: true
  simulation_software_version:
    name: simulation_software_version
    annotations:
      extracted_only:
        tag: extracted_only
        value: true
      ui_readonly:
        tag: ui_readonly
        value: true
    description: Version of software used to perform simulation step.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Production
    domain_of:
    - Production
    range: string
  simulation_method:
    name: simulation_method
    description: Method used to perform simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Production
    domain_of:
    - Production
    range: SimulationMethod
    multivalued: true

```
</details></div>
