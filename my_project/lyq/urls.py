from django.urls import re_path

from . import views

app_name = 'lyq'

urlpatterns = [
    re_path(r'^response/$', views.demo_response, name = 'res'),
    re_path(r'^view/$', views.demo_view, name = 'view'),
    re_path(r'^view2/$', views.demo_view2),
    re_path(r'^json/$', views.demo_json),
    re_path(r'^redirect/$', views.demo_redirect),
]