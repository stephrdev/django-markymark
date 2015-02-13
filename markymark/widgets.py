from django import forms

from markymark import conf


class MarkdownTextarea(forms.Textarea):
    class Media:
        css = {'all': conf.MARKYMARK_CSS}
        js = conf.MARKYMARK_JS

    def __init__(self, *args, **kwargs):
        super(MarkdownTextarea, self).__init__(*args, **kwargs)
        self.attrs['data-provide'] = 'init-markdown'
