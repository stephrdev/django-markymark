django-markymark
================

.. image:: https://img.shields.io/pypi/v/django-markymark.svg
   :target: https://pypi.org/project/django-markymark/
   :alt: Latest Version

.. image:: https://codecov.io/gh/moccu/django-markymark/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/moccu/django-markymark
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-markymark/badge/?version=latest
   :target: https://django-markymark.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/moccu/django-markymark.svg?branch=master
   :target: https://travis-ci.org/moccu/django-markymark


*django-markymark* provides helpers and tools to integrate markdown into Django.


Features
--------

* Django form fields to integrate the bootstrap markdown editor (without the dependency on bootstrap)
* `django-filer <https://github.com/divio/django-filer>`_ integration
* `django-anylink <https://github.com/moccu/django-anylink>`_ integration


Requirements
------------

django-markymark supports Python 3 only and requires at least Django 1.11.


Prepare for development
-----------------------

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6
    $ pipenv shell
    $ pip install -e .


Now you're ready to start the example project to experiment with markymark.

.. code-block:: shell

    $ pipenv run python examples/manage.py runserver


Resources
---------

* `Documentation <https://django-markymark.readthedocs.org/>`_
* `Bug Tracker <https://github.com/moccu/django-markymark/issues>`_
* `Code <https://github.com/moccu/django-markymark/>`_
