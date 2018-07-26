import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'examples'

DEBUG = True

ALLOWED_HOSTS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.db'),
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'anylink',
    'easy_thumbnails',
    'filer',
    'markymark',

    'examples.app',

]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MARKYMARK_EXTENSIONS = [
    'markymark.extensions.autolink:AutoLinkExtension',
    'markdown.extensions.codehilite',
    'markdown.extensions.fenced_code',
    'markdown.extensions.tables'
]

ANYLINK_EXTENSIONS = (
    'anylink.extensions.ExternalLink',
)

ROOT_URLCONF = 'examples.urls'

WSGI_APPLICATION = 'examples.wsgi.application'

STATIC_URL = '/static/'
