"""Tests for the theme package registration and rendered layouts."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from click.testing import CliRunner

from palewire import setup
from palewire.cli import main

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
        self.assertIn('class="desktop-nav"', page)
        self.assertIn('class="nav-menu-toggle"', page)
        self.assertIn('popovertarget="mobile-nav-links"', page)
        self.assertIn('id="mobile-nav-links" class="nav-drawer" popover', page)
        self.assertIn('popovertargetaction="hide"', page)
        self.assertIn('href="https://palewi.re/guides/"', page)


class ThemeInitializerTests(unittest.TestCase):
    """Verify the starter configuration command."""

    def test_initializer_writes_a_minimal_configuration(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            configuration_path = Path(temporary_directory) / "conf.py"

            result = CliRunner().invoke(
                main,
                [
                    "init",
                    "--project",
                    "Example site",
                    "--author",
                    "Example author",
                    "--base-url",
                    "https://palewi.re/docs/example",
                    "--layout",
                    "narrow",
                    "--navigation",
                    "minimal",
                    "--path",
                    str(configuration_path),
                ],
            )

            configuration = configuration_path.read_text()
            (configuration_path.parent / "index.rst").write_text(
                "Starter site\n============\n\nA buildable page."
            )
            output_directory = configuration_path.parent / "_build"
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "sphinx",
                    "-W",
                    "-b",
                    "html",
                    str(configuration_path.parent),
                    str(output_directory),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            page = (output_directory / "index.html").read_text()

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn('extensions = ["palewire"]', configuration)
        self.assertIn('html_baseurl = "https://palewi.re/docs/example/"', configuration)
        self.assertIn('palewire_layout = "narrow"', configuration)
        self.assertIn('palewire_navigation = "minimal"', configuration)
        self.assertIn('class="document narrow"', page)
        self.assertNotIn('class="sphinxsidebar"', page)
        self.assertIn(
            'rel="canonical" href="https://palewi.re/docs/example/index.html"', page
        )


if __name__ == "__main__":
    unittest.main()
