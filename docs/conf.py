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
    "sphinx.ext.githubpages",
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

# MyST extension configuration
myst_heading_anchors = 6
suppress_warnings = ["myst.header", "myst.strikethrough"]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "smartquotes",
    "strikethrough",
    "tasklist",
]
