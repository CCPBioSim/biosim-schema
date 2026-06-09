---
search:
  boost: 10.0
---

# Class: SimulationObservables

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/SimulationObservables](https://CCPBioSim.ac.uk/biosim-schema/SimulationObservables)





```{mermaid}
 classDiagram
    class SimulationObservables
    click SimulationObservables href "../../classes/SimulationObservables/"
      SimulationObservables : simulation_averages





        SimulationObservables --> "0..1" SimulationAverages : simulation_averages
        click SimulationAverages href "../../classes/SimulationAverages/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [simulation_averages](../slots/simulation_averages.md) | 0..1 <br/> [SimulationAverages](../classes/SimulationAverages.md) | Average values of observables outputted from the simulation | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationMetadata](../classes/SimulationMetadata.md) | [observables](../slots/observables.md) | range | [SimulationObservables](../classes/SimulationObservables.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/SimulationObservables |
| native | https://CCPBioSim.ac.uk/biosim-schema/SimulationObservables |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SimulationObservables
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- simulation_averages

```
</details>

### Induced

<details>
```yaml
name: SimulationObservables
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  simulation_averages:
    name: simulation_averages
    description: Average values of observables outputted from the simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationObservables
    domain_of:
    - SimulationObservables
    range: SimulationAverages

```
</details></div>
