import markdown
from django.conf import settings
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe


DEFAULT_MARKYMARK_EXTENSIONS = [
    'markymark.extensions.autolink',
]


def initialize_renderer(extensions=None):
    """
    Initializes the renderer by setting up the extensions (taking a comma separated
    string or iterable of extensions). These extensions are added alongside with the
    configured always-on extensions.

    Returns a markdown renderer instance.
    """
    if extensions is None:
        extensions = []

    if isinstance(extensions, str):
        extensions = [extension.strip() for extension in extensions.split(',')]

    for extension in getattr(settings, 'MARKYMARK_EXTENSIONS', DEFAULT_MARKYMARK_EXTENSIONS):
        extensions.append(extension)

    return markdown.Markdown(extensions=extensions)


def render_markdown(value, extensions=None):
    """
    Takes a text and a optional list of extensions and returns the rendered markdown text.

    The result is marked safe.
    """
    return mark_safe(initialize_renderer(extensions).convert(force_str(value)))
