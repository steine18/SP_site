from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^M1ggy0n1x/$', views.home2, name='home'),
    re_path(r'^im-not-a-local/$', views.what_to_do, name='travel'),
    path('form/<str:number>/', views.quote, name='quote'),
    re_path(r'^approval/$', views.approve, name='approve'),
]
