from django import forms
from django.db import models

from .widgets import MarkdownTextarea


class MarkdownFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        widget = kwargs.get('widget', MarkdownTextarea)
        try:
            if not issubclass(widget, MarkdownTextarea):
                widget = MarkdownTextarea
        except TypeError:
            if not isinstance(widget, MarkdownTextarea):
                widget = MarkdownTextarea
        kwargs['widget'] = widget
        super(MarkdownFormField, self).__init__(*args, **kwargs)


class MarkdownField(models.TextField):
    def formfield(self, form_class=MarkdownFormField, **kwargs):
        return super(MarkdownField, self).formfield(
            form_class=form_class, **kwargs)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules(
        rules=[((MarkdownField,), [], {})],
        patterns=['^markymark\.fields']
    )
except ImportError:
    pass
