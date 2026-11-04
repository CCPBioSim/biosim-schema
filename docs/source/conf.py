# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import importlib.metadata

project = "biosim-schema"
copyright = "2026, CCPBioSim"
release = importlib.metadata.version("biosim-schema")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "myst_parser",
    "sphinxcontrib.mermaid",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = []
suppress_warnings = [
    "toc.not_included",  # not all md files need to be in toc
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "ccpbiosim_sphinx_theme"
html_context = {"github_repo": "biosim-schema"}
html_static_path = ["_static"]


# The schema reference under linkml/ is generated during the build and is not
# in the repository, so its pages have no source file on GitHub to edit.
def hide_edit_button_on_generated_pages(app, pagename, templatename, context, doctree):
    if pagename.startswith("linkml/"):
        context["theme_use_edit_page_button"] = False


def setup(app):
    app.connect("html-page-context", hide_edit_button_on_generated_pages)
