from django.conf import settings


MARKYMARK_EXTENSIONS = getattr(settings, 'MARKYMARK_EXTENSIONS', [
    'markymark.extensions.autolink',
])


MARKYMARK_CSS = getattr(settings, 'MARKYMARK_CSS', [
    'markdown/css/markdown-editor.css',
    'markdown/css/markdown-editor-adminfix.css',
])


MARKYMARK_JS = getattr(settings, 'MARKYMARK_JS', [
    'markdown/js/markdown-init.js',
    'markdown/js/markdown.js',
    'markdown/js/markdown-editor.js',
    'markdown/js/plugins/clean.js'
])
