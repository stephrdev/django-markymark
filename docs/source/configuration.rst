Configuration
=============

Markymark uses settings to make the markdown field work in the django admin site.


Django Settings
---------------

.. py:data:: MARKYMARK_EXTENSIONS

A list with extra extensions for the markdown field.

Default can be empty.

.. code-block:: python

    MARKYMARK_EXTENSIONS = [
        'markdown.extensions.codehilite',
    ]


.. py:data:: MARKYMARK_CSS

A list of css files needed for styling of the markdown field and extensions.

default should be:

.. code-block:: python

    MARKYMARK_CSS = [
        'markdown/css/markdown-editor.css',
        'markdown/css/markdown-editor-adminfix.css',
    ]


.. py:data:: MARKYMARK_JS

A list of js files needed for the default widget and extensions.

Default should be:

.. code-block:: python

    MARKYMARK_JS = [
        'markdown/js/markdown-init.js',
        'markdown/js/markdown.js',
        'markdown/js/markdown-editor.js',
        'markdown/js/plugins/clean.js',
    ]
