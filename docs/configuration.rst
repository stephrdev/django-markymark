Configuration
=============

Markymark uses settings to make the markdown field work in the django admin site.


Django Settings
---------------

.. py:data:: MARKYMARK_EXTENSIONS

A list with extra extensions for the markdown field.

Default extensions:

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        'markymark.extensions.autolink',
    ]


.. py:data:: MARKYMARK_FONTAWESOME_CSS

By default, the markdown editor uses FontAwesome to show some nice icons.
FontAwesome is vendored and shipped with this library. You can override the
path of the FontAwesome css file to use either the CDN version or something
completly different.

Default extensions:

.. code-block:: python

    MARKYMARK_FONTAWESOME_CSS = 'https://use.fontawesome.com/releases/v5.2.0/css/all.css'
