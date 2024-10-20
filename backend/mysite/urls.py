from django.contrib import admin
from django.urls import include, path
from django.urls import re_path as url
from polls.views import *

urlpatterns = [
    path("", AnimeVideoView.as_view(), name="on shit"),
    path("admin/", admin.site.urls)
]