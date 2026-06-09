---
search:
  boost: 10.0
---

# Class: MoleculeID

<div data-search-exclude markdown="1">



URI: [https://CCPBioSim.ac.uk/biosim-schema/MoleculeID](https://CCPBioSim.ac.uk/biosim-schema/MoleculeID)





```{mermaid}
 classDiagram
    class MoleculeID
    click MoleculeID href "../../classes/MoleculeID/"
      MoleculeID : alphafold_ID

      MoleculeID : atom_count

      MoleculeID : InChI

      MoleculeID : InChIKey

      MoleculeID : modified

      MoleculeID : molecular_formula

      MoleculeID : molecular_weight





        MoleculeID --> "0..1" MassQuantity : molecular_weight
        click MassQuantity href "../../classes/MassQuantity/"



      MoleculeID : molecule_charge





        MoleculeID --> "0..1" ChargeQuantity : molecule_charge
        click ChargeQuantity href "../../classes/ChargeQuantity/"



      MoleculeID : molecule_count

      MoleculeID : monomer_count

      MoleculeID : nucleic_sequence

      MoleculeID : PDB_ID

      MoleculeID : predicted_structure

      MoleculeID : protein_sequence

      MoleculeID : PubChem_CID

      MoleculeID : SMILES

      MoleculeID : UNIPROT_ID


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [PDB_ID](../slots/PDB_ID.md) | 0..1 <br/> [string](../types/string.md) | Protein Data Bank identifier | direct |
| [UNIPROT_ID](../slots/UNIPROT_ID.md) | 0..1 <br/> [string](../types/string.md) | UniProt accession ID | direct |
| [SMILES](../slots/SMILES.md) | 0..1 <br/> [string](../types/string.md) | Simplified Molecular Input Line Entry System (SMILES) ASCII-based line notati... | direct |
| [InChI](../slots/InChI.md) | 0..1 <br/> [string](../types/string.md) | The International Chemical Identifier (InChi) is a textual identifier for che... | direct |
| [InChIKey](../slots/InChIKey.md) | 0..1 <br/> [string](../types/string.md) | The condensed, 27 character InChIKey, which is a hashed version of the full I... | direct |
| [alphafold_ID](../slots/alphafold_ID.md) | 0..1 <br/> [string](../types/string.md) | AlphaFold predicted protein structure identifier (AlphaFold DB, EMBL-EBI) | direct |
| [PubChem_CID](../slots/PubChem_CID.md) | 0..1 <br/> [string](../types/string.md) | PubChem CID of chemical molecules and their activities against biological ass... | direct |
| [protein_sequence](../slots/protein_sequence.md) | 0..1 <br/> [string](../types/string.md) | One letter sequence for protein amino acids | direct |
| [nucleic_sequence](../slots/nucleic_sequence.md) | 0..1 <br/> [string](../types/string.md) | One letter sequence for nucleic acid nucleotides | direct |
| [predicted_structure](../slots/predicted_structure.md) | 0..1 <br/> [boolean](../types/boolean.md) | Are the molecule positions derived from a prediction? | direct |
| [modified](../slots/modified.md) | 0..1 <br/> [boolean](../types/boolean.md) | Has the initial model been modified from the original? | direct |
| [molecular_formula](../slots/molecular_formula.md) | 0..1 <br/> [string](../types/string.md) | The molecular formula of a molecule\ | direct |
| [molecular_weight](../slots/molecular_weight.md) | 0..1 <br/> [MassQuantity](../classes/MassQuantity.md) | The molecular weight of a molecule | direct |
| [molecule_charge](../slots/molecule_charge.md) | 0..1 <br/> [ChargeQuantity](../classes/ChargeQuantity.md) | Electrostatic charge of a molecule | direct |
| [molecule_count](../slots/molecule_count.md) | 0..1 <br/> [integer](../types/integer.md) | Number of instances of a given molecule, defined as bonded atoms or beads | direct |
| [atom_count](../slots/atom_count.md) | 0..1 <br/> [integer](../types/integer.md) | Number of atoms in a molecule | direct |
| [monomer_count](../slots/monomer_count.md) | 0..1 <br/> [integer](../types/integer.md) | Number of monomeric units in a polymer(e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SystemComposition](../classes/SystemComposition.md) | [molecule_ID](../slots/molecule_ID.md) | range | [MoleculeID](../classes/MoleculeID.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://CCPBioSim.ac.uk/biosim-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://CCPBioSim.ac.uk/biosim-schema/MoleculeID |
| native | https://CCPBioSim.ac.uk/biosim-schema/MoleculeID |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MoleculeID
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
slots:
- PDB_ID
- UNIPROT_ID
- SMILES
- InChI
- InChIKey
- alphafold_ID
- PubChem_CID
- protein_sequence
- nucleic_sequence
- predicted_structure
- modified
- molecular_formula
- molecular_weight
- molecule_charge
- molecule_count
- atom_count
- monomer_count

```
</details>

### Induced

<details>
```yaml
name: MoleculeID
from_schema: https://CCPBioSim.ac.uk/biosim-schema/
attributes:
  PDB_ID:
    name: PDB_ID
    annotations:
      database:
        tag: database
        value: PDB
      prefix:
        tag: prefix
        value: pdb
      base_uri:
        tag: base_uri
        value: 'https://identifiers.org/pdb:'
    description: Protein Data Bank identifier
    examples:
    - value: 2VB1
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - PDB ID
    rank: 1000
    is_a: identifier
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^[0-9A-Za-z]{4}$
  UNIPROT_ID:
    name: UNIPROT_ID
    annotations:
      database:
        tag: database
        value: UNIPROT
      prefix:
        tag: prefix
        value: uniprot
      base_uri:
        tag: base_uri
        value: 'https://identifiers.org/uniprot:'
    description: UniProt accession ID
    examples:
    - value: P0DP23
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - UNIPROT ID
    rank: 1000
    is_a: identifier
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^[A-Z0-9]{6,10}$
  SMILES:
    name: SMILES
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: SMILES
    description: Simplified Molecular Input Line Entry System (SMILES) ASCII-based
      line notation used to describe chemical structures. It represents molecular
      graphs with atoms and bonds, allowing software to convert these short strings
      into 2D or 3D models.
    examples:
    - value: CN1C=NC2=C1C(=O)N(C(=O)N2C)C
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - SMILES
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^[A-Za-z0-9@+\-\[\]()=#$:./\\%*]+$
  InChI:
    name: InChI
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: InChI
    description: The International Chemical Identifier (InChi) is a textual identifier
      for chemical substances, designed to provide a standard way to encode molecular
      information
    examples:
    - value: InChI=1S/C8H10N4O2/c1-10-4-9-6-5(10)7(13)12(3)8(14)11(6)2/h4H,1-3H3
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - InChI
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^InChI=1S?/[A-Za-z0-9.+\-]+(/[a-z][^/]*)*$
  InChIKey:
    name: InChIKey
    annotations:
      database:
        tag: database
        value: IUPAC
      prefix:
        tag: prefix
        value: inchikey
      base_uri:
        tag: base_uri
        value: 'https://identifiers.org/inchikey:'
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: InChIKey
    description: The condensed, 27 character InChIKey, which is a hashed version of
      the full InChI (using the SHA-256 algorithm), designed to allow for easy web
      searches of chemical compounds.
    examples:
    - value: RYYVLZVUVIJVGH-UHFFFAOYSA-N
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - InChIKey
    rank: 1000
    is_a: identifier
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^[A-Z]{14}-[A-Z]{10}(-[A-Z])?$
  alphafold_ID:
    name: alphafold_ID
    annotations:
      database:
        tag: database
        value: AlphaFoldDB
      base_uri:
        tag: base_uri
        value: https://alphafold.ebi.ac.uk/entry/
    description: AlphaFold predicted protein structure identifier (AlphaFold DB, EMBL-EBI)
    examples:
    - value: AF-P12345-F1
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - AlphaFold ID
    rank: 1000
    is_a: identifier
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^AF-[A-Z0-9]+-F1$
  PubChem_CID:
    name: PubChem_CID
    annotations:
      database:
        tag: database
        value: PubChem
      prefix:
        tag: prefix
        value: pubchem.compound
      base_uri:
        tag: base_uri
        value: 'https://identifiers.org/pubchem.compound:'
    description: PubChem CID of chemical molecules and their activities against biological
      assays.
    examples:
    - value: '100101'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    aliases:
    - PubChem CID
    rank: 1000
    is_a: identifier
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^\d+$
  protein_sequence:
    name: protein_sequence
    annotations:
      textarea:
        tag: textarea
        value: true
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: protein_sequence
    description: One letter sequence for protein amino acids.
    examples:
    - value: DRVYIHPF
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^[ACDEFGHIKLMNPQRSTVWY]+$
  nucleic_sequence:
    name: nucleic_sequence
    annotations:
      textarea:
        tag: textarea
        value: true
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: nucleic_sequence
    description: One letter sequence for nucleic acid nucleotides.
    examples:
    - value: ATGCATCGATCGATCGATCG
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^[ACGTURYSWKMBDHVN]+$
  predicted_structure:
    name: predicted_structure
    description: Are the molecule positions derived from a prediction?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: boolean
  modified:
    name: modified
    description: Has the initial model been modified from the original?
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    - WaterPotential
    - ProteinPotential
    - LipidPotential
    - NucleicPotential
    - CarbohydratePotential
    - PolymerPotential
    - GeneralPotential
    - MachineLearnedPotential
    range: boolean
  molecular_formula:
    name: molecular_formula
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: molecular_formula
    description: The molecular formula of a molecule\
    examples:
    - value: C8H10N4O2
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: string
    pattern: ^([A-Z][a-z]?\d*)+$
  molecular_weight:
    name: molecular_weight
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: molecular_weight
          unit: g/mol
    description: The molecular weight of a molecule.
    examples:
    - value: '18.0'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: MassQuantity
  molecule_charge:
    name: molecule_charge
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: molecule_charge
          unit: e
    description: Electrostatic charge of a molecule.
    examples:
    - value: '-1.0'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: ChargeQuantity
    pattern: ^[+-]?\d+(\.\d+)?$
  molecule_count:
    name: molecule_count
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: molecule_count
    description: Number of instances of a given molecule, defined as bonded atoms
      or beads.
    examples:
    - value: '1'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: integer
    minimum_value: 0
  atom_count:
    name: atom_count
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: atom_count
    description: Number of atoms in a molecule.
    examples:
    - value: '1'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: integer
    minimum_value: 0
  monomer_count:
    name: monomer_count
    annotations:
      engine_mapping:
        tag: engine_mapping
        value:
        - engine: toptrajparser
          key: monomer_count
    description: Number of monomeric units in a polymer(e.g. protein or nucleic acid).
    examples:
    - value: '1'
    from_schema: https://CCPBioSim.ac.uk/biosim-schema/
    rank: 1000
    owner: MoleculeID
    domain_of:
    - MoleculeID
    range: integer
    minimum_value: 0

```
</details></div>
