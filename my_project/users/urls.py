from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^index/$', views.index),
    re_path(r'^get_num/$', views.get_num),
    re_path(r'^get_body/$', views.get_body),
    re_path(r'^get_json/$', views.get_json),
    re_path(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{8})$', views.weather),
]