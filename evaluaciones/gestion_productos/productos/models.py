from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Caracteristica(models.Model):
    ancho = models.CharField(max_length=5, default='0')
    alto = models.CharField(max_length=5, default='0')
    peso = models.CharField(max_length=5, default='0')
    def __str__(self):
        return f"({self.ancho} x {self.alto} x {self.peso})"

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    caracteristicas = models.OneToOneField(Caracteristica, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
