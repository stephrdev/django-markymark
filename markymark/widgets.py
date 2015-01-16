from django.conf import settings

import floppyforms.__future__ as forms


class MarkdownTextarea(forms.Textarea):
    class Media:
        css = {'all': settings.MARKYMARK_CSS}
        js = settings.MARKYMARK_JS

    def __init__(self, *args, **kwargs):
        super(MarkdownTextarea, self).__init__(*args, **kwargs)
        self.attrs['data-provide'] = 'init-markdown'
