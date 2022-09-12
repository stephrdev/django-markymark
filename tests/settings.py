import tempfile


DEBUG = True

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MIDDLEWARE = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'anylink',
    'easy_thumbnails',
    'markymark',
    'filer',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }
]

STATIC_URL = '/static/'
MEDIA_URL = '/'

ANYLINK_EXTENSIONS = ('anylink.extensions.ExternalLink',)

MEDIA_ROOT = tempfile.mkdtemp()

MARKYMARK_ICONLIBRARY = None
MARKYMARK_EXTENSIONS = [
    'markymark.extensions.anylink',
    'markymark.extensions.autolink',
    'markymark.extensions.clean',
    'markymark.extensions.filer',
]
