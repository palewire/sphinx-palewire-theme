"""Sphinx theme for palewi.re documentation."""

from pathlib import Path

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.errors import ConfigError

DEFAULT_SIDEBARS = ["about.html", "navigation.html", "searchbox.html"]


def _validate_choice(value: str, name: str, choices: set[str]) -> None:
    if value not in choices:
        allowed = ", ".join(sorted(choices))
        raise ConfigError(f"{name} must be one of: {allowed}")


def _configure_theme(_: Sphinx, config: Config) -> None:
    """Apply opt-in site defaults after Sphinx has loaded its configuration."""
    layout = config.palewire_layout
    navigation = config.palewire_navigation
    _validate_choice(layout, "palewire_layout", {"wide", "narrow"})
    _validate_choice(navigation, "palewire_navigation", {"sidebar", "minimal"})

    options = dict(config.html_theme_options)
    if layout == "narrow":
        options.setdefault("nosidebar", True)
    if config.html_baseurl:
        options.setdefault("canonical_url", config.html_baseurl.rstrip("/") + "/")
    config.html_theme_options = options

    sidebars = dict(config.html_sidebars)
    if navigation == "sidebar":
        sidebars.setdefault("**", DEFAULT_SIDEBARS)
    else:
        sidebars.setdefault("**", [])
    config.html_sidebars = sidebars


def setup(app: Sphinx) -> dict[str, bool]:
    """Register the theme and its opt-in configuration defaults."""
    theme_path = str(Path(__file__).parent)
    app.add_html_theme("palewire", theme_path)
    app.add_config_value("palewire_layout", "wide", "html", types=[str])
    app.add_config_value("palewire_navigation", "sidebar", "html", types=[str])
    app.connect("config-inited", _configure_theme)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
