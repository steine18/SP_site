from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('registery/', views.registery, name = 'registery'),
]