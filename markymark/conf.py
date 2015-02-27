from django.conf import settings
from . import defaults


MARKYMARK_EXTENSIONS = getattr(
    settings,
    'MARKYMARK_EXTENSIONS',
    defaults.DEFAULT_MARKYMARK_EXTENSIONS
)

MARKYMARK_CSS = getattr(
    settings,
    'MARKYMARK_CSS',
    defaults.DEFAULT_MARKYMARK_CSS
)

MARKYMARK_JS = getattr(
    settings,
    'MARKYMARK_JS',
    defaults.DEFAULT_MARKYMARK_JS
)

MARKYMARK_TEMPLATES = getattr(
    settings,
    'MARKYMARK_TEMPLATES',
    defaults.DEFAULT_MARKYMARK_TEMPLATES
)
