from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_producto, name='registro_producto'),
    path('consulta/', views.consulta_productos, name='consulta_productos'),
    path('resultado/', views.resultado_producto, name='resultado_producto'),
]
