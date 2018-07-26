import tempfile


DEBUG = True

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

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
}]

STATIC_URL = '/static/'
MEDIA_URL = '/'

ANYLINK_EXTENSIONS = (
    'anylink.extensions.ExternalLink',
)

MEDIA_ROOT = tempfile.mkdtemp()

MARKYMARK_EXTENSIONS = [
    'markymark.extensions.anylink',
    'markymark.extensions.filer',
    'markymark.extensions.autolink',
    'markymark.extensions.clean',
]
