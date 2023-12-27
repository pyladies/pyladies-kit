---
orphan: true
---

# Making a Simple Location Page

Don't have time to make your {doc}`own local website <local>`?  Not a problem - if you have a few minutes, you can make a simple "place holder" page.

For the sake of having an example, let's say our new location is "Foo City"

1. Create a directory within `www/locations` named after your location (this will be your URL path - e.g. `www.pyladies.com/locations/foo`).
2. Create a new `index.html` within the directory you just created.
3. Copy & edit the following HTML/Jinja template to the `index.html` file.

```jinja
{% extends "site.html" %}
{% block title %}PyLadies Foo City{% endblock %}
{% block content %}
    <section id="archive">
        <h1>PyLadies Foo City</h1>
            <article>
                <ul class="social">
                    <aside>
                        <h4><a href="{{ get_url("locations/foo") }}">Foo City</a> | <a class="social icon vcard" data-icon="&#59170;" href="mailto:foocity@pyladies.com" title"Contact"></a><a class="social icon twitter" data-icon="&#62217;" title="Twitter" href="https://twitter.com/pyladies_foo"></a><a class="social icon location" data-icon="&#59172;" title="Meetup Link" href="http://www.meetup.com/pyladies-foo"></a></h4>

                    </aside>
                </ul>
            </article>
    </section>
{% endblock %}
```

Once your done, test how it looks (refer to {ref}`usingmynt` to see how).  Then commit your code, push to your fork of the repository, then open a pull request!  You can see what others have done within the `www/locations` directory as well.
