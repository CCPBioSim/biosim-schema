---
search:
  boost: 10.0
---

# Class: Thermostat

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Thermostat](https://CCPBioSim.ac.uk/biosim-schema/Thermostat)





```{mermaid}
 classDiagram
    class Thermostat
    click Thermostat href "../../classes/Thermostat/"
      Thermostat : chain_length

      Thermostat : collision_frequency





        Thermostat --> "0..1" FrequencyQuantity : collision_frequency
        click FrequencyQuantity href "../../classes/FrequencyQuantity/"



      Thermostat : coupling_group

      Thermostat : friction_coefficient





        Thermostat --> "0..1" FrictionCoefficientQuantity : friction_coefficient
        click FrictionCoefficientQuantity href "../../classes/FrictionCoefficientQuantity/"



      Thermostat : target_temperature





        Thermostat --> "0..1" VectorTemperatureQuantity : target_temperature
        click VectorTemperatureQuantity href "../../classes/VectorTemperatureQuantity/"



      Thermostat : temperature_time_constant





        Thermostat --> "0..1" VectorTimeQuantity : temperature_time_constant
        click VectorTimeQuantity href "../../classes/VectorTimeQuantity/"



      Thermostat : thermostat_algorithm





        Thermostat --> "0..1" ThermostatAlgorithm : thermostat_algorithm
        click ThermostatAlgorithm href "../../enums/ThermostatAlgorithm/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [thermostat_algorithm](../slots/thermostat_algorithm.md) | 0..1 <br/> [ThermostatAlgorithm](../enums/ThermostatAlgorithm.md) | List of thermostat algorithms used in the simulation | direct |
| [target_temperature](../slots/target_temperature.md) | 0..1 <br/> [VectorTemperatureQuantity](../classes/VectorTemperatureQuantity.md) | Target/reference temperature set to reach in the simulation, given as a list ... | direct |
| [collision_frequency](../slots/collision_frequency.md) | 0..1 <br/> [FrequencyQuantity](../classes/FrequencyQuantity.md) | Collision frequency for the integrator, given as a float | direct |
| [temperature_time_constant](../slots/temperature_time_constant.md) | 0..1 <br/> [VectorTimeQuantity](../classes/VectorTimeQuantity.md) | Time constant for coupling the system temperature in seconds units, given as ... | direct |
| [coupling_group](../slots/coupling_group.md) | 0..1 <br/> [string](../types/string.md) | A subset of atoms for which temperature is controlled, often needed for simul... | direct |
| [chain_length](../slots/chain_length.md) | 0..1 <br/> [integer](../types/integer.md) | Usually required in the Nosé-Hoover thermostat, the chain length (e | direct |
| [friction_coefficient](../slots/friction_coefficient.md) | 0..1 <br/> [FrictionCoefficientQuantity](../classes/FrictionCoefficientQuantity.md) | Usually used in the Langevin thermostat, the friction coefficient determines ... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationSettings](../classes/SimulationSettings.md) | [thermostat](../slots/thermostat.md) | range | [Thermostat](../classes/Thermostat.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Thermostat |
| native | https://CCPBioSim.ac.uk/biosim-schema/Thermostat |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Thermostat
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- thermostat_algorithm
- target_temperature
- collision_frequency
- temperature_time_constant
- coupling_group
- chain_length
- friction_coefficient

```
</details>

### Induced

<details>
```yaml
name: Thermostat
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  thermostat_algorithm:
    name: thermostat_algorithm
    description: List of thermostat algorithms used in the simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Thermostat
    domain_of:
    - Thermostat
    range: ThermostatAlgorithm
  target_temperature:
    name: target_temperature
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: temp0
          unit: K
        - engine: gromacs
          key: ref-t
          unit: K
        - engine: lammps
          key: temp
          unit: K
    description: Target/reference temperature set to reach in the simulation, given
      as a list (e.g. 300, 300).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Thermostat
    domain_of:
    - Thermostat
    range: VectorTemperatureQuantity
  collision_frequency:
    name: collision_frequency
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: gamma_ln
          unit: 1/ps
    description: Collision frequency for the integrator, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Thermostat
    domain_of:
    - Thermostat
    range: FrequencyQuantity
  temperature_time_constant:
    name: temperature_time_constant
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: tau-t
          unit: ps
    description: Time constant for coupling the system temperature in seconds units,
      given as a list (e.g. 300, 300).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Thermostat
    domain_of:
    - Thermostat
    range: VectorTimeQuantity
  coupling_group:
    name: coupling_group
    description: A subset of atoms for which temperature is controlled, often needed
      for simulating complex systems (e.g., protein in water), used in gromacs, given
      as a string
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Thermostat
    domain_of:
    - Thermostat
    range: string
  chain_length:
    name: chain_length
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: nhc_chain_length
        - engine: gromacs
          key: nh-chain-length
    description: Usually required in the Nosé-Hoover thermostat, the chain length
      (e.g., nh-chain-length in GROMACS) is used to maintain canonical distribution,
      given as an integer.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Thermostat
    domain_of:
    - Thermostat
    range: integer
    minimum_value: 0
  friction_coefficient:
    name: friction_coefficient
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: bd-fric
          unit: a/ps
    description: Usually used in the Langevin thermostat, the friction coefficient
      determines the strength of coupling between a system and a heat bath, given
      as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Thermostat
    domain_of:
    - Thermostat
    range: FrictionCoefficientQuantity

```
</details></div>
