"""Sphinx configuration."""

import os
import sys
from typing import Any
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.abspath(".."))

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
html_sidebars: Any[Any] = {
    "**": [
        "about.html",
        "navigation.html",
    ]
}
html_theme_options: Any[Any] = {
    # "nosidebar": True,
}
