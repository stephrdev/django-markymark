from __future__ import absolute_import

import re

from anylink.models import AnyLink
from django.conf import settings
from django.template.loader import render_to_string
import markdown

from markymark import conf
from markymark.extensions.base import MarkymarkExtension


LINK_RE = re.compile(r'(\[link\:(?P<id>\d+)\])', re.IGNORECASE)


class AnyLinkExtension(MarkymarkExtension):
    class Media:
        js = (
            'markdown/js/plugins/anylink-link.js',
        )

    def extendMarkdown(self, md, md_globals):
        super(AnyLinkExtension, self).extendMarkdown(md, md_globals)
        md.postprocessors.add('anylink', AnyLinkPostprocessor(md), '_end')


class AnyLinkPostprocessor(markdown.postprocessors.Postprocessor):
    def run(self, text):
        def re_callback(match):

            options = match.groupdict()
            try:
                link = AnyLink.objects.get(pk=int(options['id']))
                return match.group(0).replace(
                    match.group(1),
                    render_to_string(conf.MARKYMARK_TEMPLATES['anylink'], {'link': link})
                )

            except (KeyError, AnyLink.DoesNotExist):
                if settings.DEBUG:
                    raise

        return LINK_RE.sub(re_callback, text)


def makeExtension(**kwargs):
    return AnyLinkExtension(**kwargs)
