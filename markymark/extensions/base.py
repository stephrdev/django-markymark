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

    def extendMarkdown(self, md):
        """
        Every extension requires a extendMarkdown method to tell the markdown
        renderer how use the extension.
        """
        md.registerExtension(self)

        for processor in self.preprocessors or []:
            md.preprocessors.register(processor(md), processor.__name__.lower(), 0)

        for pattern in self.inlinepatterns or []:
            md.inlinePatterns.register(pattern(md), pattern.__name__.lower(), 0)

        for processor in self.postprocessors or []:
            md.postprocessors.register(processor(md), processor.__name__.lower(), 0)
