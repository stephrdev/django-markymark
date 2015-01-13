from django.views.generic.edit import FormView

from .forms import MarkdownForm


class MarkdownView(FormView):

    form_class = MarkdownForm
    template_name = 'example.html'

    def form_valid(self, form):
        return self.render_to_response(self.context, {})
