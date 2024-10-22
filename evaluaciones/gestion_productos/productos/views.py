from django.shortcuts import render, redirect
from .models import Producto, Marca, Categoria, Caracteristica

def registro_producto(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        marca_id = request.POST['marca']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        precio = request.POST['precio']
        ancho = request.POST['ancho']
        alto = request.POST['alto']
        peso = request.POST['peso']
        categoria_id = request.POST['categoria']

        # Obtener la marca y categoría desde la base de datos
        marca = Marca.objects.get(id=marca_id)
        categoria = Categoria.objects.get(id=categoria_id)

        # Crear las características del producto
        caracteristicas = Caracteristica.objects.create(ancho=ancho, alto=alto, peso=peso)

        # Crear y guardar el nuevo producto
        nuevo_producto = Producto.objects.create(
            codigo=codigo,
            nombre=nombre,
            marca=marca,
            precio=precio,
            categoria=categoria,
            caracteristicas=caracteristicas
        )

        return redirect('resultado_producto')

    # Obtener marcas y categorías desde la base de datos
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos/registro.html', {'marcas': marcas, 'categorias': categorias})

def consulta_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos desde la base de datos
    return render(request, 'productos/consulta.html', {'productos': productos})

def resultado_producto(request):
    productos = Producto.objects.all()
    return render(request, 'productos/resultado.html', {'productos': productos})

def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nueva_categoria = Categoria.objects.create(nombre=nombre)
        return redirect('index')

    return render(request, 'productos/categoria.html')

def filtrar_productos(request):
    marca_id = request.GET.get('marca')
    categoria_id = request.GET.get('categoria')

    productos_filtrados = Producto.objects.all()

    if marca_id and marca_id != "":
        productos_filtrados = productos_filtrados.filter(marca_id=marca_id)

    if categoria_id and categoria_id != "":
        productos_filtrados = productos_filtrados.filter(categoria_id=categoria_id)

    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    return render(request, 'productos/filtrar.html', {
        'productos': productos_filtrados,
        'marcas': marcas,
        'categorias': categorias
    })

def index(request):
    return render(request, 'productos/index.html')