from django import template

from ..renderer import render_markdown


register = template.Library()


@register.filter(is_safe=True, name='markdown')
def markdown_filter(value, extensions=None):
    """
    Template which converts a provided value using markdown to html.
    Accepts additional extensions when rendering with markdown.
    """
    return render_markdown(value, extensions)
