import os

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
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'easy_thumbnails',
    'filer',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'markymark', 'templates'),
)

STATIC_URL = '/'
MEDIA_URL = '/'
