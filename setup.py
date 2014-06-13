#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Lynn Root 2014

from __future__ import print_function
from setuptools import setup
import io


def read(*filenames, **kwargs):
    # adapted from http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md', 'CHANGES.md')

setup(name='pyladies',
      version='2.0.2',
      author=u'Lynn Root',
      author_email='lynn@pyladies.com',
      license="Creative Commons Attribution-ShareAlike 3.0 Unported",
      platforms='any',
      url='http://www.pyladies.com',
      description='Everything you need to start your own PyLadies location',
      long_description=long_description,
      install_requires=['Sphinx', 'sphinx-rtd-theme'],
      packages=['pyladies'],
      entry_points={
          'console_scripts': [
              'pyladies = pyladies.main:main'
          ]
      },
      include_package_data=True
      )
