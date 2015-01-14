from django.conf.urls import patterns, url

from app.views import MarkdownView


urlpatterns = patterns(
    '',
    url(r'^$', MarkdownView.as_view(), name='markdown'),
)
