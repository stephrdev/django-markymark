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

    {% load static markup %}

    {{ obj.content|markdown }}
