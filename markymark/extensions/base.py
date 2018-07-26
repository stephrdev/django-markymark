import markdown
from django.forms.widgets import MediaDefiningClass


class MarkymarkExtension(markdown.Extension, metaclass=MediaDefiningClass):
    """
    Base class for all markymark extensions.

    Actually its just a markdown.Extension class with some media attached.
    """
    preprocessors = None
    inlinepatterns = None
    postprocessors = None

    def extendMarkdown(self, md, md_globals):
        """
        Every extension requires a extendMarkdown method to tell the markdown
        renderer how use the extension.
        """
        md.registerExtension(self)

        for processor in (self.preprocessors or []):
            md.preprocessors.add(processor.__name__.lower(), processor(md), '_end')

        for pattern in (self.inlinepatterns or []):
            md.inlinePatterns.add(pattern.__name__.lower(), pattern(md), '_end')

        for processor in (self.postprocessors or []):
            md.postprocessors.add(processor.__name__.lower(), processor(md), '_end')
