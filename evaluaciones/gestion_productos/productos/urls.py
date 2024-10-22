from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro_producto, name='registro_producto'),
    path('consulta/', views.consulta_productos, name='consulta_productos'),
    path('resultado/', views.resultado_producto, name='resultado_producto'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('filtrar_productos/', views.filtrar_productos, name='filtrar_productos'),
    ]
