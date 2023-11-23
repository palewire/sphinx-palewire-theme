import os


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def setup(app):
    app.require_sphinx("1.6")
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme("palewire", theme_path)
    app.connect("html-page-context", update_context)
    return {"parallel_read_safe": True}
