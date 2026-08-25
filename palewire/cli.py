"""Commands for configuring Sphinx projects to use the palewire theme."""

import json
from pathlib import Path

import click

CONFIG_TEMPLATE = '''"""Sphinx configuration for {project}."""

extensions = ["palewire"]

project = {project}
author = {author}
html_theme = "palewire"
html_baseurl = {base_url}
palewire_layout = {layout}
palewire_navigation = {navigation}
'''


@click.group()
def main() -> None:
    """Configure Sphinx projects to use the palewire theme."""


@main.command("init")
@click.option("--project", prompt="Project name")
@click.option("--author", prompt="Author")
@click.option("--base-url", prompt="Published documentation URL")
@click.option(
    "--layout",
    type=click.Choice(["wide", "narrow"], case_sensitive=False),
    default="wide",
    show_default=True,
)
@click.option(
    "--navigation",
    type=click.Choice(["sidebar", "minimal"], case_sensitive=False),
    default="sidebar",
    show_default=True,
)
@click.option(
    "--path",
    type=click.Path(path_type=Path),
    default=Path("conf.py"),
    show_default=True,
)
@click.option("--force", is_flag=True, help="Overwrite an existing configuration file.")
def initialize(
    project: str,
    author: str,
    base_url: str,
    layout: str,
    navigation: str,
    path: Path,
    force: bool,
) -> None:
    """Create a minimal Sphinx configuration for the palewire theme."""
    if path.exists() and not force:
        raise click.ClickException(
            f"{path} already exists. Use --force to overwrite it."
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        CONFIG_TEMPLATE.format(
            project=json.dumps(project),
            author=json.dumps(author),
            base_url=json.dumps(base_url.rstrip("/") + "/"),
            layout=json.dumps(layout),
            navigation=json.dumps(navigation),
        )
    )
    click.echo(f"Created {path}")
