import re

import markdown
from django.conf import settings
from django.template.loader import render_to_string

from .base import MarkymarkExtension


class AutoLinkPostprocessor(markdown.postprocessors.Postprocessor):
    """
    Post processor to look for valid URIs and converts them to html links.
    """

    AUTOLINK_RE = re.compile(
        (
            r'(href="|src="|<a.*>)?'
            r'(?:(https?|ftps?|file|ssh|mms|svn(?:\+ssh)?|git|dict|nntp|irc|'
            r'rsync|smb|apt|telnet|s?news|sips?|skype|apt)://|(mailto:))'
            r'([-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&@#/%=~_()|])'
        )
    )

    def run(self, text):
        def re_callback(match):
            prefix = match.group(1) or ''

            # Skip already rendered links/real html links.
            if prefix in ('href="', 'src="') or prefix.startswith('<a'):
                return match.group()

            if match.group(3) == 'mailto:':
                name = match.group(4)
            else:
                name = match.group()

            return render_to_string(
                getattr(settings, 'MARKYMARK_TEMPLATE_AUTOLINK', 'markymark/autolink.html'),
                {'url': match.group(), 'name': name},
            ).strip()

        return self.AUTOLINK_RE.sub(re_callback, text)


class AutoLinkExtension(MarkymarkExtension):
    """
    Extension to insert html links for certain URIs.
    """

    postprocessors = (AutoLinkPostprocessor,)


def makeExtension(**kwargs):
    return AutoLinkExtension(**kwargs)
