Extensions
==========


Python Markdown
---------------

Regular extensions from `Python Markdown <https://python-markdown.github.io/extensions/>`_
for extra markdown features, can be used with markymark.

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        '..',
        'markdown.extensions.codehilite',
        'markdown.extensions.fenced_code',
        'markdown.extensions.tables',
    ]


Django-anylink
--------------

An extension for `django-anylink <https://github.com/moccu/django-anylink>`_ a generic linking module for Django.

The following needs to be added to the settings:

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        '..',
        'markymark.extensions.anylink',
    ]


This extension has extra dependencies that need to be installed:

.. code-block:: bash

    $ pip install django-markymark[anylink]

.. note::

    For this extension additional settings are required that can be found in the `django-anylink documentation <https://django-anylink.readthedocs.io/en/latest/configuration.html>`_

.. warning::

    The JavaScript plugin overwrites the functionality of the "Link" button
    of the markdown editor with it's own implementation.
    Please be aware of that.


Django-filer
------------

An extension for `django-filer <https://github.com/divio/django-filer>`_ a file and image management application for django.

The following needs to be added to the settings:

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        '..',
        'markymark.extensions.filer',
    ]


This extension has extra dependencies that need to be installed:

.. code-block:: bash

    $ pip install django-markymark[filer]

.. note::

    For this extension additional settings are required that can be found in the `django-filer documentation <https://django-filer.readthedocs.io/en/latest/settings.html>`_

.. warning::

    The JavaScript plugin overwrites the functionality of the "Link" button
    of the markdown editor with it's own implementation.
    Please be aware of that.


Autolink
--------

An extension to automatically create anchor tags from urls inspired by `Github Flavored Markdown <https://help.github.com/articles/github-flavored-markdown/>`_.

The following needs to be added to the settings:

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        '..',
        'markymark.extensions.autolink',
    ]

Example input/output:

.. code-block:: HTML

    http://www.example.com will turn into <a href="http://www.example.com">http://www.example.com</a>
