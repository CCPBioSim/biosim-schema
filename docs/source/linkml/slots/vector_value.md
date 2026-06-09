---
search:
  boost: 5.0
---

# Slot: vector_value


_vector value for a given quantity._



<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/vector_value](https://CCPBioSim.ac.uk/biosim-schema/vector_value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VectorLengthQuantity](../classes/VectorLengthQuantity.md) | A quantity representing 3D lengths/dimensions |  no  |
| [VectorAngleQuantity](../classes/VectorAngleQuantity.md) | A quantity representing 3D angles |  no  |
| [VectorVolumeQuantity](../classes/VectorVolumeQuantity.md) |  |  no  |
| [VectorCompressibilityQuantity](../classes/VectorCompressibilityQuantity.md) |  |  no  |
| [VectorPressureQuantity](../classes/VectorPressureQuantity.md) |  |  no  |
| [VectorTemperatureQuantity](../classes/VectorTemperatureQuantity.md) | Temperature values for multiple coupling groups |  no  |
| [VectorTimeQuantity](../classes/VectorTimeQuantity.md) | Time values for multiple coupling groups |  no  |
| [MatrixPressureQuantity](../classes/MatrixPressureQuantity.md) |  |  no  |
| [MatrixCompressibilityQuantity](../classes/MatrixCompressibilityQuantity.md) |  |  no  |
| [MatrixQuantity](../classes/MatrixQuantity.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](../types/string.md) |
| Domain Of | [VectorLengthQuantity](../classes/VectorLengthQuantity.md), [VectorAngleQuantity](../classes/VectorAngleQuantity.md), [VectorVolumeQuantity](../classes/VectorVolumeQuantity.md), [VectorCompressibilityQuantity](../classes/VectorCompressibilityQuantity.md), [VectorPressureQuantity](../classes/VectorPressureQuantity.md), [VectorTemperatureQuantity](../classes/VectorTemperatureQuantity.md), [VectorTimeQuantity](../classes/VectorTimeQuantity.md), [MatrixPressureQuantity](../classes/MatrixPressureQuantity.md), [MatrixCompressibilityQuantity](../classes/MatrixCompressibilityQuantity.md), [MatrixQuantity](../classes/MatrixQuantity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/vector_value |
| native | https://CCPBioSim.ac.uk/biosim-schema/vector_value |




## LinkML Source

<details>
```yaml
name: vector_value
description: vector value for a given quantity.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
domain_of:
- VectorLengthQuantity
- VectorAngleQuantity
- VectorVolumeQuantity
- VectorCompressibilityQuantity
- VectorPressureQuantity
- VectorTemperatureQuantity
- VectorTimeQuantity
- MatrixPressureQuantity
- MatrixCompressibilityQuantity
- MatrixQuantity
range: string

```
</details></div>
