Contributing to BioSim Schema
=============================

This page explains how to contribute new terms and improvements to the BioSim schema,
how LinkML is used in this repository, and how schema changes flow into downstream
artefacts used by other BioSimDR tools.

What is LinkML
--------------

LinkML is a schema language for defining data models in YAML and generating
downstream representations such as JSON-LD, JSON Schema, Python data models,
and human-readable documentation.

Useful references:

- linkml_docs_
- linkml_schema_guide_
- linkml_validation_

How this Schema is Designed
---------------------------

The root schema is defined in biosim_schema_root_.
It imports domain components from schema_components_folder_.

Design principles used in this project:

- Keep top-level structure stable via the SimulationMetadata root class.
- Group terms by scientific domain in component files.
- Prefer reusable quantity classes for values with units.
- Use engine_mapping annotations on slots to map MD engine-native terms to canonical schema terms.
- Generate derived artefacts from schema source, rather than editing generated files manually.

How to Propose Changes
----------------------

You can contribute through either a GitHub issue or a pull request.

Issue-first workflow (recommended for new terms):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open an issue in biosim_schema_issues_ describing the term, scientific meaning, expected value type, and unit.
2. Include at least one engine-specific key where available, for example gromacs or amber naming.
3. State where the term should live in the schema hierarchy.

Direct pull request workflow:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fork and branch from main.
2. Update relevant schema component file(s) in schema_components_folder_.
3. Regenerate artefacts with the utility command.
4. Run tests and checks.
5. Submit a PR in biosim_schema_pulls_ with rationale and examples.


.. _linkml_docs: https://linkml.io/linkml/
.. _linkml_schema_guide: https://linkml.io/linkml/schemas/
.. _linkml_validation: https://linkml.io/linkml/data/validating-data.html

.. _biosim_schema_root: https://github.com/CCPBioSim/biosim-schema/blob/main/biosim_schema/schema/biosim_schema.yaml
.. _schema_components_folder: https://github.com/CCPBioSim/biosim-schema/tree/main/biosim_schema/schema/components

.. _biosim_schema_issues: https://github.com/CCPBioSim/biosim-schema/issues
.. _biosim_schema_pulls: https://github.com/CCPBioSim/biosim-schema/pulls
