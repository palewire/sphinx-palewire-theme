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
