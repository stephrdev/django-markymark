from django import forms
from django.conf import settings

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

        if getattr(settings, 'MARKYMARK_ICONLIBRARY', None):
            self.attrs['data-iconlibrary'] = settings.MARKYMARK_ICONLIBRARY

    @property
    def media(self):
        """
        Returns a forms.Media instance with the basic editor media and media
        from all registered extensions.
        """
        css = ['markymark/css/markdown-editor.css']
        iconlibrary_css = getattr(
            settings, 'MARKYMARK_FONTAWESOME_CSS', 'markymark/fontawesome/fontawesome.min.css'
        )
        if iconlibrary_css:
            css.append(iconlibrary_css)

        media = forms.Media(css={'all': css}, js=('markymark/js/markdown-editor.js',))

        # Use official extension loading to initialize all extensions
        # and hook in extension-defined media files.
        renderer = initialize_renderer()

        for extension in renderer.registeredExtensions:
            if hasattr(extension, 'media'):
                media += extension.media
        return media
