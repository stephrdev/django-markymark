Extensions
==========


Python Markdown
---------------

Regular extensions from `Python Markdown <https://pythonhosted.org/Markdown/extensions/index.html>`_
for extra markdown features, can be installed using module paths.

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        '..',
        'markdown.extensions.codehilite',
        'markdown.extensions.fenced_code',
    ]


Django-anylink
--------------

An extension for `django-anylink <https://github.com/moccu/django-anylink>`_ a generic linking module for Django.

The following needs to be added to the settings:

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        '..',
        'markymark.extensions:LinkExtension',
    ]

    MARKYMARK_JS = [
        '..',
        'markdown/js/plugins/anylink-link.js',
    ]

For this extension additional settings are required that can be found in the `django-anylink documentation <http://django-anylink.readthedocs.org/en/latest/configuration.html>`_


Django-filer
------------

An extension for `django-filer <https://github.com/stefanfoulis/django-filer>`_ a file and image management application for django.

The following needs to be added to the settings:

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        '..',
        'markymark.extensions:FilerFileExtension',
    ]

    MARKYMARK_CSS = [
        '..',
        'markdown/css/plugins/filer-file.css',
    ]

    MARKYMARK_JS = [
        '..',
        'markdown/js/plugins/filer-file.js',
    ]

For this extension additional settings are required that can be found in the `django-filer documentation <http://django-filer.readthedocs.org/en/latest/settings.html>`_



Autolink
--------

An extension to automatically create anchor tags from urls inspired by `Github Flavored Markdown <https://help.github.com/articles/github-flavored-markdown/>`_.

The following needs to be added to the settings:

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        '..',
        'markymark.extensions:AutoLinkExtension',
    ]

.. note::
    If you combine the ``AutoLinkExtension`` together with ``LinkExtension``, then make sure that the ``AutoLinkExtension`` is listed before in ``MARKYMARK_EXTENSIONS``.


Example input/output:

.. code-block:: HTML

    http://www.example.com will turn into <a href="http://www.example.com">http://www.example.com</a>
