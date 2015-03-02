import re

import markdown
from django.template.loader import render_to_string

from markymark import conf
from markymark.extensions.base import MarkymarkExtension


AUTOLINK_RE = re.compile((
    r'(https?|ftps?|file|ssh|mms|svn(?:\+ssh)?|git|dict|nntp|irc|'
    r'rsync|smb|apt|mailto|telnet|s?news|sips?|skype|apt)'
    r'(://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&@#/%=~_()|])'
))


class AutoLinkPostprocessor(markdown.postprocessors.Postprocessor):

    def run(self, text):
        def re_callback(match):
            return render_to_string(
                conf.MARKYMARK_TEMPLATES['autolink'],
                {'url': match.group()}
            )
        return AUTOLINK_RE.sub(re_callback, text)


class AutoLinkExtension(MarkymarkExtension):
    def extendMarkdown(self, md, md_globals):
        super(AutoLinkExtension, self).extendMarkdown(md, md_globals)
        md.postprocessors.add('autolink', AutoLinkPostprocessor(md), '_end')


def makeExtension(**kwargs):
    return AutoLinkExtension(**kwargs)
