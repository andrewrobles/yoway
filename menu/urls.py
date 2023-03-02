# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('history/', views.history, name='history'),
    path('done/<int:order_id>/', views.done, name='done'),
    path('not-done/<int:order_id>/', views.not_done, name='not_done'),
]