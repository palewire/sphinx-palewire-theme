"""Regression tests for Sphinx sidebar compatibility."""

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class SidebarBuildTests(unittest.TestCase):
    """Verify the theme styles sidebar markup emitted by current Sphinx."""

    def test_sidebar_has_page_navigation_and_mobile_footer_pagination(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            source_directory = REPOSITORY_ROOT / "tests" / "fixtures" / "sidebar"
            output_directory = Path(temporary_directory) / "output"

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "sphinx",
                    "-b",
                    "html",
                    str(source_directory),
                    str(output_directory),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            page = (output_directory / "guide.html").read_text()
            stylesheet = (output_directory / "_static" / "palewire.css").read_text()

        self.assertIn("_static/palewire.css", page)
        navigation = re.search(
            r'<nav class="sphinxsidebar-navigation"[^>]*>(.*?)</nav>',
            page,
            re.DOTALL,
        )
        self.assertIsNotNone(navigation)
        assert navigation is not None
        self.assertIn("Getting started", navigation.group(1))
        self.assertIn("Buildable views", navigation.group(1))
        self.assertIn("Settings", navigation.group(1))
        self.assertNotIn("Build a view", navigation.group(1))
        self.assertNotIn("<h4>Previous topic</h4>", page)
        self.assertNotIn("<h4>Next topic</h4>", page)
        self.assertIn('id="searchbox"', page)
        self.assertIn('class="search"', page)
        self.assertIn('type="submit"', page)
        self.assertIn('id="rellinks" aria-label="Related pages"', page)
        self.assertIn('title="Previous document"', page)
        self.assertIn('title="Next document"', page)
        self.assertIn("div.sphinxsidebar h4", stylesheet)
        self.assertIn("div.sphinxsidebar .sphinxsidebar-relations", stylesheet)
        self.assertIn("nav#rellinks {\n  display: none;", stylesheet)
        self.assertIn(
            "@media screen and (max-width: 875px) {\n"
            "    nav#rellinks {\n"
            "        display: block;",
            stylesheet,
        )
        self.assertIn("div.sphinxsidebar form.search", stylesheet)
        self.assertIn("box-sizing: border-box", stylesheet)
        relations_template = (
            REPOSITORY_ROOT / "palewire" / "relations.html"
        ).read_text()
        self.assertIn('class="sphinxsidebar-relations"', relations_template)


if __name__ == "__main__":
    unittest.main()
