---
search:
  boost: 10.0
---

# Class: Particles

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Particles](https://CCPBioSim.ac.uk/biosim-schema/Particles)





```{mermaid}
 classDiagram
    class Particles
    click Particles href "../../classes/Particles/"
      Particles : coarse_grained

      Particles : fixed_charges

      Particles : masses

      Particles : resolution





        Particles --> "0..1" ModelResolution : resolution
        click ModelResolution href "../../enums/ModelResolution/"



      Particles : system_charge





        Particles --> "0..1" ChargeQuantity : system_charge
        click ChargeQuantity href "../../classes/ChargeQuantity/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [masses](../slots/masses.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are masses present in the topology? | direct |
| [fixed_charges](../slots/fixed_charges.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are fixed charges on atoms included in the topology? | direct |
| [system_charge](../slots/system_charge.md) | 0..1 <br/> [ChargeQuantity](../classes/ChargeQuantity.md) | Total electrostatic charge of the system given by the elementary charge (e) | direct |
| [coarse_grained](../slots/coarse_grained.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are atoms coarse-grained? | direct |
| [resolution](../slots/resolution.md) | 0..1 <br/> [ModelResolution](../enums/ModelResolution.md) | Resolution of simulated system | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TopologyMetadata](../classes/TopologyMetadata.md) | [particles](../slots/particles.md) | range | [Particles](../classes/Particles.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Particles |
| native | https://CCPBioSim.ac.uk/biosim-schema/Particles |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Particles
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- masses
- fixed_charges
- system_charge
- coarse_grained
- resolution

```
</details>

### Induced

<details>
```yaml
name: Particles
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  masses:
    name: masses
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: masses
    description: Are masses present in the topology?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Particles
    domain_of:
    - Particles
    range: boolean
  fixed_charges:
    name: fixed_charges
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: fixed_charges
    description: Are fixed charges on atoms included in the topology?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Particles
    domain_of:
    - Particles
    range: boolean
  system_charge:
    name: system_charge
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: system_charge
          unit: e
    description: Total electrostatic charge of the system given by the elementary
      charge (e).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Particles
    domain_of:
    - Particles
    range: ChargeQuantity
    pattern: ^[+-]?\d+(\.\d+)?$
  coarse_grained:
    name: coarse_grained
    description: Are atoms coarse-grained?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Particles
    domain_of:
    - Particles
    range: boolean
  resolution:
    name: resolution
    description: Resolution of simulated system.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Particles
    domain_of:
    - Particles
    range: ModelResolution

```
</details></div>
