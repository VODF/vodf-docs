# Licensed under a 3-clause BSD style license - see LICENSE.rst
import os

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "VODF"
copyright = "2022, VODF Working Group"
author = "VODF Working Group"

# The full version, including alpha/beta/rc tags
release = "0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.mathjax",
    "sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

json_url = "https://github.com/vodf/vodf-docs/tree/main/source/_static/switcher.json"

# Define the version we use for matching in the version switcher.
version_match = os.environ.get("READTHEDOCS_VERSION")
# If READTHEDOCS_VERSION doesn't exist, we're not on RTD
# If it is an integer, we're in a PR build and the version isn't correct.
if not version_match or version_match.isdigit():
    # For local development, infer the version to match from the package.
    if "dev" in release:
        version_match = "latest"
        # We want to keep the relative reference if we are in dev mode
        # but we want the whole url if we are effectively in a released version
        json_url = "/_static/switcher.json"
    else:
        version_match = "v" + release

html_theme_options = {
    # "logo_link": "",
    "github_url": "https://github.com/vodf/vodf-docs",
    "icon_links_label": "Quick Links",
    # "show_nav_level": 4,
    # "navigation_depth": 4,
    "use_edit_page_button": True,
    "navbar_align": "content",
    "navbar_end": ["version-switcher", "navbar-icon-links"],
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
    "header_links_before_dropdown": 6,
    "announcement": "<p>This is an unreleased version, informaton may not be correct</p>",
}

html_context = {
    "github_user": "vodf",
    "github_repo": "vodf-docs",
    "github_version": "main",
    "doc_path": "source",
}

html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]
html_logo = "_static/VODF-logo.svg"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
