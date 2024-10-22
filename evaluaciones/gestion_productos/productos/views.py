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
        # Capturar los valores del formulario
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        marca_id = request.POST['marca']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        precio = request.POST['precio']
        ancho = request.POST['ancho']
        alto = request.POST['alto']
        peso = request.POST['peso']
        categoria_id = request.POST['categoria']

        # Buscar la marca y la categoría en memoria
        marca = obtener_elemento_por_id(marcas, marca_id)
        categoria = obtener_elemento_por_id(categorias, categoria_id)

        # Características del producto
        caracteristicas = {
            'ancho': ancho,
            'alto': alto,
            'peso': peso,
        }

        # Crear el producto y agregarlo a la lista de productos en memoria
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

# Consulta de productos (en memoria)
def consulta_productos(request):
    return render(request, 'productos/consulta.html', {'productos': productos})

# Resultado del registro
def resultado_producto(request):
    return render(request, 'productos/resultado.html', {'productos': productos})

def index(request):
    return render(request, 'productos/index.html')

def crear_categoria(request):
    if request.method == 'POST':
        # Capturar los valores del formulario
        nombre = request.POST['nombre']  # El name del input debe ser 'nombre', no 'categoria'

        # Crear la categoría y agregarla a la lista de categorías en memoria
        nueva_categoria = {
            'id': len(categorias) + 1,
            'nombre': nombre,
        }
        categorias.append(nueva_categoria)

        # Redirigir a la vista de consulta de productos (o alguna otra)
        return redirect('index')

    return render(request, 'productos/categoria.html')

def filtrar_productos(request):
    """Vista para filtrar productos por marca o categoría según los valores seleccionados en el formulario"""

    # Obtener los valores seleccionados de los parámetros de la URL (GET)
    marca_id = request.GET.get('marca')  # Obtener el valor de marca desde el formulario
    categoria_id = request.GET.get('categoria')  # Obtener el valor de categoría desde el formulario

    # Inicialmente, comenzamos con todos los productos
    productos_filtrados = productos

    # Filtrar por marca solo si se selecciona una marca válida
    if marca_id and marca_id != "":  # Si marca_id tiene valor
        marca = obtener_elemento_por_id(marcas, marca_id)
        if marca:  # Filtrar productos por marca
            productos_filtrados = [p for p in productos if p['marca'] == marca['nombre']]

    # Filtrar por categoría solo si se selecciona una categoría válida
    if categoria_id and categoria_id != "":  # Si categoria_id tiene valor
        categoria = obtener_elemento_por_id(categorias, categoria_id)
        if categoria:  # Filtrar productos por categoría
            productos_filtrados = [p for p in productos_filtrados if p['categoria'] == categoria['nombre']]

    # Renderizar el template con los productos filtrados
    return render(request, 'productos/filtrar.html', {
        'productos': productos_filtrados,  # Lista de productos filtrados
        'marcas': marcas,  # Lista de marcas para el formulario
        'categorias': categorias  # Lista de categorías para el formulario
    })
