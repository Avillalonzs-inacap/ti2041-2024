from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Producto, Marca, Categoria, Caracteristica


def logout_view(request):
    request.session.flush()
    return redirect('login')  # Redirige al login después de hacer logout

# Vista de login
def login_view(request):
    if request.method == "POST":
        # Crear el formulario de autenticación con los datos de la solicitud
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Si el formulario es válido, obtener el usuario autenticado
            user = form.get_user()
            login(request, user)
            # Redirigir a la página de inicio (index) después de iniciar sesión
            next_url = request.GET.get('next') or 'productos:index'
            return redirect(next_url)
        else:
            # Opcional: Agregar un mensaje de error para el usuario
            return render(request, 'productos/login.html', {'form': form, 'error': 'Credenciales inválidas'})
    else:
        # Mostrar el formulario vacío si el método es GET
        form = AuthenticationForm()

    return render(request, 'productos/login.html', {'form': form})


# Vista para logout
def logout_view(request):
    logout(request)
    return redirect('productos:login')  # Redirige al login después de hacer logout

# Vista protegida de registro de producto
@login_required
def registro_producto(request):
    if request.method == 'POST':
        # Validar que todos los campos estén presentes
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        marca_id = request.POST.get('marca')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        precio = request.POST.get('precio')
        ancho = request.POST.get('ancho')
        alto = request.POST.get('alto')
        peso = request.POST.get('peso')
        categoria_id = request.POST.get('categoria')

        # Verificar que todos los datos sean válidos antes de proceder
        if not (codigo and nombre and marca_id and fecha_vencimiento and precio and ancho and alto and peso and categoria_id):
            return render(request, 'productos/registro.html', {'error': 'Todos los campos son obligatorios'})

        try:
            marca = get_object_or_404(Marca, id=marca_id)
            categoria = get_object_or_404(Categoria, id=categoria_id)
        except:
            return render(request, 'productos/registro.html', {'error': 'Marca o Categoría no encontrados'})

        # Crear las características
        caracteristicas = Caracteristica.objects.create(ancho=ancho, alto=alto, peso=peso)

        # Crear el producto
        Producto.objects.create(
            codigo=codigo,
            nombre=nombre,
            marca=marca,
            precio=precio,
            fecha_vencimiento=fecha_vencimiento,
            categoria=categoria,
            caracteristicas=caracteristicas
        )

        return redirect('productos:resultado_producto')  # Redirige a la página de resultado del producto

    # Cargar las marcas y categorías para mostrar en el formulario
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos/registro.html', {'marcas': marcas, 'categorias': categorias})


# Vista principal (index), protegida por login
@login_required
def index(request):
    return render(request, 'productos/index.html')


# Vista para consultar productos (solo accesible por usuarios autenticados)
@login_required
def consulta_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/consulta.html', {'productos': productos})


# Vista para mostrar resultados de productos
@login_required
def resultado_producto(request):
    productos = Producto.objects.all()
    return render(request, 'productos/resultado.html', {'productos': productos})


# Vista para crear una nueva categoría
@login_required
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if not nombre:
            return render(request, 'productos/categoria.html', {'error': 'El nombre de la categoría es obligatorio'})
        Categoria.objects.create(nombre=nombre)
        return redirect('productos:registro_producto')  # Redirige al registro de productos después de crear la categoría

    return render(request, 'productos/categoria.html')


# Vista para filtrar productos según marca y categoría
@login_required
def filtrar_productos(request):
    marca_id = request.GET.get('marca')
    categoria_id = request.GET.get('categoria')

    productos_filtrados = Producto.objects.all()

    if marca_id:
        productos_filtrados = productos_filtrados.filter(marca_id=marca_id)

    if categoria_id:
        productos_filtrados = productos_filtrados.filter(categoria_id=categoria_id)

    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    return render(request, 'productos/filtrar.html', {
        'productos': productos_filtrados,
        'marcas': marcas,
        'categorias': categorias
    })
