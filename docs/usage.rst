Usage
=====


Model Field
-----------

.. code-block:: python

    from django.db import models

    from markymark.fields import MarkdownField


    class Post(models.Model):
        content = MarkdownField()


Template filter
---------------

To display the rendered markdown in your template.

.. code-block:: HTML

    {% load markymark %}

    {{ obj.content|markdown }}


Running tests
-------------

To run the tests, you need to install the test requirements with pip:

.. code-block:: bash

    $ pip install -e .[tests]


Now you can run the tests from the root folder of the package:

.. code-block:: bash

    $ make tests
