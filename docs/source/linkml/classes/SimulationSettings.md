---
search:
  boost: 10.0
---

# Class: SimulationSettings

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/SimulationSettings](https://CCPBioSim.ac.uk/biosim-schema/SimulationSettings)





```{mermaid}
 classDiagram
    class SimulationSettings
    click SimulationSettings href "../../classes/SimulationSettings/"
      SimulationSettings : barostat





        SimulationSettings --> "0..1" Barostat : barostat
        click Barostat href "../../classes/Barostat/"



      SimulationSettings : ensemble





        SimulationSettings --> "0..1" Ensemble : ensemble
        click Ensemble href "../../classes/Ensemble/"



      SimulationSettings : integrator





        SimulationSettings --> "0..1" Integrator : integrator
        click Integrator href "../../classes/Integrator/"



      SimulationSettings : interactions





        SimulationSettings --> "0..1" Interactions : interactions
        click Interactions href "../../classes/Interactions/"



      SimulationSettings : thermostat





        SimulationSettings --> "0..1" Thermostat : thermostat
        click Thermostat href "../../classes/Thermostat/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ensemble](../slots/ensemble.md) | 0..1 <br/> [Ensemble](../classes/Ensemble.md) | Ensemble information | direct |
| [integrator](../slots/integrator.md) | 0..1 <br/> [Integrator](../classes/Integrator.md) | Integrator information | direct |
| [barostat](../slots/barostat.md) | 0..1 <br/> [Barostat](../classes/Barostat.md) | Barostat information | direct |
| [thermostat](../slots/thermostat.md) | 0..1 <br/> [Thermostat](../classes/Thermostat.md) | thermostat information | direct |
| [interactions](../slots/interactions.md) | 0..1 <br/> [Interactions](../classes/Interactions.md) | Interaction information | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationMetadata](../classes/SimulationMetadata.md) | [settings](../slots/settings.md) | range | [SimulationSettings](../classes/SimulationSettings.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/SimulationSettings |
| native | https://CCPBioSim.ac.uk/biosim-schema/SimulationSettings |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SimulationSettings
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- ensemble
- integrator
- barostat
- thermostat
- interactions

```
</details>

### Induced

<details>
```yaml
name: SimulationSettings
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  ensemble:
    name: ensemble
    description: Ensemble information.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationSettings
    domain_of:
    - SimulationSettings
    range: Ensemble
  integrator:
    name: integrator
    description: Integrator information.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationSettings
    domain_of:
    - SimulationSettings
    range: Integrator
  barostat:
    name: barostat
    description: Barostat information.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationSettings
    domain_of:
    - SimulationSettings
    range: Barostat
  thermostat:
    name: thermostat
    description: thermostat information.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationSettings
    domain_of:
    - SimulationSettings
    range: Thermostat
  interactions:
    name: interactions
    description: Interaction information.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationSettings
    domain_of:
    - SimulationSettings
    range: Interactions

```
</details></div>
