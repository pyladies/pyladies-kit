# -*- coding: utf-8 -*-
#
project = "PyLadies Handbook"
copyright = "2014-2024, PyLadies"
html_title = "PyLadies Handbook"
html_short_title = "PyLadies Kit"
version = "2024.01"
release = ""

extensions = [
    "myst_parser",
    "sphinx.ext.viewcode",
    "sphinxext.opengraph",
]

master_doc = "index"
exclude_patterns = ["_build", "_"]
source_suffix = ".rst"

html_theme = "furo"


html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_use_smartypants = True
htmlhelp_basename = "PyLadiesHandbookdoc"
html_logo = "_static/images/pylady_geek_rainbow.png"

latex_documents = [
    (
        "index",
        "PyLadiesHandbook.tex",
        "PyLadies Handbook Documentation",
        "PyLadies",
        "manual",
    ),
]
man_pages = [
    (
        "index",
        "pyladieshandbook",
        "PyLadies Handbook Documentation",
        ["PyLadies"],
        1,
    )
]
texinfo_documents = [
    (
        "index",
        "PyLadiesHandbook",
        "PyLadies Handbook Documentation",
        "PyLadies",
        "PyLadiesHandbook",
        "One line description of project.",
        "Miscellaneous",
    ),
]

html_context = {
    "display_github": True,
    "github_user": "pyladies",
    "github_repo": "pyladies-kit",
}

linkcheck_timeout = 5

# MyST extension configuration
myst_heading_anchors = 6
suppress_warnings = ["myst.header", "myst.strikethrough"]
html_theme_options = {
    "light_css_variables": {"color-announcement-background": "#e51e41"},
    "sidebar_hide_name": True,
    "source_repository": "https://github.com/pyladies/pyladies-kit/",
    "source_branch": "master",
    "source_directory": "docs/",
}
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "smartquotes",
    "strikethrough",
    "tasklist",
]

set_announcement = True
# one string per line - in HTML markup
announcement_lines = [
    """Introducing the new <b><a href="https://pyladies.com/blog/Announcing-The-Outstanding-PyLady-Award/outstanding-award/">Outstanding PyLady Award</a>!</b>!""",
    """<b>PyCon US 2024:</b> Check out the <a href="https://pyladies.com/blog/PyLadies-at-PyCon-US-2024/pyladies-at-pycon-us/">PyLadies representation</a> at this year's PyCon!""",
]
current_announcement_html = "<br/>".join(announcement_lines)
if set_announcement:
    html_theme_options["announcement"] = current_announcement_html
