"""Sphinx configuration for the Python-OC-Lettings-FR documentation."""

import os
import sys
from pathlib import Path

# -- Path setup --------------------------------------------------------------
# Make the Django project importable so autodoc can pull in docstrings from
# models, views, etc.
DOCS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = DOCS_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Minimal environment so Django can be configured without a real .env file
# (used both for local builds and on Read the Docs).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
os.environ.setdefault("SECRET_KEY", "docs-build-secret-key")
os.environ.setdefault("ALLOWED_HOSTS", "localhost")

try:
    import django

    django.setup()
except Exception:  # noqa: BLE001 - autodoc must not crash the whole build
    pass

# -- Project information ------------------------------------------------------

project = "Python-OC-Lettings-FR"
copyright = "2026, Orange County Lettings"
author = "Orange County Lettings"
release = "0.1.0"

# -- General configuration ----------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "myst_parser",
    "sphinxcontrib.mermaid",
]

myst_enable_extensions = [
    "colon_fence",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}
autodoc_mock_imports = ["psycopg2"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": (
        "https://docs.djangoproject.com/en/5.2/",
        "https://docs.djangoproject.com/en/5.2/_objects/",
    ),
}

# -- Options for HTML output ---------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "Python-OC-Lettings-FR"
