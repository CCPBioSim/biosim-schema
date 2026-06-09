Development Workflow
====================

This page explains how generation, pre-commit, CI, and tests work together.


Set up Development Environment
------------------------------

.. code-block:: bash

   git clone https://github.com/CCPBioSim/biosim-schema.git
   cd biosim-schema
   conda create -n biosim-schema python=3.14
   conda activate biosim-schema
   pip install -e ".[testing,docs,pre-commit]"


Simple Example: Add a New Term
------------------------------

Example addition:

.. code-block:: yaml

   slots:
     pressure_relaxation_time:
       description: Relaxation time used by barostat coupling.
       range: TimeQuantity
       annotations:
         engine_mapping:
           - engine: gromacs
             key: tau-p
             unit: ps

Then attach it to the relevant class slot list, regenerate artefacts, and include
a concise note in the pull-request describing engine mapping and units.

How Schema Changes Propagate to Downstream Artefacts
----------------------------------------------------

The generation utility is implemented in generate_artifacts_utility_.

Use the utility command:

.. code-block:: bash

   biosim-schema-generate derived

Derived files are produced as:

- webform_fields_artefact_
- engine_mappings_artefact_
- schema_summary_artefact_

These generated outputs are consumed by downstream BioSimDR tools:

- biosim-extractor uses engine mappings to populate canonical metadata.
- biosimdb-interface uses webform fields and schema paths to drive form rendering and validation.

Submitting Changes
------------------

1. Create a branch from ``main``.
2. Add or update schema, tests, and generated artefacts as needed.
3. Regenerate artefacts and run tests/checks locally.
4. Build docs locally to confirm there are no documentation errors.
5. Open a pull request in biosim_schema_pulls_ with a concise change summary.

Minimal Local Workflow
----------------------

Run artefact generation after schema edits:

.. code-block:: bash

   biosim-schema-generate derived

Run tests:

.. code-block:: bash

   pytest

Or, additionally check coverage with tests:

.. code-block:: bash

    pytest --cov=biosimd_schema --cov-report=term-missing

Add tests if applicable.

Run formatting and lint checks:

.. code-block:: bash

   ruff check .
   ruff format --check .

Docs
----

LinkML markdown generation
~~~~~~~~~~~~~~~~~~~~~~~~~~

LinkML schema pages are generated as Markdown files under ``docs/source/linkml``
using the project utility:

.. code-block:: bash

   biosim-schema-generate docs

Internally, this runs ``gen-doc`` from LinkML against
``biosim_schema/schema/biosim_schema.yaml`` and writes one page per schema
entity (classes, slots, enums, and types), plus an index page.

A small post-processing step is applied to generated files to fix known
formatting issues (for example malformed ``---#`` type headers and ``puml``
fences) before Sphinx builds the documentation.

Sphinx reStructuredText content generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation pages (excluding schema entities) are generated under ``docs/source``.

Sphinx content is built with:

.. code-block:: bash

   make -C docs clean html

Schema validation tests
-----------------------

Schema validation is performed in pytest, not as an import-time script. Tests in
``tests/test_validation/test_schema_validation.py`` validate:

- a known valid payload passes
- intentionally invalid payloads fail (for example wrong type or enum value)

This keeps schema validation deterministic and CI-friendly.

Pre-commit behavior
-------------------

Manually run pre-commit with:

.. code-block:: bash

   pre-commit run --all-files

Pre-commit runs local hooks before commit. The generation hook updates derived
artefacts so contributors do not need to remember manual regeneration.

Typical flow:

1. Edit schema or extraction logic.
2. Run ``git commit``.
3. Pre-commit regenerates derived files.
4. Stage modified generated files and re-run commit.

If generated files changed, this is expected: pre-commit is keeping outputs in sync.

CI and Quality Gates
--------------------

CI verifies that generated artefacts are reproducible and tests pass.
See ci_workflow_ for:

- **tests**: runs pytest across supported OS/Python versions.
- **generated-artifacts**: runs ``biosim-schema-generate verify`` to ensure committed generated outputs are reproducible.
- **docs**: generates LinkML docs and builds Sphinx HTML.

This ensures local generation and CI validation stay aligned, and schema contributions remain consistent for downstream tooling.

.. _generate_artifacts_utility: https://github.com/CCPBioSim/biosim-schema/blob/main/biosim_schema/utils/generate_artifacts.py

.. _webform_fields_artefact: https://github.com/CCPBioSim/biosim-schema/blob/main/project/schema_webformfields.json
.. _engine_mappings_artefact: https://github.com/CCPBioSim/biosim-schema/blob/main/project/schema_enginemappings.json
.. _schema_summary_artefact: https://github.com/CCPBioSim/biosim-schema/blob/main/project/schema_summary.yaml

.. _biosim_schema_pulls: https://github.com/CCPBioSim/biosim-schema/pulls

.. _ci_workflow: https://github.com/CCPBioSim/biosim-schema/blob/main/.github/workflows/biosim_schema_project-ci.yaml
