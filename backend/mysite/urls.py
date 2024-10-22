from django.contrib import admin
from django.urls import include, path
from django.urls import re_path as url
from polls.views import *

# Статика
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", AnimeVideoView.as_view(), name="on shit"),
    path("admin/", admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)