import re

import markdown
from django.conf import settings
from django.template.loader import render_to_string
from filer.models.filemodels import File


FILE_RE = re.compile(r'(\[file\:(?P<id>\d+)\])', re.IGNORECASE)
LINK_RE = re.compile(r'(\[link\:(?P<id>\d+)\])', re.IGNORECASE)
AUTOLINK_RE = re.compile((
    r'(https?|ftps?|file|ssh|mms|svn(?:\+ssh)?|git|dict|nntp|irc|'
    r'rsync|smb|apt|mailto|telnet|s?news|sips?|skype|apt)'
    r'(://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&@#/%=~_()|])'
))


class FilerFileExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('filerfile', FilerFilePostprocessor(md), '_end')


class FilerFilePostprocessor(markdown.postprocessors.Postprocessor):
    """
    File markdown extension for django-filer for files and images.

    Usage:

      [file:id type:full pos:left|right]

    Position `pos` is optional.
    """

    def run(self, text):
        def re_callback(match):
            options = match.groupdict()
            try:
                file = File.objects.get(pk=int(options['id']))
                return render_to_string('markdown/file.html', {
                    'file': file.get_real_instance(),
                })

            except File.DoesNotExist:
                if settings.DEBUG:
                    raise

            return match.group(0).replace(match.group(1), '')

        return FILE_RE.sub(re_callback, text)


class LinkExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('link', LinkPostprocessor(md), '_end')


class LinkPostprocessor(markdown.postprocessors.Postprocessor):
    def run(self, text):
        def re_callback(match):
            from anylink.models import AnyLink

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


class AutoLinkPostprocessor(markdown.postprocessors.Postprocessor):

    def run(self, text):
        def re_callback(match):
            return render_to_string('markdown/autolink.html', {'url': match.group()})
        return AUTOLINK_RE.sub(re_callback, text)


class AutoLinkExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('autolink', AutoLinkPostprocessor(md), '_end')
