from django.conf import settings
from . import defaults


MARKYMARK_EXTENSIONS = getattr(
    settings,
    'MARKYMARK_EXTENSIONS',
    defaults.MARKYMARK_EXTENSIONS
)

MARKYMARK_CSS = getattr(
    settings,
    'MARKYMARK_CSS',
    defaults.MARKYMARK_CSS
)

MARKYMARK_JS = getattr(
    settings,
    'MARKYMARK_JS',
    defaults.MARKYMARK_JS
)
