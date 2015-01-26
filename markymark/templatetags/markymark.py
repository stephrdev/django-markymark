from __future__ import absolute_import

from django import template
from django.utils.safestring import mark_safe

from markymark.utils import render_markdown


register = template.Library()


@register.filter(is_safe=True, name='markdown')
def markdown_filter(value, arg=''):
    return mark_safe(render_markdown(value, arg))
