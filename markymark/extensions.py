import markdown
import re

from django.conf import settings
from django.template.loader import render_to_string
from filer.models.filemodels import File


FILE_RE = re.compile(r'(\[file\:(?P<id>\d+)\])', re.IGNORECASE)
LINK_RE = re.compile(r'(\[link\:(?P<id>\d+)\])', re.IGNORECASE)


class FilerFileExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('filerfile', FilerFilePostprocessor(md), '_end')


class FilerFilePostprocessor(markdown.postprocessors.Postprocessor):
    """
    Image markdown extension for django-filer + easy_thumbnails

    Usage:

      [image:id type:full pos:left|right]

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
