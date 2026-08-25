"""Sphinx configuration for the sidebar regression fixture."""

from pathlib import Path

html_theme = "palewire"
html_theme_path = [Path(__file__).resolve().parents[3]]
html_sidebars = {"**": ["navigation.html", "searchbox.html"]}
