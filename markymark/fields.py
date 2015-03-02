from django import forms
from django.db import models

from .widgets import MarkdownTextarea


class MarkdownFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = MarkdownTextarea
        super(MarkdownFormField, self).__init__(*args, **kwargs)


class MarkdownField(models.TextField):
    def formfield(self, form_class=MarkdownFormField, **kwargs):
        return super(MarkdownField, self).formfield(
            form_class=form_class, **kwargs)
