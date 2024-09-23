from django.urls import path
from . import views

urslpatterns = [
    path('', views.index, name='Home'),
]
