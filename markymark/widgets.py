from django import forms

from markymark.utils import initialize_renderer


class MarkdownTextarea(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(MarkdownTextarea, self).__init__(*args, **kwargs)
        self.attrs['data-provide'] = 'markdown'

    def _media(self):
        media = forms.Media(
            css={'all': (
                'markdown/css/markdown-editor.css',
                'markdown/css/markdown-editor-adminfix.css',
            )},
            js=(
                'markdown/js/markdown.js',
                'markdown/js/markdown-editor.js'
            )
        )

        # Use official extension loading to initialize all extensions
        # and hook in extension-defined media files.
        renderer = initialize_renderer()

        for extension in renderer.registeredExtensions:
            if hasattr(extension, 'media'):
                media += extension.media
        return media

    media = property(_media)
