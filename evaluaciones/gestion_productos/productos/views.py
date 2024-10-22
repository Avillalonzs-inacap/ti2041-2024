from django.shortcuts import render, redirect

# Datos en memoria
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

def obtener_elemento_por_id(lista, elemento_id):
    """Función auxiliar para buscar un elemento en una lista por su ID"""
    return next((item for item in lista if item['id'] == int(elemento_id)), None)

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

        marca = obtener_elemento_por_id(marcas, marca_id)
        categoria = obtener_elemento_por_id(categorias, categoria_id)

        caracteristicas = {
            'ancho': ancho,
            'alto': alto,
            'peso': peso,
        }

        nuevo_producto = {
            'codigo': codigo,
            'nombre': nombre,
            'marca': marca['nombre'] if marca else 'Desconocida',
            'fecha_vencimiento': fecha_vencimiento,
            'precio': precio,
            'caracteristicas': caracteristicas,
            'categoria': categoria['nombre'] if categoria else 'Desconocida'
        }
        productos.append(nuevo_producto)

        return redirect('resultado_producto')

    return render(request, 'productos/registro.html', {'marcas': marcas, 'categorias': categorias})

def consulta_productos(request):
    return render(request, 'productos/consulta.html', {'productos': productos})

def resultado_producto(request):
    return render(request, 'productos/resultado.html', {'productos': productos})

def index(request):
    return render(request, 'productos/index.html')

def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']

        nueva_categoria = {
            'id': len(categorias) + 1,
            'nombre': nombre,
        }
        categorias.append(nueva_categoria)

        return redirect('index')

    return render(request, 'productos/categoria.html')

def filtrar_productos(request):
    """Vista para filtrar productos por marca o categoría según los valores seleccionados en el formulario"""

    marca_id = request.GET.get('marca')
    categoria_id = request.GET.get('categoria')

    productos_filtrados = productos


    if marca_id and marca_id != "":
        marca = obtener_elemento_por_id(marcas, marca_id)
        if marca:
            productos_filtrados = [p for p in productos if p['marca'] == marca['nombre']]


    if categoria_id and categoria_id != "":
        categoria = obtener_elemento_por_id(categorias, categoria_id)
        if categoria:
            productos_filtrados = [p for p in productos_filtrados if p['categoria'] == categoria['nombre']]


    return render(request, 'productos/filtrar.html', {
        'productos': productos_filtrados,
        'marcas': marcas,  
        'categorias': categorias  
    })
