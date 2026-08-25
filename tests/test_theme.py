"""Tests for the theme package registration and rendered layouts."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from palewire import setup

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class ThemeRegistrationTests(unittest.TestCase):
    """Verify Sphinx can discover and register the theme."""

    def test_setup_registers_theme_and_declares_parallel_safety(self) -> None:
        app = Mock()

        metadata = setup(app)

        app.add_html_theme.assert_called_once_with(
            "palewire", str(REPOSITORY_ROOT / "palewire")
        )
        self.assertEqual(
            metadata, {"parallel_read_safe": True, "parallel_write_safe": True}
        )


class ThemeLayoutTests(unittest.TestCase):
    """Verify both supported layouts can render from a minimal project."""

    def test_narrow_layout_builds_without_sidebar(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project_directory = Path(temporary_directory)
            (project_directory / "conf.py").write_text(
                "\n".join(
                    [
                        "from pathlib import Path",
                        f"html_theme_path = [{str(REPOSITORY_ROOT)!r}]",
                        'html_theme = "palewire"',
                        'html_theme_options = {"nosidebar": True}',
                    ]
                )
            )
            (project_directory / "index.rst").write_text(
                "Narrow layout\n=============\n\nA buildable page."
            )
            output_directory = project_directory / "_build"

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "sphinx",
                    "-W",
                    "-b",
                    "html",
                    str(project_directory),
                    str(output_directory),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            page = (output_directory / "index.html").read_text()

        self.assertIn('class="document narrow"', page)
        self.assertNotIn('class="sphinxsidebar"', page)


if __name__ == "__main__":
    unittest.main()
