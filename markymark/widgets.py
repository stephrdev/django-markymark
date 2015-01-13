import floppyforms.__future__ as forms


class MarkdownTextarea(forms.Textarea):
    class Media:
        css = {'all': (
            'markdown/css/markdown-editor.css',
            'markdown/css/markdown-editor-adminfix.css',
            'markdown/css/plugins/filer-file.css',
        )}
        js = (
            'markdown/js/markdown.js',
            'markdown/js/markdown-editor.js',
            'markdown/js/markdown-init.js',
            'markdown/js/plugins/clean.js',
            'markdown/js/plugins/anylink-link.js',
            'markdown/js/plugins/filer-file.js',
        )

    def __init__(self, *args, **kwargs):
        super(MarkdownTextarea, self).__init__(*args, **kwargs)
        self.attrs['data-provide'] = 'init-markdown'
