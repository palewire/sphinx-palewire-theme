"""Sphinx configuration."""

from datetime import datetime
from importlib.metadata import version as distribution_version

extensions = [
    "myst_parser",
    "palewire",
]
source_suffix = {".md": "markdown"}
root_doc = "index"

project = "Sphinx palewire theme"
author = "Ben Welsh"
copyright = f"{datetime.now().year} Ben Welsh"
release = distribution_version("sphinx-palewire-theme")
version = release
language = "en"

exclude_patterns = ["_build"]
linkcheck_ignore = [r"https://askubuntu\.com/.*"]

html_theme = "palewire"
html_title = project
html_baseurl = "https://palewi.re/docs/"
palewire_layout = "wide"
palewire_navigation = "sidebar"
