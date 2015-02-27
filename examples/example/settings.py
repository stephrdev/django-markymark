import os


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'database.db'),
    }
}

TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = os.path.join(ROOT_DIR, 'web', 'media')
MEDIA_URL = '/media/'

SECRET_KEY = 'test'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'example.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'example.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'anylink',
    'easy_thumbnails',
    'filer',
    'markymark',
    'example.app',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)

TEST_RUNNER = ''

MARKYMARK_EXTENSIONS = [
    'markymark.extensions:AutoLinkExtension',
    'markymark.extensions:LinkExtension',
    'markymark.extensions:FilerFileExtension',
    'markdown.extensions.codehilite',
    'markdown.extensions.fenced_code',
]

ANYLINK_EXTENSIONS = (
    'anylink.extensions.ExternalLink',
)

FILER_FILE_MODELS = (
    'filer.models.imagemodels.Image',
    'filer.models.filemodels.File',
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
