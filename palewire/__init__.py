from pathlib import Path


def setup(app):
    theme_path = Path(__file__).parent.absolute()
    app.add_html_theme("palewire", str(theme_path))
    return {'parallel_read_safe': True, 'parallel_write_safe': True}