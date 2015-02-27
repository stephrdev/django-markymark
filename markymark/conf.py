from django.conf import settings
from . import defaults


MARKYMARK_EXTENSIONS = getattr(
    settings,
    'MARKYMARK_EXTENSIONS',
    defaults.DEFAULT_MARKYMARK_EXTENSIONS
)

MARKYMARK_TEMPLATES = getattr(
    settings,
    'MARKYMARK_TEMPLATES',
    defaults.DEFAULT_MARKYMARK_TEMPLATES
)
