import re

import markdown
from anylink.models import AnyLink
from django.conf import settings
from django.template.loader import render_to_string

from .base import MarkymarkExtension


class AnyLinkPostprocessor(markdown.postprocessors.Postprocessor):
    """
    Post processor to look for anylink link tags, replaces these tags with html links.
    """

    LINK_RE = re.compile(r'(\[link\:(?P<id>\d+)\])', re.IGNORECASE)

    def run(self, text):
        def re_callback(match):
            options = match.groupdict()
            try:
                link = AnyLink.objects.get(pk=int(options['id']))
                return render_to_string(
                    getattr(settings, 'MARKYMARK_TEMPLATE_ANYLINK', 'markymark/anylink.html'),
                    {'link': link},
                ).strip()

            except (KeyError, AnyLink.DoesNotExist):
                if settings.DEBUG:
                    raise

            return match.group(0).replace(match.group(1), '')

        return self.LINK_RE.sub(re_callback, text)


class AnyLinkExtension(MarkymarkExtension):
    """
    Extension to insert django-anylink links into a markdown document.
    """

    postprocessors = (AnyLinkPostprocessor,)

    class Media:
        js = ('markymark/extensions/anylink.js',)


def makeExtension(**kwargs):
    return AnyLinkExtension(**kwargs)
