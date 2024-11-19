from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('registro/', views.registro_producto, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('consulta_productos/', views.consulta_productos, name='consulta_productos'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('filtrar_productos/', views.filtrar_productos, name='filtrar_productos'),


]
