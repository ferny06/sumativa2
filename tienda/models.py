from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    imagen = models.ImageField(upload_to='categorias/')
    
    class Meta:
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    identificador = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    # Campos para descuentos
    precio_original = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    es_descuento = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def precio_actual(self):
        return self.precio_descuento if self.es_descuento else self.precio

    class Meta:
        verbose_name_plural = "Productos"
        # ordering = ['-fecha_creacion']

class Carrito(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='carritos')
    producto = models.ForeignKey(Producto, to_field='identificador', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'producto')

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} ({self.usuario.username})"
