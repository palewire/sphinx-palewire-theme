# Working in this repository

This is a Python Sphinx theme. Use `uv` for all Python commands. Do not add
Pipenv files or use unpinned dependency installs.

## Setup and checks

```bash
uv sync --all-groups
uv run pre-commit run --all-files
uv run python -m unittest discover -s tests
uv run sphinx-build -W -b html docs docs/_build/html
uv build
```

Run the narrowest relevant check while working, then run all four checks before
opening a pull request. Keep template and CSS changes covered by a rendering
test when practical.

## Change guidelines

- Support Python 3.9 through 3.11.
- Keep the published package free of development files and generated output.
- Do not change release or branch-protection settings without documenting why
  in the pull request.
- Do not commit `.venv`, Sphinx output, coverage data, or agent scratch files.
