---
orphan: true
---

# Add a Resource

If you want to write your own resources, like Barbara's [beginner workshop notes] or Juliana's [Mac setup], in addition to {ref}`the headers for blogging <blogheaders>`, you will need to add more items in the header portion, like so:

```yaml
---
layout: post.html
title: "Your title here"
tags: [list, of relevant, tags]
author: Name, or blank/none
author_link: Twitter/Blog/etc or blank/none
category: [resources, pyladies]
---
```

Notice that `pyladies` and `resources` are required in for `category`.

Once done, save it in `www/_posts/` with the date and title in the name of the file, like so: `2013-04-21-lynns-awesome-resource.md`.  The title portion of the filename, `lynns-awesome-resource`, will end up being the URL of the post, e.g. `pyladies.com/blog/lynns-awesome-resource`.

[beginner workshop notes]: http://www.pyladies.com/blog/intro-python-april-6-recap/
[mac setup]: http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/
