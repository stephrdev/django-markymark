import markdown
from django.utils.encoding import force_text

from markymark import conf


def render_markdown(value, extensions=''):
    extensions = [e.strip() for e in extensions.split(',') if e]
    [extensions.append(module) for module in conf.MARKYMARK_EXTENSIONS]
    return markdown.markdown(force_text(value), extensions)
