---
orphan: true
---

# Using Mynt

```{attention}
As of December 2023, we're considering moving from mynt to [Hugo](https://gohugo.io/). If you want to help with this effort, drop a note in the `#project-tech-info` PyLadies Slack channel.
```

[mynt] is a simple static site generator written in Python.

When you've added or edited content in any way, you can check out your changes by running the website locally.  To do so:

1. Set up your machine following the {ref}`setupenv` instructions.

2. With the activated [virtualenv], make sure you're in the `www` directory, then run:

   ```console
   (env) $ mynt gen -f _site
   (env) $ mynt serve _site
   ```

3. Copy the IP address provided once mynt has completed building the site. (It will say something like `>> Serving at 127.0.0.1:8080`), then paste the IP address into the URL bar of a browser window and load it to view the site.

4. To view any changes you make to the site code, type `CTRL` + `c` (at the same time) in the terminal to stop the local server, then run the two `mynt` commands from Step 2 again and refresh the browser window.

```{tip}
If you wish to run the `mynt` server (aka `mynt serve _site`) on a different port, use the `-p` option:  `mynt serve _site -p 5050`.
```

The `mynt gen -f _site` "compiles" the Markdown files into the Jinja2 template files (and does some other linking magic for CSS, JavaScript, images, fonts, etc) and spits out the output into the `_site` directory.  This is actually what gets deployed (but is **not** committed to the repo!).

The `mynt serve _site` command runs a simple HTTP server for you to view local changes.

```{tip}
If you are having to stop the server, make your changes, run the two mynt commands many times, try the following:

1. Have two terminal windows/spaces open.
2. In one terminal window/space:
   1. Move to the `www` directory, and then run `mynt gen -f _site` (with your activated virtualenv) just once.
   2. Then run `mynt watch -f _site` - mynt will then watch for any changes saved to the file and re-run `mynt gen -f _site` for you.
3. In the other terminal window/space:
   1. Move into the `www/_site` directory.
   2. If running Python 2.x, run `python -m SimpleHTTPServer 8080` (or whatever port you'd like)
   3. If running Python 3.x - to be honest, not sure if mynt supports running on Python 3, but if it does - run `python -m http.server 8080`
4. Now whatever changes you make & save, you'll just have to refresh your browser.
```

[mynt]: http://mynt.uhnomoli.com/
[pyladies/pyladies]: https://github.com/pyladies/pyladies
[virtualenv]: http://simononsoftware.com/virtualenv-tutorial/
