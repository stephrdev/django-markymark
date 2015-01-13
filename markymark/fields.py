from django import forms

from .widgets import MarkdownTextarea


class MarkdownFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = MarkdownTextarea
        super(MarkdownFormField, self).__init__(*args, **kwargs)
