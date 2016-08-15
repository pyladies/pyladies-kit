# -*- coding: utf-8 -*-
#

extensions = []
project = u'PyLadies Handbook'
copyright = u'2014-2016, PyLadies'

version = '2.1'
release = '2.1.0'

master_doc = 'index'
exclude_patterns = ['_build', '_']
source_suffix = '.rst'


pygments_style = 'sphinx'


html_theme = "pyladies"
html_theme_path = ["_themes"]
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
