---
search:
  boost: 10.0
---

# Class: Setup

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Setup](https://CCPBioSim.ac.uk/biosim-schema/Setup)





```{mermaid}
 classDiagram
    class Setup
    click Setup href "../../classes/Setup/"
      Setup : setup_tool





        Setup --> "0..1" SetupTool : setup_tool
        click SetupTool href "../../enums/SetupTool/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [setup_tool](../slots/setup_tool.md) | 0..1 <br/> [SetupTool](../enums/SetupTool.md) | Name of the tool used to setup simulation | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationStages](../classes/SimulationStages.md) | [setup](../slots/setup.md) | range | [Setup](../classes/Setup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Setup |
| native | https://CCPBioSim.ac.uk/biosim-schema/Setup |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Setup
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- setup_tool

```
</details>

### Induced

<details>
```yaml
name: Setup
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  setup_tool:
    name: setup_tool
    description: Name of the tool used to setup simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Setup
    domain_of:
    - Setup
    range: SetupTool

```
</details></div>
