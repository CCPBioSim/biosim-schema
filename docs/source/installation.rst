Installation
============

Install ``biosim-schema`` from source to work with the schema definitions,
run validation and tests, and generate downstream artefacts used by BioSimDR tools.

Requirements
------------

- Python 3.12+
- pip
- LinkML toolchain (installed via project dependencies)

Install from source
-------------------

.. code-block:: bash

   conda create -n biosim-schema python=3.14
   conda activate biosim-schema
   git clone https://github.com/CCPBioSim/biosim-schema.git
   cd biosim-schema
   pip install -e .

Optional dependency groups
--------------------------

.. code-block:: bash

   pip install -e ".[testing]"
   pip install -e ".[docs]"
   pip install -e ".[pre-commit]"
