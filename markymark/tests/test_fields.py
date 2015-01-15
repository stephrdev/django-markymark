from markymark.fields import MarkdownField, MarkdownFormField
from markymark.widgets import MarkdownTextarea


def test_markdownfield_formfield():
    field = MarkdownField()
    form_field = field.formfield()
    assert isinstance(form_field, MarkdownFormField)
    assert isinstance(form_field.widget, MarkdownTextarea)
