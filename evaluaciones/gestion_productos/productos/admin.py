from django.contrib import admin
from .models import Producto, Categoria, Marca, Caracteristica

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Caracteristica)
