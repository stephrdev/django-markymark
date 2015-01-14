from markymark.fields import MarkdownFormField
from markymark.widgets import MarkdownTextarea


def test_markdownfield_formfield():
    field = MarkdownFormField()
    assert isinstance(field, MarkdownFormField)
    assert isinstance(field.widget, MarkdownTextarea)
