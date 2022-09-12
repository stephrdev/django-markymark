django-markymark
================

.. image:: https://img.shields.io/pypi/v/django-markymark.svg
   :target: https://pypi.org/project/django-markymark/
   :alt: Latest Version

.. image:: https://github.com/stephrdev/django-markymark/workflows/Test/badge.svg?branch=master
   :target: https://github.com/stephrdev/django-markymark/actions?workflow=Test
   :alt: CI Status

.. image:: https://codecov.io/gh/stephrdev/django-markymark/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/stephrdev/django-markymark
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-markymark/badge/?version=latest
   :target: https://django-markymark.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status


*django-markymark* provides helpers and tools to integrate markdown into Django.


Features
--------

* Django form fields to integrate the bootstrap markdown editor (without the dependency on bootstrap)
* `django-filer <https://github.com/divio/django-filer>`_ integration
* `django-anylink <https://github.com/moccu/django-anylink>`_ integration


Requirements
------------

django-markymark supports Python 3 only and requires at least Django 3.2


Prepare for development
-----------------------

A Python 3 interpreter is required in addition to Poetry.

.. code-block:: shell

    $ poetry install


Now you're ready to start the example project to experiment with markymark.

.. code-block:: shell

    $ poetry run python examples/manage.py runserver


Resources
---------

* `Documentation <https://django-markymark.readthedocs.org/>`_
* `Bug Tracker <https://github.com/stephrdev/django-markymark/issues>`_
* `Code <https://github.com/stephrdev/django-markymark/>`_
