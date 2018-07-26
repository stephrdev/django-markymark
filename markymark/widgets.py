from django import forms

from markymark.renderer import initialize_renderer


class MarkdownTextarea(forms.Textarea):
    """
    Extended forms Textarea which enables the javascript markdown editor.
    """

    def __init__(self, *args, **kwargs):
        """
        Sets the required data attributes to enable the markdown editor.
        """
        super().__init__(*args, **kwargs)
        self.attrs['data-provide'] = 'markdown'

    def _media(self):
        """
        Returns a forms.Media instance with the basic editor media and media
        from all registered extensions.
        """
        media = forms.Media(
            css={
                'all': (
                    'markymark/css/markdown-editor.css',
                    'https://use.fontawesome.com/releases/v5.2.0/css/all.css',
                )
            },
            js=('markymark/js/markdown-editor.js',)
        )

        # Use official extension loading to initialize all extensions
        # and hook in extension-defined media files.
        renderer = initialize_renderer()

        for extension in renderer.registeredExtensions:
            if hasattr(extension, 'media'):
                media += extension.media
        return media

    media = property(_media)
