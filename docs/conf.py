import os
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, os.path.abspath('..'))

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
templates_path = ["_templates"]
source_suffix = ".md"
master_doc = "index"

project = "Sphinx palewire theme"
copyright = f"{datetime.now().year} Ben Welsh"

exclude_patterns = ["_build"]

html_theme = "palewire"
html_theme_path = [
    Path(__file__).parent.parent.absolute(),
]
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "searchbox.html",
    ]
}
html_theme_options = {
    "description": "A light, configurable Sphinx theme",
    "github_user": "palewire",
    "github_repo": "sphinx-palewire-theme",
    "fixed_sidebar": True,
}