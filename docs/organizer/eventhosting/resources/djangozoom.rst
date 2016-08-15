:orphan:

DjangoZoom Beginner Walkthrough
===============================

This is a walkthrough of deploying https://github.com/pyladies/djangotutorial

Deploying from your repo
------------------------

Log into djangozoom.com.

Go to My Projects. Click [Add a new project »]

Under New Project > Repo url, enter something like git@github.com:pyladies/djangotutorial.git

Click [Checkout code & continue]

Check that your configuration matches your project, making changes if needed. (For https://github.com/pyladies/djangotutorial, the default values work as-is.)

Scroll all the way down. Click [Deploy project]

It should say "Working..." Wait for it to finish.  It should change to "Job succeeded, deployed at http://p00000333.djangozoom.net".

(Note: if it fails, check your configuration. Ask for help in #djangozoom - they're nice)

Open whatever URL you were given in a new browser tab.  Congrats, your project is now live on the web!

Domain names
------------

To set your domain name, click [Custom Hostnames] and follow the instructions.

Accessing the Django admin
--------------------------

Finally, to access your site's Django admin, click [Create Superuser].  Enter a password that you'll be able to remember and click [Create Superuser Account].

Then go to your site's Django admin (something like http://p00000333.djangozoom.net/admin/) and log in with your superuser name/password.
