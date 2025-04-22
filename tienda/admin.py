from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    search_fields = ['nombre']
    prepopulated_fields = {"slug": ("nombre",)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'es_descuento', 'precio_original', 'precio_descuento']
    list_filter = ['categoria', 'es_descuento']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio', 'es_descuento', 'precio_descuento']
    fieldsets = (
        (None, {'fields': ('nombre', 'descripcion', 'precio', 'precio_original', 'precio_descuento', 'es_descuento', 'categoria', 'imagen')}),
    )
