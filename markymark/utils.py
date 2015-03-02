import markdown
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils import six

from markymark import conf
from markymark.extensions.base import MarkymarkExtension


class MarkymarkRenderer(markdown.Markdown):
    def registerExtensions(self, extensions, configs):
        """
        We are overwriting the default behavior of `markdown.Markdown`
        to provide some extensible plugin system and avoid failing
        because of stupid sublcass validation.

        `markdown` originally validates that instances that get passed to
        `registerExtension` are actual instances of `markdown.Extension`
        and if we're putting `MarkymarkExtension` in between this fails.
        """
        for ext in extensions:
            if isinstance(ext, six.string_types):
                ext = self.build_extension(ext, configs.get(ext, {}))
            if isinstance(ext, (markdown.Extension, MarkymarkExtension)):
                ext.extendMarkdown(self, globals())
            else:
                raise TypeError(
                    'Extension "%s.%s" must be of type: '
                    '"markdown.Extension" or "markymark.extensions.MarkymarkExtension"'
                    % (ext.__class__.__module__, ext.__class__.__name__))

        return self


def initialize_renderer(extensions=''):
    extensions = [e.strip() for e in extensions.split(',') if e]
    [extensions.append(module) for module in conf.MARKYMARK_EXTENSIONS]
    return MarkymarkRenderer(extensions=extensions)


def render_markdown(value, extensions=''):
    return mark_safe(initialize_renderer(extensions).convert(force_text(value)))
