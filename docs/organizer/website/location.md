---
orphan: true
---

# Adding your Location

Nearly all locations are listed on our [locations] page.  To get listed on there, **you** must put it there. :-)

### Process

1. Setup your machine following the {ref}`setupenv` instructions above.
2. Within the `www` directory, make an edit to the `config.yml` file.  More about the `config.yml` file structure {ref}`below <config>`.
3. **Optional:** If you don't have a website setup yet, you can make a simple static page within `www/locations/`.  Read {ref}`simplepage` for more information.
4. Test your changes by running `mynt gen -f _site && mynt serve _site` (**within** the `www` directory).
5. Commit the code locally, and push it up to **your** fork.
6. Make a pull request against the `pyladies/pyladies` repository.

(config)=

### config.yml File

The [config.yml] file contains most (if not all) of the configuration for the main PyLadies website.

#### Editing

To make your location show up on our [locations] page, create an entry under `chapters`.

```{danger} Important!
Please - maintain alphabetical order of the `chapters` listing!!
```

Here are the available configuration items you can set, and what they mean/show up as on the [locations] page.

A complete example:

```yaml
- name: Austin, TX
  meetup_id: 5947662
  website: atx.pyladies.com
  image: pyladies_atx.jpeg
  email: atx@pyladies.com
  twitter: pyladiesATX
  meetup: pyladies-atx
  location:
      latitude: 30.2711286
      longitude: -97.7436995
```

Make sure a tick, `-` precedes the `name:` attribute (in `yaml` syntax, it symbolizes another item in a list).

It shows up on the [locations] page as its own little "card":

```{image} ../../_static/images/location_config/complete.png
:align: center
:alt: Complete Example
:width: 200px
```

(attrs)=

#### Attributes

```{eval-rst}
.. option:: name

    **required** The ``name`` attribute sets the name to show up on the [locations] page.  You can as verbose or minimal as you'd like:

    .. image:: ../../_static/images/location_config/name.png
        :alt: Config: name
        :width: 200px
        :align: center


```

```{eval-rst}
.. option:: meetup_id

    **optional** The ``meetup_id`` actually corresponds to the Meetup Widget on the website.  The code for the Meetup Widget can be found `here <https://github.com/pyladies/pyladies/blob/master/www/_assets/js/meetup_widget.js>`_.

    .. image:: ../../_static/images/location_config/upcoming_meetups.png
        :alt: Config: meetup_id
        :width: 300px
        :align: center
        :target: https://github.com/pyladies/pyladies/blob/master/www/_assets/js/meetup_widget.js


```

```{eval-rst}
.. option:: website

    **optional** The ``website`` attribute is the absolute URL for the location's :doc:`website <local>`, or the relative URL for your location's :ref:`page <simplepage>` (e.g. ``atx`` for ``pyladies.com/locations/atx``).

    .. note::

        If it is an absolute URL - e.g. it is **not** relative to the pyladies.com domain (e.g. ``pyladies.com/locations/atx``) but is a subdomain (e.g. ``atx.pyladies.com``), the ``external_website`` attribute **needs** to be set to ``True``.

    .. image:: ../../_static/images/location_config/website.png
        :alt: Config: website
        :width: 200px
        :align: center
```

```{eval-rst}
.. option:: external_website

    **required if location has a subdomain** A boolean flag (if not set, will default to ``False``) for when the location has a subdomain.


```

```{eval-rst}
.. option:: image

    **required** The ``image`` attribute is the filename of the location's image that should be placed in the ``www/_assets/images/`` directory.  You can use a standard one that's already in the repository, or adapt the logo to your location (see :ref:`logos`).

    .. image:: ../../_static/images/location_config/image.png
        :alt: Config: image
        :width: 200px
        :align: center

```

```{eval-rst}
.. option:: email

    **required** The ``email`` attribute is the location's email address.

    .. image:: ../../_static/images/location_config/email.png
        :alt: Config: email
        :width: 200px
        :align: center

```

```{eval-rst}
.. option:: twitter
```

```{eval-rst}
.. option:: github
```

```{eval-rst}
.. option:: facebook
```

```{eval-rst}
.. option:: google_plus

    **optional** The ``twitter``, ``facebook``, ``google_plus``, and ``github`` attributes are links to the location's handle/account.  You may set as many as you'd like, or none.  If your group uses other social media accounts that you want to publish, please read :ref:`addingnewlinktypes`.

    .. image:: ../../_static/images/location_config/twitter.png
        :alt: Config: twitter
        :width: 200px
        :align: center

```

```{eval-rst}
.. option:: meetup

    **optional** The ``meetup`` is the Meetup group's URL name - the string that comes after ``www.meetup.com/``.  If your group uses a different service than Meetup.com for event publishing (other than your own location's website), please read :ref:`addingnewlinktypes`.

    .. image:: ../../_static/images/location_config/meetup.png
        :alt: Config: meetup
        :width: 200px
        :align: center

```

```{eval-rst}
.. option:: location

    **required** The ``location`` attribute is a map of ``latitude`` and ``longitude``.  If this is set, it will add a pinpoint to the map at the top of the page.  It will automatically pull in all the information, too.

    .. image:: ../../_static/images/location_config/coords.png
        :alt: Config: location
        :width: 400px
        :align: center
```

[config.yml]: https://github.com/pyladies/pyladies/blob/master/www/config.yml
[locations]: http://www.pyladies.com/locations
