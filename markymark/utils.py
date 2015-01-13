import markdown

from django.utils.encoding import force_text

from .extensions import FilerFileExtension, LinkExtension


def render_markdown(value, extensions=''):
    extensions = [e.strip() for e in extensions.split(',') if e]

    extensions.append(LinkExtension())
    extensions.append(FilerFileExtension())

    if extensions and extensions[0] == 'safe':
        extensions = extensions[1:]
        return markdown.markdown(
            force_text(value),
            extensions,
            safe_mode=True,
            enable_attributes=False
        )

    return markdown.markdown(
        force_text(value),
        extensions,
        safe_mode=False
    )
