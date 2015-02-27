import markdown
from django.forms.widgets import MediaDefiningClass
from django.utils import six


class MarkymarkExtension(six.with_metaclass(MediaDefiningClass), markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
