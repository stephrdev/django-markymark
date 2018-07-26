from markymark.extensions.base import MarkymarkExtension


class CleanExtension(MarkymarkExtension):
    """
    Extension to enable the cleanup plugin for the markdown editor.
    """

    class Media:
        js = ('markymark/extensions/clean.js',)


def makeExtension(**kwargs):
    return CleanExtension(**kwargs)
