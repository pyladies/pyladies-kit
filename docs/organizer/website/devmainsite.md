---
orphan: true
---

# Developing the Main Website

Is there some CSS inconsistency that's bugging you?  Is the site missing some accessibility?  Want to add a new page or content?  Cool!  Here's how to get started.

```{note}
When changing the website or adding content - beyond adding your location information - it is a good idea to email the [organizers list] to ask for others' feedback on your ideas, either before you start developing, or when you make the pull request.
```

### Current Layout

The website lives in the [pyladies/pyladies], as well as many locations' websites, where `www` is the main website, and the other directories map to subdomains, more or less.

The website consists of just static HTML, CSS, and some client-side JavaScript.  We use [mynt] to convert [Markdown] files into HTML files (using [Jinja2] templates).

The general layout for the `www` directory:

```
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
```

When you first run `mynt` (detailed below), it will also create a `_site` directory, where the complete site will be living.  This `_site` directory is **not** committed within the repository.

```{note}
The HTML files here are just *templates*.  You must first run `mynt gen -f _site` ({ref}`detailed below <usingmynt>`) to generate the HTML to see what will be on the website.
```

[fork]: https://help.github.com/articles/fork-a-repo
[jinja2]: http://jinja.pocoo.org/docs/dev/
[markdown]: http://daringfireball.net/projects/markdown/syntax
[mynt]: http://mynt.uhnomoli.com/
[organizers list]: mailto:pyladies-group-organizers@googlegroups.com
[pyladies/pyladies]: https://github.com/pyladies/pyladies
