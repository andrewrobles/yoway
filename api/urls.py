# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guest/', views.guest, name='guest'),
    path('cook/', views.cook, name='cook'),
]