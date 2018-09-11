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

.. code-block:: python

    # Override default setting.
    MARKYMARK_FONTAWESOME_CSS = 'https://use.fontawesome.com/releases/v5.2.0/css/all.css'


.. py:data:: MARKYMARK_ICONLIBRARY

By default, the markdown editor uses Font Awesome 5 compatible css classes for icons.
In addition, you can change the used icon library to Font Awesome 4.

To change the icon classes to Fa4, use this setting:

.. code-block:: python

    MARKYMARK_ICONLIBRARY = 'fa4'
