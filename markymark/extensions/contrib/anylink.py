from __future__ import absolute_import

import re

from anylink.models import AnyLink
from django.conf import settings
from django.template.loader import render_to_string
import markdown


LINK_RE = re.compile(r'(\[link\:(?P<id>\d+)\])', re.IGNORECASE)


class LinkExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('link', LinkPostprocessor(md), '_end')


class LinkPostprocessor(markdown.postprocessors.Postprocessor):
    def run(self, text):
        def re_callback(match):

            options = match.groupdict()
            try:
                link = AnyLink.objects.get(pk=int(options['id']))
                return match.group(0).replace(
                    match.group(1),
                    render_to_string('markdown/link.html', {'link': link})
                )

            except (KeyError, AnyLink.DoesNotExist):
                if settings.DEBUG:
                    raise

        return LINK_RE.sub(re_callback, text)


def makeExtension(**kwargs):
    return LinkExtension(**kwargs)
