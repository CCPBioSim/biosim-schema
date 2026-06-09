Usage
=====

This page describes the day-to-day command-line workflow for biosim-schema:
generating schema outputs, rebuilding LinkML docs, and running verification
checks that mirror CI.

Common generation workflow
--------------------------

Generate derived artefacts used by downstream tools:

.. code-block:: bash

   biosim-schema-generate derived

Generate LinkML markdown documentation in docs/source/linkml:

.. code-block:: bash

   biosim-schema-generate docs

Generate full project outputs (LinkML project artefacts, derived files, docs):

.. code-block:: bash

   biosim-schema-generate all

Verify generated artefacts are up to date (used in CI):

.. code-block:: bash

   biosim-schema-generate verify

If LinkML docs are committed and should also be checked:

.. code-block:: bash

   biosim-schema-generate verify --include-docs

Command reference
-----------------

Available subcommands:

- project: generate full LinkML project artefacts
- jsonld: generate JSON-LD output only
- derived: generate webform fields, engine mappings, and summary files
- docs: generate LinkML markdown docs
- all: run project, derived, and docs generation
- verify: regenerate and fail if tracked generated files differ

Validate example data
---------------------

Schema validation is primarily exercised through tests. For ad hoc validation:

.. code-block:: bash

   linkml-validate -s biosim_schema/schema/biosim_schema.yaml tests/valid_data/test.yaml
