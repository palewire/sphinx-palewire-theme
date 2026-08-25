A Sphinx theme for sites hosted at [palewi.re](https://palewi.re/).

## Installation

Install the theme with pipenv:

```bash
pipenv install palewire-sphinx-theme
```

Then, in your Sphinx project's `conf.py` file, add the following line:

```python
html_theme = "palewire"
```

## Configuration

The theme supports two different layouts, a "wide" layout and a "narrow" layout. The wide layout that includes a sidebar is the default. You can switch to the narrow single-column layout by adding the following line to your `conf.py` file:

```python
html_theme_options = {
    "nosidebar": True,
}
```

When using the wide layout, configure the sidebar with the theme's page
navigation template. It renders links from your site's top-level toctree, not
the current page's section headings. Previous and next page links are rendered
in the responsive footer navigation on mobile.

```python
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "searchbox.html",
    ]
}
```

Do not add `localtoc.html` or `relations.html` to this configuration. Further
configuration of this setting is explained by the [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars).

The theme supports the current Sphinx search form markup. It does not set an
upper bound on Sphinx versions.

## Quick start

Install the theme, then create a minimal Sphinx configuration:

```bash
uv add sphinx-palewire-theme
uvx sphinx-palewire-theme init
```

The initializer asks for the site metadata and creates `conf.py`. It enables
the `palewire` extension, which supplies the standard sidebar and canonical
URL defaults. Use `--layout narrow` for a single-column site or
`--navigation minimal` to hide the sidebar.

For an existing configuration, add these settings:

```python
extensions = ["palewire"]

html_theme = "palewire"
html_baseurl = "https://palewi.re/docs/my-site/"
palewire_layout = "wide"
palewire_navigation = "sidebar"
```

## Development

Install the locked development tools and run the same checks used in CI:

```bash
uv sync --all-groups
uv run pre-commit run --all-files
uv run python -m unittest discover -s tests
uv run sphinx-build -W -b html docs docs/_build/html
uv run sphinx-build -W -b linkcheck docs docs/_build/linkcheck
```
