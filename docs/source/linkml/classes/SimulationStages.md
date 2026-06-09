---
search:
  boost: 10.0
---

# Class: SimulationStages

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/SimulationStages](https://CCPBioSim.ac.uk/biosim-schema/SimulationStages)





```{mermaid}
 classDiagram
    class SimulationStages
    click SimulationStages href "../../classes/SimulationStages/"
      SimulationStages : analysis





        SimulationStages --> "0..1" Analysis : analysis
        click Analysis href "../../classes/Analysis/"



      SimulationStages : equilibration





        SimulationStages --> "0..1" Equilibration : equilibration
        click Equilibration href "../../classes/Equilibration/"



      SimulationStages : minimisation





        SimulationStages --> "0..1" Minimisation : minimisation
        click Minimisation href "../../classes/Minimisation/"



      SimulationStages : production





        SimulationStages --> "0..1" Production : production
        click Production href "../../classes/Production/"



      SimulationStages : setup





        SimulationStages --> "0..1" Setup : setup
        click Setup href "../../classes/Setup/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [setup](../slots/setup.md) | 0..1 <br/> [Setup](../classes/Setup.md) | Setup stage of a simulation | direct |
| [minimisation](../slots/minimisation.md) | 0..1 <br/> [Minimisation](../classes/Minimisation.md) | Minimisation stage of a simulation | direct |
| [equilibration](../slots/equilibration.md) | 0..1 <br/> [Equilibration](../classes/Equilibration.md) | Equilibration stage of a simulation | direct |
| [production](../slots/production.md) | 0..1 <br/> [Production](../classes/Production.md) | Production stage of a simulation | direct |
| [analysis](../slots/analysis.md) | 0..1 <br/> [Analysis](../classes/Analysis.md) | Analysis stage of a simulation | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationMetadata](../classes/SimulationMetadata.md) | [stages](../slots/stages.md) | range | [SimulationStages](../classes/SimulationStages.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/SimulationStages |
| native | https://CCPBioSim.ac.uk/biosim-schema/SimulationStages |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SimulationStages
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- setup
- minimisation
- equilibration
- production
- analysis

```
</details>

### Induced

<details>
```yaml
name: SimulationStages
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  setup:
    name: setup
    description: Setup stage of a simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationStages
    domain_of:
    - SimulationStages
    range: Setup
  minimisation:
    name: minimisation
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: imin
          value: 1
    description: Minimisation stage of a simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationStages
    domain_of:
    - SimulationStages
    range: Minimisation
  equilibration:
    name: equilibration
    description: Equilibration stage of a simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationStages
    domain_of:
    - SimulationStages
    range: Equilibration
  production:
    name: production
    description: Production stage of a simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationStages
    domain_of:
    - SimulationStages
    range: Production
  analysis:
    name: analysis
    description: Analysis stage of a simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationStages
    domain_of:
    - SimulationStages
    range: Analysis

```
</details></div>
