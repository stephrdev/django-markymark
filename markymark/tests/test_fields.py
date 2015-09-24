from markymark.fields import MarkdownField, MarkdownFormField
from markymark.widgets import MarkdownTextarea


class CustomMarkdownTextarea(MarkdownTextarea):
    pass


def test_markdownfield_formfield():
    field = MarkdownField()
    form_field = field.formfield()
    assert isinstance(form_field, MarkdownFormField)
    assert isinstance(form_field.widget, MarkdownTextarea)


def test_markdownfield_formfield_no_override():
    field = MarkdownField()
    form_field = field.formfield(widget=CustomMarkdownTextarea)
    assert isinstance(form_field, MarkdownFormField)
    assert isinstance(form_field.widget, CustomMarkdownTextarea)
