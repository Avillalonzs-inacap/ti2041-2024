from ninja import NinjaAPI
from ninja.security import HttpBearer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Categoria, Marca, Producto
from django.shortcuts import get_object_or_404
from decimal import Decimal

# Seguridad con JWT
class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            JWTAuthentication().authenticate(request)
            return token
        except Exception:
            return None

# Crear instancia de la API
api = NinjaAPI()

# ENDPOINTS PÚBLICOS
@api.get("/categorias", tags=["Categorías"])
def listar_categorias(request):
    return [{"id": cat.id, "nombre": cat.nombre} for cat in Categoria.objects.all()]

@api.get("/marcas", tags=["Marcas"])
def listar_marcas(request):
    return [{"id": marca.id, "nombre": marca.nombre} for marca in Marca.objects.all()]

@api.get("/productos", tags=["Productos"])
def listar_productos(request, marca: int = None, categoria: int = None):
    productos = Producto.objects.all()
    if marca:
        productos = productos.filter(marca_id=marca)
    if categoria:
        productos = productos.filter(categoria_id=categoria)
    return [
        {
            "codigo": p.codigo,
            "nombre": p.nombre,
            "precio": float(p.precio),
            "marca": p.marca.nombre,
            "categoria": p.categoria.nombre,
        }
        for p in productos
    ]

@api.get("/productos/{codigo}", tags=["Productos"])
def detalle_producto(request, codigo: str):
    producto = get_object_or_404(Producto, codigo=codigo)
    return {
        "codigo": producto.codigo,
        "nombre": producto.nombre,
        "precio": float(producto.precio),
        "marca": producto.marca.nombre,
        "categoria": producto.categoria.nombre,
        "caracteristicas": {
            "ancho": producto.caracteristicas.ancho if producto.caracteristicas else None,
            "alto": producto.caracteristicas.alto if producto.caracteristicas else None,
            "peso": producto.caracteristicas.peso if producto.caracteristicas else None,
        },
    }

# ENDPOINTS PROTEGIDOS POR JWT
@api.put("/productos/{codigo}/modificar", tags=["Productos"], auth=JWTAuth())
def modificar_producto(request, codigo: str, payload: dict):
    producto = get_object_or_404(Producto, codigo=codigo)
    for key, value in payload.items():
        if hasattr(producto, key):
            if key == "precio":  # Asegúrate de manejar correctamente los Decimals
                value = Decimal(value)
            setattr(producto, key, value)
    producto.save()
    return {"success": True, "message": "Producto modificado exitosamente"}

@api.post("/token", tags=["Autenticación"])
def obtener_token(request, username: str, password: str):
    from django.contrib.auth.models import User
    from django.contrib.auth import authenticate

    user = authenticate(username=username, password=password)
    if not user:
        return {"error": "Credenciales inválidas"}
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
