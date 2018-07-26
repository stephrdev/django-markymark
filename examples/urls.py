from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from examples.app.views import MarkdownView, PostsView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MarkdownView.as_view(), name='markdown'),
    url(r'^posts/$', PostsView.as_view(), name='posts'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
