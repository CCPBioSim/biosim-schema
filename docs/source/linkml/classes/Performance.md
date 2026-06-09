---
search:
  boost: 10.0
---

# Class: Performance

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Performance](https://CCPBioSim.ac.uk/biosim-schema/Performance)





```{mermaid}
 classDiagram
    class Performance
    click Performance href "../../classes/Performance/"
      Performance : energy_consumption





        Performance --> "0..1" EnergyQuantity : energy_consumption
        click EnergyQuantity href "../../classes/EnergyQuantity/"



      Performance : wall_time





        Performance --> "0..1" TimeQuantity : wall_time
        click TimeQuantity href "../../classes/TimeQuantity/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [wall_time](../slots/wall_time.md) | 0..1 <br/> [TimeQuantity](../classes/TimeQuantity.md) | Total elapsed runtime of the simulation | direct |
| [energy_consumption](../slots/energy_consumption.md) | 0..1 <br/> [EnergyQuantity](../classes/EnergyQuantity.md) | Total energy consumed by the simulation run | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ComputationalEnvironment](../classes/ComputationalEnvironment.md) | [performance](../slots/performance.md) | range | [Performance](../classes/Performance.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Performance |
| native | https://CCPBioSim.ac.uk/biosim-schema/Performance |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Performance
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- wall_time
- energy_consumption

```
</details>

### Induced

<details>
```yaml
name: Performance
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  wall_time:
    name: wall_time
    description: Total elapsed runtime of the simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Performance
    domain_of:
    - Performance
    range: TimeQuantity
  energy_consumption:
    name: energy_consumption
    description: Total energy consumed by the simulation run.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Performance
    domain_of:
    - Performance
    range: EnergyQuantity

```
</details></div>
