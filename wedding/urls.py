from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name = 'home'),
    re_path(r'^what-to-do$', views.what_to_do, name = 'what-to-do'),
    re_path(r'(?P<category>[A-z]*)/$', views.what_to_do_detail, name = 'what-to-do/category')
]