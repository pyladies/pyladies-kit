# -*- coding: utf-8 -*-
#

extensions = [
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

project = u'PyLadies Handbook'
copyright = u'2014-2020, PyLadies'


try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

version = '2020.03'
release = ''

master_doc = 'index'
exclude_patterns = ['_build', '_']
source_suffix = '.rst'


pygments_style = 'sphinx'

if sphinx_rtd_theme:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = "default"

html_sidebars = {
    '**': [
        'nav.sidebar.html',
        'nav.global.html',
        'searchbox.html',
    ]
}
html_style = "css/custom.css"
html_title = "PyLadies Organizer Handbook"
html_short_title = "PyLadies Kit"
html_favicon = "_static/favicon.ico"
html_static_path = ['_static']
html_use_smartypants = True
htmlhelp_basename = 'PyLadiesHandbookdoc'

latex_documents = [
    ('index', 'PyLadiesHandbook.tex', u'PyLadies Handbook Documentation',
     u'PyLadies', 'manual'),
]
man_pages = [
    ('index', 'pyladieshandbook', u'PyLadies Handbook Documentation',
     [u'PyLadies'], 1)
]
texinfo_documents = [
    ('index', 'PyLadiesHandbook', u'PyLadies Handbook Documentation',
     u'PyLadies', 'PyLadiesHandbook', 'One line description of project.',
     'Miscellaneous'),
]

html_context = {
    'display_github': True,
    'github_user': 'pyladies',
    'github_repo': 'pyladies-kit',
}