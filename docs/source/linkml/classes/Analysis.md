---
search:
  boost: 10.0
---

# Class: Analysis

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/Analysis](https://CCPBioSim.ac.uk/biosim-schema/Analysis)





```{mermaid}
 classDiagram
    class Analysis
    click Analysis href "../../classes/Analysis/"
      Analysis : analysis_method





        Analysis --> "*" AnalysisMethod : analysis_method
        click AnalysisMethod href "../../enums/AnalysisMethod/"



      Analysis : analysis_software





        Analysis --> "*" AnalysisSoftware : analysis_software
        click AnalysisSoftware href "../../enums/AnalysisSoftware/"



      Analysis : analysis_tool





        Analysis --> "*" AnalysisTool : analysis_tool
        click AnalysisTool href "../../enums/AnalysisTool/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [analysis_tool](../slots/analysis_tool.md) | * <br/> [AnalysisTool](../enums/AnalysisTool.md) | Name of the tool used to analyse simulation | direct |
| [analysis_software](../slots/analysis_software.md) | * <br/> [AnalysisSoftware](../enums/AnalysisSoftware.md) | Name of software used to analyse simulation | direct |
| [analysis_method](../slots/analysis_method.md) | * <br/> [AnalysisMethod](../enums/AnalysisMethod.md) | Name of the method used to analyse simulation | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SimulationStages](../classes/SimulationStages.md) | [analysis](../slots/analysis.md) | range | [Analysis](../classes/Analysis.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/Analysis |
| native | https://CCPBioSim.ac.uk/biosim-schema/Analysis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Analysis
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- analysis_tool
- analysis_software
- analysis_method

```
</details>

### Induced

<details>
```yaml
name: Analysis
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  analysis_tool:
    name: analysis_tool
    description: Name of the tool used to analyse simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Analysis
    domain_of:
    - Analysis
    range: AnalysisTool
    multivalued: true
  analysis_software:
    name: analysis_software
    description: Name of software used to analyse simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Analysis
    domain_of:
    - Analysis
    range: AnalysisSoftware
    multivalued: true
  analysis_method:
    name: analysis_method
    description: Name of the method used to analyse simulation.
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: Analysis
    domain_of:
    - Analysis
    range: AnalysisMethod
    multivalued: true

```
</details></div>
