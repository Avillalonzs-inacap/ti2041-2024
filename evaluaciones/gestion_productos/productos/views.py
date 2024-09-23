from django.shortcuts import render, redirect

# Datos en memoria
productos = []

def registro_producto(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        marca = request.POST['marca']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        # Agregar el producto a la lista en memoria
        productos.append({'codigo': codigo, 'nombre': nombre, 'marca': marca, 'fecha_vencimiento': fecha_vencimiento})
        return redirect('resultado_producto')
    return render(request, 'productos/registro.html')

def resultado_producto(request):
    return render(request, 'productos/resultado.html')

def consulta_productos(request):
    return render(request, 'productos/consulta.html', {'productos': productos})
