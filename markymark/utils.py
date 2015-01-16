import markdown

from django.conf import settings
from django.utils.encoding import force_text


def render_markdown(value, extensions=''):
    extensions = [e.strip() for e in extensions.split(',') if e]
    [extensions.append(module) for module in settings.MARKYMARK_EXTENSIONS]
    return markdown.markdown(force_text(value), extensions)
