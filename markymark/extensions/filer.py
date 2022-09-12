import re

import markdown
from django.conf import settings
from django.template.loader import render_to_string
from filer.models import File

from .base import MarkymarkExtension


class FilerPostprocessor(markdown.postprocessors.Postprocessor):
    """
    Filer markdown extension for django-filer to show files and images.
    """

    FILE_RE = re.compile(r'(\[file\:(?P<id>\d+)\])', re.IGNORECASE)

    def run(self, text):
        def re_callback(match):
            options = match.groupdict()
            try:
                obj = File.objects.get(pk=int(options['id']))
                return render_to_string(
                    getattr(settings, 'MARKYMARK_TEMPLATE_FILER', 'markymark/filer.html'),
                    {'file': obj.get_real_instance()},
                ).strip()

            except (KeyError, File.DoesNotExist):
                if settings.DEBUG:
                    raise

            return match.group(0).replace(match.group(1), '')

        return self.FILE_RE.sub(re_callback, text)


class FilerExtension(MarkymarkExtension):
    """
    Extension to look for file tags, replaces them with html tags.
    In case of image, the image is added as img-tag, files are added as download links.
    """

    postprocessors = (FilerPostprocessor,)

    class Media:
        js = ('markymark/extensions/filer.js',)
        css = {'all': ('markymark/extensions/filer.css',)}


def makeExtension(**kwargs):
    return FilerExtension(**kwargs)
