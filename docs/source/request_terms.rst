Requesting New Metadata Terms
=============================

This page is for researchers and users who want to suggest new metadata terms
for BioSim schema, without editing code.

When To Open A Request
----------------------

Open a request when:

- a term you need is missing
- an existing term is unclear or too narrow
- a unit or allowed value is missing
- a term should be renamed or better described

Before You Submit
-----------------

Please quickly check:

- linkml_docs_ for basic schema concepts
- biosim_schema_issues_ to avoid duplicates
- biosim_schema_root_ to see current top-level structure

How To Submit A Request
-----------------------

Use the metadata_term_request_form_.

If the form is not visible yet, open biosim_schema_issues_ and create a new issue
using the same fields shown below.

Lightweight Issue Template
--------------------------

Please include:

- Title
- Summary
- Why this is needed
- Proposed term name
- Suggested schema location
- Expected value type
- Units (if applicable)
- Example values
- Engine mapping (optional)
- Extra context

Fully Worked Example
--------------------

Title
^^^^^

[Metadata Term]: pressure_relaxation_time

Summary
^^^^^^^

Request to add a term for barostat pressure relaxation time in molecular dynamics metadata.

Why is this needed?
^^^^^^^^^^^^^^^^^^^

Pressure-coupling settings are required to reproduce NPT simulations and compare setups
across engines. This value is commonly reported in methods sections and simulation inputs.

Proposed term name
^^^^^^^^^^^^^^^^^^

Preferred label: pressure_relaxation_time
Alternative labels: tau_p, pressure_time_constant

Where it belongs
^^^^^^^^^^^^^^^^

settings -> barostat

Expected value type
^^^^^^^^^^^^^^^^^^^

float

Units (if applicable)
^^^^^^^^^^^^^^^^^^^^^

ps

Example value(s)
^^^^^^^^^^^^^^^^

- 2.0
- 5.0
- 10.0

Engine-specific mapping (optional but helpful)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- gromacs: tau-p
- amber: barostat_tau (or project-preferred equivalent)

Extra context
^^^^^^^^^^^^^

This term should align with existing pressure-coupling metadata and be compatible
with downstream extraction and webform generation.

Acceptance Notes
----------------

A request is usually easier to review when it includes:

- scientific meaning of the term
- where it fits in the current structure
- example values
- units and engine keys when relevant

What Happens Next
-----------------

After submission:

1. Maintainers review and discuss the request.
2. If accepted, the schema is updated via pull request.
3. Generated artefacts are refreshed by project automation.
4. The new term becomes available to downstream tools.

.. _linkml_docs: https://linkml.io/linkml/
.. _biosim_schema_issues: https://github.com/CCPBioSim/biosim-schema/issues
.. _biosim_schema_root: https://github.com/CCPBioSim/biosim-schema/blob/main/biosim_schema/schema/biosim_schema.yaml
.. _metadata_term_request_form: https://github.com/CCPBioSim/biosim-schema/issues/new?template=metadata_term_request.md&title=%5BMetadata%20Term%5D%3A%20
