from django.shortcuts import render, redirect
from .models import Producto, Marca, Categoria

# Datos en memoria<ss<
productos = []

marcas = [
    {'id': 1, 'nombre': 'Marca 1'},
    {'id': 2, 'nombre': 'Marca 2'},
    {'id': 3, 'nombre': 'Marca 3'},
]

categorias = [
    {'id': 1, 'nombre': 'Categoria 1'},
    {'id': 2, 'nombre': 'Categoria 2'},
    {'id': 3, 'nombre': 'Categoria 3'},
]

# Registro de productos
def registro_producto(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        marca_id = request.POST.get('marca')  # Obtener el ID de la marca seleccionada
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')  # Obtener el ID de la categoría seleccionada

        # Obtener instancias de Marca y Categoria
        marca = Marca.objects.get(id=marca_id)
        categoria = Categoria.objects.get(id=categoria_id)

        # Crear y guardar el producto en la base de datos
        producto = Producto(codigo=codigo, nombre=nombre, marca=marca, fecha_vencimiento=fecha_vencimiento, precio=precio, categoria=categoria)
        producto.save()

        return redirect('consulta_productos')
    
    # Obtener marcas y categorías para el formulario
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos/registro.html', {'marcas': marcas, 'categorias': categorias})

# Consulta de productos
def consulta_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/consulta.html', {'productos': productos})

# Resultado del registro (opcional)
def resultado_producto(request):
    return render(request, 'productos/resultado.html')