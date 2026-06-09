---
search:
  boost: 10.0
---

# Class: ComputationalEnvironment

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/ComputationalEnvironment](https://CCPBioSim.ac.uk/biosim-schema/ComputationalEnvironment)





```{mermaid}
 classDiagram
    class ComputationalEnvironment
    click ComputationalEnvironment href "../../classes/ComputationalEnvironment/"
      ComputationalEnvironment : hardware





        ComputationalEnvironment --> "0..1" Hardware : hardware
        click Hardware href "../../classes/Hardware/"



      ComputationalEnvironment : performance





        ComputationalEnvironment --> "0..1" Performance : performance
        click Performance href "../../classes/Performance/"



      ComputationalEnvironment : software





        ComputationalEnvironment --> "0..1" Software : software
        click Software href "../../classes/Software/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [hardware](../slots/hardware.md) | 0..1 <br/> [Hardware](../classes/Hardware.md) |  | direct |
| [software](../slots/software.md) | 0..1 <br/> [Software](../classes/Software.md) |  | direct |
| [performance](../slots/performance.md) | 0..1 <br/> [Performance](../classes/Performance.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationMetadata](../classes/SimulationMetadata.md) | [compute](../slots/compute.md) | range | [ComputationalEnvironment](../classes/ComputationalEnvironment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/ComputationalEnvironment |
| native | https://CCPBioSim.ac.uk/biosim-schema/ComputationalEnvironment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ComputationalEnvironment
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- hardware
- software
- performance

```
</details>

### Induced

<details>
```yaml
name: ComputationalEnvironment
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  hardware:
    name: hardware
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: ComputationalEnvironment
    domain_of:
    - ComputationalEnvironment
    range: Hardware
  software:
    name: software
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: ComputationalEnvironment
    domain_of:
    - ComputationalEnvironment
    range: Software
  performance:
    name: performance
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: ComputationalEnvironment
    domain_of:
    - ComputationalEnvironment
    range: Performance

```
</details></div>
