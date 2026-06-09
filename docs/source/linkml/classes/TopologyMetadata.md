---
search:
  boost: 10.0
---

# Class: TopologyMetadata

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/TopologyMetadata](https://CCPBioSim.ac.uk/biosim-schema/TopologyMetadata)





```{mermaid}
 classDiagram
    class TopologyMetadata
    click TopologyMetadata href "../../classes/TopologyMetadata/"
      TopologyMetadata : connectivity





        TopologyMetadata --> "0..1" Connectivity : connectivity
        click Connectivity href "../../classes/Connectivity/"



      TopologyMetadata : particles





        TopologyMetadata --> "0..1" Particles : particles
        click Particles href "../../classes/Particles/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [connectivity](../slots/connectivity.md) | 0..1 <br/> [Connectivity](../classes/Connectivity.md) | Particle connectivity information | direct |
| [particles](../slots/particles.md) | 0..1 <br/> [Particles](../classes/Particles.md) | Particles information | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationMetadata](../classes/SimulationMetadata.md) | [topology](../slots/topology.md) | range | [TopologyMetadata](../classes/TopologyMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/TopologyMetadata |
| native | https://CCPBioSim.ac.uk/biosim-schema/TopologyMetadata |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TopologyMetadata
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- connectivity
- particles

```
</details>

### Induced

<details>
```yaml
name: TopologyMetadata
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  connectivity:
    name: connectivity
    description: Particle connectivity information
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: TopologyMetadata
    domain_of:
    - TopologyMetadata
    range: Connectivity
  particles:
    name: particles
    description: Particles information
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: TopologyMetadata
    domain_of:
    - TopologyMetadata
    range: Particles

```
</details></div>
