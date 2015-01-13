from markymark.fields import MarkdownFormField
from markymark.widgets import MarkdownTextarea


def test_markdownfield_formfield():
    field = MarkdownFormField()
    form_field = field.formfield()
    assert isinstance(form_field, MarkdownFormField)
    assert isinstance(form_field.widget, MarkdownTextarea)
