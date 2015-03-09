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
