import markdown

from django.utils.encoding import force_text

from .extensions import FilerFileExtension, LinkExtension


def render_markdown(value, extensions=''):
    extensions = [e.strip() for e in extensions.split(',') if e]

    extensions.append(LinkExtension())
    extensions.append(FilerFileExtension())
    extensions.append('markdown.extensions.codehilite')

    return markdown.markdown(
        force_text(value),
        extensions)
