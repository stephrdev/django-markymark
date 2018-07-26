from django import forms

from markymark.fields import MarkdownFormField


class MarkdownForm(forms.Form):
    content = MarkdownFormField()
