import os
import tempfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MIDDLEWARE_CLASSES = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'floppyforms',
    'anylink',
    'easy_thumbnails',
    'filer',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'markymark', 'templates'),
)

STATIC_URL = '/'
MEDIA_URL = '/'

ANYLINK_EXTENSIONS = (
    'anylink.extensions.ExternalLink',
)

MEDIA_ROOT = tempfile.mkdtemp()

MARKYMARK_EXTENSIONS = [
    'markymark.extensions:LinkExtension',
    'markymark.extensions:FilerFileExtension',
]

MARKYMARK_CSS = [
    'markdown/css/markdown-editor.css',
    'markdown/css/markdown-editor-adminfix.css',
    'markdown/css/plugins/filer-file.css',
]

MARKYMARK_JS = [
    'markdown/js/markdown-init.js',
    'markdown/js/markdown.js',
    'markdown/js/markdown-editor.js',
    'markdown/js/plugins/clean.js',
    'markdown/js/plugins/anylink-link.js',
    'markdown/js/plugins/filer-file.js',
]
