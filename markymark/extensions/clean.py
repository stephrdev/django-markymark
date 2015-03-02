from markymark.extensions.base import MarkymarkExtension


class CleanExtension(MarkymarkExtension):
    class Media:
        js = ('markdown/js/plugins/clean.js',)


def makeExtension(**kwargs):
    return CleanExtension(**kwargs)
