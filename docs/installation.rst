Installation
============

* Install with pip::

    pip install django-markymark


* Your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        # ...
        'markymark',
    )


Configuration for Django-CMS
----------------------------

If you plan to use django-markymark in a Django-CMS project, you should change
the following two settings to make sure there are no iconlibrary problems:

.. code-block:: python

    MARKYMARK_FONTAWESOME_CSS = None
    MARKYMARK_ICONLIBRARY = 'fa4'
