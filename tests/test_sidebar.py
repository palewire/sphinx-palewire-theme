"""Regression tests for Sphinx sidebar compatibility."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class SidebarBuildTests(unittest.TestCase):
    """Verify the theme styles sidebar markup emitted by current Sphinx."""

    def test_relations_and_search_sidebar_is_styled(self) -> None:
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
        self.assertIn("<h4>Next topic</h4>", page)
        self.assertIn('id="searchbox"', page)
        self.assertIn('class="search"', page)
        self.assertIn('type="submit"', page)
        self.assertIn("div.sphinxsidebar h4", stylesheet)
        self.assertIn("div.sphinxsidebar form.search", stylesheet)
        self.assertIn("box-sizing: border-box", stylesheet)


if __name__ == "__main__":
    unittest.main()
