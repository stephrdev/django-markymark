from django.conf import settings


MARKYMARK_EXTENSIONS = getattr(settings, 'MARKYMARK_EXTENSIONS', [
    'markymark.extensions:LinkExtension',
    'markymark.extensions:FilerFileExtension',
    'markymark.extensions:AutoLinkExtension',
])


MARKYMARK_CSS = getattr(settings, 'MARKYMARK_CSS', [
    'markdown/css/markdown-editor.css',
    'markdown/css/markdown-editor-adminfix.css',
    'markdown/css/plugins/filer-file.css',
])


MARKYMARK_JS = getattr(settings, 'MARKYMARK_JS', [
    'markdown/js/markdown-init.js',
    'markdown/js/markdown.js',
    'markdown/js/markdown-editor.js',
    'markdown/js/plugins/clean.js',
    'markdown/js/plugins/anylink-link.js',
    'markdown/js/plugins/filer-file.js',
])
