from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^response/$', views.demo_response),
    re_path(r'^view/$', views.demo_view),
    re_path(r'^view2/$', views.demo_view2),
    re_path(r'^json/$', views.demo_json),
]