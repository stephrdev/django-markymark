from django import forms
from django.db import models

from .widgets import MarkdownTextarea


class MarkdownFormField(forms.CharField):
    """
    Form field to configure the markdown textarea widget if not already set.
    """

    def __init__(self, *args, **kwargs):
        """
        Update the kwargs to set the markdown widget.
        Special note: the provided widget should be a subclass of MarkdownTextarea,
        if not the provided widget will be ignored.
        """
        widget = kwargs.get('widget', MarkdownTextarea)
        try:
            if not issubclass(widget, MarkdownTextarea):
                widget = MarkdownTextarea
        except TypeError:
            if not isinstance(widget, MarkdownTextarea):
                widget = MarkdownTextarea

        kwargs['widget'] = widget
        super().__init__(*args, **kwargs)


class MarkdownField(models.TextField):
    """
    Model field based on TextField with enabled markdown form field.
    """

    def formfield(self, form_class=MarkdownFormField, **kwargs):
        return super().formfield(form_class=form_class, **kwargs)
