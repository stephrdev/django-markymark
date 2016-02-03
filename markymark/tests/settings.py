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

    'anylink',
    'easy_thumbnails',
    'filer',
    'markymark',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'markymark', 'templates'),
)

STATIC_URL = '/static/'
MEDIA_URL = '/'

ANYLINK_EXTENSIONS = (
    'anylink.extensions.ExternalLink',
)

MEDIA_ROOT = tempfile.mkdtemp()

MARKYMARK_EXTENSIONS = [
    'markymark.extensions.contrib.anylink',
    'markymark.extensions.contrib.filer',
    'markymark.extensions.autolink',
    'markymark.extensions.clean',
]
