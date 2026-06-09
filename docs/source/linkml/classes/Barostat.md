---
search:
  boost: 10.0
---

# Class: Barostat

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Barostat](https://CCPBioSim.ac.uk/biosim-schema/Barostat)





```{mermaid}
 classDiagram
    class Barostat
    click Barostat href "../../classes/Barostat/"
      Barostat : barostat_algorithm





        Barostat --> "0..1" BarostatAlgorithm : barostat_algorithm
        click BarostatAlgorithm href "../../enums/BarostatAlgorithm/"



      Barostat : compressibility





        Barostat --> "0..1" MatrixCompressibilityQuantity : compressibility
        click MatrixCompressibilityQuantity href "../../classes/MatrixCompressibilityQuantity/"



      Barostat : pressure_coupling_frequency

      Barostat : pressure_coupling_type





        Barostat --> "0..1" PressureCouplingType : pressure_coupling_type
        click PressureCouplingType href "../../enums/PressureCouplingType/"



      Barostat : pressure_time_constant





        Barostat --> "0..1" TimeQuantity : pressure_time_constant
        click TimeQuantity href "../../classes/TimeQuantity/"



      Barostat : target_pressure





        Barostat --> "0..1" MatrixPressureQuantity : target_pressure
        click MatrixPressureQuantity href "../../classes/MatrixPressureQuantity/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [barostat_algorithm](../slots/barostat_algorithm.md) | 0..1 <br/> [BarostatAlgorithm](../enums/BarostatAlgorithm.md) | List of barostat algorithms used in the simulation | direct |
| [compressibility](../slots/compressibility.md) | 0..1 <br/> [MatrixCompressibilityQuantity](../classes/MatrixCompressibilityQuantity.md) | Compressibility of the simulated system, given as a float | direct |
| [target_pressure](../slots/target_pressure.md) | 0..1 <br/> [MatrixPressureQuantity](../classes/MatrixPressureQuantity.md) | Target/reference pressure set to reach in the simulation, given as a float or... | direct |
| [pressure_time_constant](../slots/pressure_time_constant.md) | 0..1 <br/> [TimeQuantity](../classes/TimeQuantity.md) | Time constant/step (relaxation time of pressure) used for coupling the system... | direct |
| [pressure_coupling_frequency](../slots/pressure_coupling_frequency.md) | 0..1 <br/> [integer](../types/integer.md) | Step frequency to apply the barostat, given as an integer | direct |
| [pressure_coupling_type](../slots/pressure_coupling_type.md) | 0..1 <br/> [PressureCouplingType](../enums/PressureCouplingType.md) | List of coupling types for adjusting box vectors | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationSettings](../classes/SimulationSettings.md) | [barostat](../slots/barostat.md) | range | [Barostat](../classes/Barostat.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Barostat |
| native | https://CCPBioSim.ac.uk/biosim-schema/Barostat |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Barostat
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- barostat_algorithm
- compressibility
- target_pressure
- pressure_time_constant
- pressure_coupling_frequency
- pressure_coupling_type

```
</details>

### Induced

<details>
```yaml
name: Barostat
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  barostat_algorithm:
    name: barostat_algorithm
    description: List of barostat algorithms used in the simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Barostat
    domain_of:
    - Barostat
    range: BarostatAlgorithm
  compressibility:
    name: compressibility
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: compressibility
          unit: 1/bar
        - engine: amber
          key: comp
          unit: 1e10-6 1/bar
    description: Compressibility of the simulated system, given as a float.
    examples:
    - value: 44.6 1e10-6 1/bar
    - value: 4.5e-5 1/bar
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Barostat
    domain_of:
    - Barostat
    range: MatrixCompressibilityQuantity
  target_pressure:
    name: target_pressure
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: ref-p
          unit: bar
        - engine: amber
          key: pres0
          unit: bar
    description: Target/reference pressure set to reach in the simulation, given as
      a float or a list (e.g. 1, 1).
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Barostat
    domain_of:
    - Barostat
    range: MatrixPressureQuantity
  pressure_time_constant:
    name: pressure_time_constant
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: tau-p
          unit: ps
        - engine: amber
          key: taup
          unit: ps
    description: Time constant/step (relaxation time of pressure) used for coupling
      the system pressure, given as a float.
    examples:
    - value: 1.0 ps
    - value: 5.0 ps
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Barostat
    domain_of:
    - Barostat
    range: TimeQuantity
  pressure_coupling_frequency:
    name: pressure_coupling_frequency
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: gromacs
          key: nstpcouple
    description: Step frequency to apply the barostat, given as an integer.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Barostat
    domain_of:
    - Barostat
    range: integer
  pressure_coupling_type:
    name: pressure_coupling_type
    description: List of coupling types for adjusting box vectors.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Barostat
    domain_of:
    - Barostat
    range: PressureCouplingType

```
</details></div>
