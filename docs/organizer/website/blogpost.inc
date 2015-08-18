:orphan:

Writing a Blog Post
===================

.. startblog


We accept posts (from anyone!) for the PyLadies blog. Here is a guest post that you should read as samples of what we're looking for: `Get the Most Out of Your Conference-Going Experience`_.


Topics
^^^^^^

We're looking for posts about Python and the ladies doing cool things with it. Our audience includes both experts and newer programmers. If you're writing a more expert level post, consider pointing newer programmers to resources to get started with.

.. note::

    We reserve the right to decline posts, or work to improve the work of the post.

Attribution
^^^^^^^^^^^

Cite your sources! Either link to them in your post, or the old-fashioned academic Chicago MLA style of "quoting someone's work"(FooPyLady) with an entry for "FooPyLady" at the bottom of your post (or any other MLA styling).

**Also** Please include whether:

1. You want to be noted as the author
2. If so, what name you want to use
3. If we can link to you somehow, either through Twitter handle, email, or website.

Anonymous submissions are fine.

Length
^^^^^^

Posts should be 500 words in length. If your post is much longer (thousands of words), consider whether it could be broken into two connected posts.

Images
^^^^^^

If you wish to include images, they must be 500 pixels wide or less. You must own the images you're submitting, or they must be available under a Creative Commons license.

The Markdown_ syntax is a bit limiting when wanting to add style to the image.  Therefore, if you want to add style to it (e.g. different alignment than default, add a border, rounded corners, etc.) then just write plain HTML inside your Markdown document.

.. code-block:: html

    <img src="{{ get_asset('images/foo.png') }}" width="400" class="my-foo-image" style="any extra styling"/>

.. _blogheaders:

Formatting the Blog Post File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Write your guest post in Markdown and save it in the ``www/_posts`` directory.

    - Suggestion #1: Mou.app for mac is created for Markdown - gives you a preview while you write
    - Suggestion #2: `dillinger`_ is a web app that provides a live preview when you're writing in Markdown.
    - A `cheatsheet`_ for Markdown commands.
2. The very top of the blog post needs the following (including the three dashes before and after the layout/title/tags):


.. code-block:: yaml

    ---
    layout: post.html
    title: "Your title here"
    tags: [list, of relevant, tags]
    author: Name, or blank/none
    author_link: Twitter/Blog/etc or blank/none
    ---


Process
^^^^^^^

1. Setup your machine by following the :ref:`setupenv` instructions .
2. Save the file in ``www/_posts``.
3. Test your changes locally. Start up mynt as per the :ref:`instructions below <usingmynt>`.
4. Make sure that your changes look good, and that there are no errors or formatting issues. If you find problems, stop mynt, make the changes, restart, and check the site again.
5. Commit your changes, and push to **your** fork of the `pyladies/pyladies`_ repository.
6. Create a pull request against the `pyladies/pyladies`_ repo.

When you submit a pull request, everyone with commit access for Pyladies will see it.  You may also ping the `organizers list`_ for more eyes to review.


.. _pyladies/pyladies: https://github.com/pyladies/pyladies
.. _dillinger: http://dillinger.io/
.. _organizers list: mailto:pyladies-group-organizers@googlegroups.com
.. _cheatsheet: http://daringfireball.net/projects/markdown/syntax
.. _Get the Most Out of Your Conference-Going Experience: http://www.pyladies.com/blog/get-the-most-out-of-your-conference-going-experience/
.. _Markdown: http://daringfireball.net/projects/markdown/syntax
