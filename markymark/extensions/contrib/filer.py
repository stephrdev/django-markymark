from __future__ import absolute_import

import re

from django.conf import settings
from django.template.loader import render_to_string
from filer.models.filemodels import File
import markdown


FILE_RE = re.compile(r'(\[file\:(?P<id>\d+)\])', re.IGNORECASE)


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


def makeExtension(**kwargs):
    return FilerFileExtension(**kwargs)
