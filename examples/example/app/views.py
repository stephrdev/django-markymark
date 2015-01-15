from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import MarkdownForm
from .models import Post


class MarkdownView(FormView):

    form_class = MarkdownForm
    template_name = 'example.html'

    def form_valid(self, form):
        return self.render_to_response({
            'form': form,
            'content': form.cleaned_data['content']
        })


class PostsView(TemplateView):

    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
