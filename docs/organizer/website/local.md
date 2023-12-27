# Create a Chapter Website

Ready to setup your location's website? Great!

## Domain Setup

*Domain admins:* currently [Esther Nam] and [Lynn Root]

```{warning}
Please **DO NOT** purchase your own separate domain!
```

We will easily setup a subdomain on the `pyladies.com` site for you (e.g. `nyc.pyladies.com`).  It's also possible if you'd prefer to use the `pyladies.org` namespace (e.g. `nyc.pyladies.org`).  We can also do `pyladies.com/nyc` or `pyladies.org/nyc` too.  Your choice!

If you are in a location that frequently uses other TLDs, e.g. `.co.uk`, please contact our domain administrators listed above.

## Developing the Website

You have two options: a {ref}`static` website, or a {ref}`dynamic` website.  Whichever you prefer!  And you can switch over any time.  It may be easier/quicker for you to start with a static website - then create a dynamic website when you have more time.

(static)=

### Static Website

A static website is just HTML, CSS, and client-side JavaScript (exactly like the current `www.pyladies.com` site is set up).  It's great if you don't want a database or server-side logic; it's really easy to maintain.

#### Current Examples

There are plenty of PyLadies locations that have simple static websites.  Here are a couple:

- [remote.pyladies.com]: [remote codebase](https://github.com/pyladies/pyladies/tree/master/remote)
- [boston.pyladies.com]: [boston codebase](https://github.com/pyladies/pyladies/tree/master/boston)
- [nyc.pyladies.com]: [nyc codebase](https://github.com/pyladies/pyladies/tree/master/nyc)

#### Process

If you're interested in the various static website tools out there, check out {ref}`tools`.

To setup your static website:

1. Fork the [pyladies/pyladies] repository to your own (or your local PyLadies) GitHub account.
2. Locally clone **your** fork of the repository.
3. Create a directory within the main `pyladies` folder of the repository (on the same directory level as `www` and the other subdomains.)
4. Develop the website within your new directory.
5. Be sure to add a `README.md` file that explains how to create the HTML files if you are using a static site generator (like [here]).
6. Commit the code locally, and push it up to **your** fork.
7. Make a pull request against the `pyladies/pyladies` repository.

```{note}
When making a pull request, please squash all your commits into one commit!  We like a clean history!  Here's a good how-to on [git rebase] to squash commits.
```

```{note}
In your pull request - please include the desired subdomain namespace - e.g. `nyc.pyladies.com`
```

```{note}
Be sure that the subdomain information in [www/config.yml] within the [pyladies/pyladies] repository matches the subdomain of your website!  Lots of linking-magic goes on.
```

(tools)=

#### Tools

You can hand-write all your HTML files, but that's a bit of a pain.  Here are a list of tools that can help create your static website for you:

##### Mynt

[mynt] is a static site generator written in Python.  This is the tool that the main PyLadies site - [www.pyladies.com](http://www.pyladies.com) uses.

You write the content of your site in [Markdown] format, design the layout and organization of the site (e.g. how the content will be presented) using [Jinja2] templates (another Python library), and edit/create your own themes with CSS.  Running `mynt gen` over your Markdown & CSS files and Jinja2 templates will create static HTML files that you can then view via the `mynt serve` command.

##### Pelican

Extremely similar to [mynt], [pelican] is another static site generator written in Python.  It's the same process - write in [Markdown], organize via [Jinja2] tempaltes, and edit your theme with CSS.

Pelican does offer a bigger user base than [mynt], and therefore has many plugins and themes already setup to use.

##### Other Python Static Site Generators

Some others if you're curious:

- [nikola]
- [hyde]
- [Frozen Flask]
- [Sphinx] (generally used for project documentation but can easily be used for this)
- [mkdocs] (similar to Sphinx - generally used for project docs but easily used for this)

##### Other Non-Python Static Site Generators

It's totally okay to use a non-Python package(s) to help make your website.  Here's a list of common & widely-used ones:

- [Jekyll] (Ruby)
- [Octopress] (Ruby)
- [GitBook] (JavaScript)
- A [nice list of static site generators]

(dynamic)=

### Dynamic Website

A dynamic website goes beyond simple HTML/CSS/JavaScript.  A website written with [Django] or [Flask] is a dynamic website (and it's okay if you want to use a non-Python web framework, so long as it's supported by [Heroku]).

#### Current Examples

There are a few PyLadies locations that have built their own dynamic websites.  Here are a couple:

- [australia.pyladies.com]
- [tw.pyladies.com]
- [brasil.pyladies.com]

#### Process

If you're interested in the various dynamic website frameworks out there, check out {ref}`frameworks`.

To setup your dynamic website:

1. Create your own git repository (ideally under your local PyLadies GitHub account, registered under your `pyladies.com` email address).
2. Create your website.
3. Create a free [Heroku account] with your PyLadies email address, if you haven't already.  Be sure to download the [Heroku toolbelt] for easy application setup and deployment.
4. When you're ready to deploy, ping the domain admins (above).  They will set up your PyLadies email address to an admin-managed Heroku app (which will give your PyLadies complete access for deployment) as well as setup all the DNS records needed.
5. Log into your Heroku account and follow the instructions for deploying (available under newly-created application that the admins made).

(frameworks)=

#### Frameworks

(django)=

(flask)=

[australia.pyladies.com]: http://australia.pyladies.com/
[boston.pyladies.com]: http://boston.pyladies.com
[brasil.pyladies.com]: http://brasil.pyladies.com/
[django]: https://devcenter.heroku.com/categories/language-support
[esther nam]: mailto:esthernam@gmail.com
[flask]: https://devcenter.heroku.com/categories/language-support
[frozen flask]: http://packages.python.org/Frozen-Flask/
[git rebase]: http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html
[gitbook]: https://www.staticgen.com/gitbook
[here]: https://github.com/pyladies/pyladies#to-run-locally
[heroku]: https://devcenter.heroku.com/categories/language-support
[heroku account]: https://signup.heroku.com/www-header
[heroku toolbelt]: https://toolbelt.heroku.com/
[hyde]: http://hyde.github.io/
[jekyll]: https://www.staticgen.com/jekyll
[jinja2]: http://jinja.pocoo.org/docs/dev/
[lynn root]: mailto:lynn@pyladies.com
[markdown]: http://daringfireball.net/projects/markdown/syntax
[mkdocs]: https://www.staticgen.com/mkdocs
[mynt]: http://mynt.uhnomoli.com/
[nice list of static site generators]: https://www.staticgen.com/
[nikola]: https://getnikola.com/
[nyc.pyladies.com]: http://nyc.pyladies.com
[octopress]: https://www.staticgen.com/octopress
[pelican]: http://pelican.readthedocs.org/en/latest/
[pyladies/pyladies]: https://github.com/pyladies/pyladies
[remote.pyladies.com]: http://remote.pyladies.com
[sphinx]: http://sphinx.pocoo.org/
[tw.pyladies.com]: http://tw.pyladies.com
[www/config.yml]: https://github.com/pyladies/pyladies/blob/master/www/config.yml
