---
search:
  boost: 10.0
---

# Class: SimulationAverages

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/SimulationAverages](https://CCPBioSim.ac.uk/biosim-schema/SimulationAverages)





```{mermaid}
 classDiagram
    class SimulationAverages
    click SimulationAverages href "../../classes/SimulationAverages/"
      SimulationAverages : average_enthalpy





        SimulationAverages --> "0..1" MolarEnergyQuantity : average_enthalpy
        click MolarEnergyQuantity href "../../classes/MolarEnergyQuantity/"



      SimulationAverages : average_kinetic_energy





        SimulationAverages --> "0..1" MolarEnergyQuantity : average_kinetic_energy
        click MolarEnergyQuantity href "../../classes/MolarEnergyQuantity/"



      SimulationAverages : average_potential_energy





        SimulationAverages --> "0..1" MolarEnergyQuantity : average_potential_energy
        click MolarEnergyQuantity href "../../classes/MolarEnergyQuantity/"



      SimulationAverages : average_pressure





        SimulationAverages --> "0..1" PressureQuantity : average_pressure
        click PressureQuantity href "../../classes/PressureQuantity/"



      SimulationAverages : average_temperature





        SimulationAverages --> "0..1" TemperatureQuantity : average_temperature
        click TemperatureQuantity href "../../classes/TemperatureQuantity/"



      SimulationAverages : average_volume





        SimulationAverages --> "0..1" VolumeQuantity : average_volume
        click VolumeQuantity href "../../classes/VolumeQuantity/"



      SimulationAverages : average_volume_vector





        SimulationAverages --> "0..1" VectorVolumeQuantity : average_volume_vector
        click VectorVolumeQuantity href "../../classes/VectorVolumeQuantity/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [average_kinetic_energy](../slots/average_kinetic_energy.md) | 0..1 <br/> [MolarEnergyQuantity](../classes/MolarEnergyQuantity.md) | Average kinetic energy sampled from the simulation, given as a float | direct |
| [average_potential_energy](../slots/average_potential_energy.md) | 0..1 <br/> [MolarEnergyQuantity](../classes/MolarEnergyQuantity.md) | Average potential energy sampled from the simulation, given as a float | direct |
| [average_enthalpy](../slots/average_enthalpy.md) | 0..1 <br/> [MolarEnergyQuantity](../classes/MolarEnergyQuantity.md) | Average enthalpy sampled from the simulation, given as a float | direct |
| [average_pressure](../slots/average_pressure.md) | 0..1 <br/> [PressureQuantity](../classes/PressureQuantity.md) | Average pressure sampled from the simulation, given as a float | direct |
| [average_temperature](../slots/average_temperature.md) | 0..1 <br/> [TemperatureQuantity](../classes/TemperatureQuantity.md) | Average temperature sampled from the simulation, given as a float | direct |
| [average_volume](../slots/average_volume.md) | 0..1 <br/> [VolumeQuantity](../classes/VolumeQuantity.md) | Average volume sampled from the simulation, given as a float | direct |
| [average_volume_vector](../slots/average_volume_vector.md) | 0..1 <br/> [VectorVolumeQuantity](../classes/VectorVolumeQuantity.md) | Average volume sampled from the simulation, given as a list, (e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationObservables](../classes/SimulationObservables.md) | [simulation_averages](../slots/simulation_averages.md) | range | [SimulationAverages](../classes/SimulationAverages.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/SimulationAverages |
| native | https://CCPBioSim.ac.uk/biosim-schema/SimulationAverages |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SimulationAverages
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- average_kinetic_energy
- average_potential_energy
- average_enthalpy
- average_pressure
- average_temperature
- average_volume
- average_volume_vector

```
</details>

### Induced

<details>
```yaml
name: SimulationAverages
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  average_kinetic_energy:
    name: average_kinetic_energy
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: Kinetic En.
          unit: kJ/mol
        - engine: amber
          key: EKtot
          unit: kcal/mol
    description: Average kinetic energy sampled from the simulation, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationAverages
    domain_of:
    - SimulationAverages
    range: MolarEnergyQuantity
  average_potential_energy:
    name: average_potential_energy
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: Potential
          unit: kJ/mol
        - engine: amber
          key: EPtot
          unit: kcal/mol
    description: Average potential energy sampled from the simulation, given as a
      float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationAverages
    domain_of:
    - SimulationAverages
    range: MolarEnergyQuantity
  average_enthalpy:
    name: average_enthalpy
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: Total Energy
          unit: kJ/mol
        - engine: amber
          key: Etot
          unit: kcal/mol
    description: Average enthalpy sampled from the simulation, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationAverages
    domain_of:
    - SimulationAverages
    range: MolarEnergyQuantity
  average_pressure:
    name: average_pressure
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: Pressure (bar)
          unit: bar
        - engine: amber
          key: PRESS
          unit: bar
    description: Average pressure sampled from the simulation, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationAverages
    domain_of:
    - SimulationAverages
    range: PressureQuantity
  average_temperature:
    name: average_temperature
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: Temperature
          unit: K
        - engine: amber
          key: TEMP(K)
          unit: K
    description: Average temperature sampled from the simulation, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationAverages
    domain_of:
    - SimulationAverages
    range: TemperatureQuantity
  average_volume:
    name: average_volume
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: amber
          key: VOLUME
          unit: A^3
    description: Average volume sampled from the simulation, given as a float.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationAverages
    domain_of:
    - SimulationAverages
    range: VolumeQuantity
  average_volume_vector:
    name: average_volume_vector
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key:
          - Box-X
          - Box-Y
          - Box-Z
          unit: nm
    description: Average volume sampled from the simulation, given as a list, (e.g.
      10, 10, 10).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: SimulationAverages
    domain_of:
    - SimulationAverages
    range: VectorVolumeQuantity

```
</details></div>
