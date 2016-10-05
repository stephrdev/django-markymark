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


def test_markdownfield_widget_instance():
    field = MarkdownField()
    widget_instance = MarkdownTextarea(attrs={'rows': 30, 'autofocus': True})
    form_field = field.formfield(widget=widget_instance)
    assert isinstance(form_field, MarkdownFormField)
    assert isinstance(form_field.widget, MarkdownTextarea)
    assert form_field.widget.attrs['rows'] == 30
    assert form_field.widget.attrs['autofocus'] is True
