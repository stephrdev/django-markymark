from django.conf import settings
from django.contrib import admin
from django.urls import re_path
from django.views.static import serve

from examples.app.views import MarkdownView, PostsView


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', MarkdownView.as_view(), name='markdown'),
    re_path(r'^posts/$', PostsView.as_view(), name='posts'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
