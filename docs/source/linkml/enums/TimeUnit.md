---
search:
  boost: 2.0
---


# Enum: TimeUnit




_Units used to describe time._



<div data-search-exclude markdown="1">

URI: [https://CCPBioSim.ac.uk/biosim-schema/TimeUnit](https://CCPBioSim.ac.uk/biosim-schema/TimeUnit)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| s | qudt:SEC | Time units in seconds |
| ms | qudt:MilliSEC | Time units in milliseconds |
| μs | qudt:MicroSEC | Time units in microseconds |
| ns | qudt:NanoSEC | Time units in nanoseconds |
| ps | qudt:PicoSEC | Time units in picoseconds |
| fs | None | Time units in femtoseconds |













## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/






## LinkML Source

<details>
```yaml
name: TimeUnit
description: Units used to describe time.
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
rank: 1000
permissible_values:
  s:
    text: s
    description: Time units in seconds.
    meaning: qudt:SEC
    unit:
      ucum_code: s
      has_quantity_kind: Time
    aliases:
    - s
  ms:
    text: ms
    description: Time units in milliseconds.
    meaning: qudt:MilliSEC
    unit:
      ucum_code: ms
      has_quantity_kind: Time
    aliases:
    - ms
  μs:
    text: μs
    description: Time units in microseconds.
    meaning: qudt:MicroSEC
    unit:
      ucum_code: us
      has_quantity_kind: Time
    aliases:
    - μs
    - us
  ns:
    text: ns
    description: Time units in nanoseconds.
    meaning: qudt:NanoSEC
    unit:
      ucum_code: ns
      has_quantity_kind: Time
    aliases:
    - ns
  ps:
    text: ps
    description: Time units in picoseconds.
    meaning: qudt:PicoSEC
    unit:
      ucum_code: ps
      has_quantity_kind: Time
    aliases:
    - ps
  fs:
    text: fs
    description: Time units in femtoseconds.
    unit:
      ucum_code: fs
      has_quantity_kind: Time
    aliases:
    - fs

```
</details>

</div>
