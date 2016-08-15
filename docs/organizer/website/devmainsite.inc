:orphan:

Developing the Main Website
===========================

.. startdev

Is there some CSS inconsistency that's bugging you?  Is the site missing some accessibility?  Want to add a new page or content?  Cool!  Here's how to get started.

.. note::

    When changing the website or adding content - beyond adding your location information - it is a good idea to email the `organizers list`_ to ask for others' feedback on your ideas, either before you start developing, or when you make the pull request.

Current Layout
~~~~~~~~~~~~~~

The website lives in the `pyladies/pyladies`_, as well as many locations' websites, where ``www`` is the main website, and the other directories map to subdomains, more or less.

The website consists of just static HTML, CSS, and some client-side JavaScript.  We use mynt_ to convert Markdown_ files into HTML files (using Jinja2_ templates).

The general layout for the ``www`` directory::

    .
    ├── _assets        # JavaScript, images/logos, fonts, and CSS stuff goes here
    ├── _posts         # these are the blog posts written in markdown
    ├── _templates     # these are the base templates that other things use.
    ├── about/         # any directory maps to a URL path, e.g. www.pyladies.com/about,
    ├── archives/      #     and contains its HTML Jinja template
    ├── blog/
    ├── CodeOfConduct/
    ├── config.yml     # configuration for the overall site
    ├── feed.xml       # RSS feed that is automatically generated
    ├── index.html     # HTML Jinja template for the main page, www.pyladies.com
    ├── locations/
    ├── resources/
    └── sponsor/


When you first run ``mynt`` (detailed below), it will also create a ``_site`` directory, where the complete site will be living.  This ``_site`` directory is **not** committed within the repository.

.. note::

    The HTML files here are just *templates*.  You must first run ``mynt gen -f _site`` (:ref:`detailed below <usingmynt>`) to generate the HTML to see what will be on the website.



.. _pyladies/pyladies: https://github.com/pyladies/pyladies
.. _organizers list: mailto:pyladies-group-organizers@googlegroups.com
.. _Markdown: http://daringfireball.net/projects/markdown/syntax
.. _Jinja2: http://jinja.pocoo.org/docs/dev/
.. _Fork: https://help.github.com/articles/fork-a-repo
.. _mynt: http://mynt.uhnomoli.com/
