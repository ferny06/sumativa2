from django.core.files import File
from tienda.models import Categoria, Producto
from pathlib import Path

# Crear categorías
categorias_data = [
    {'nombre': 'Novedades', 'slug': 'novedades', 'imagen': 'categorias/novedades.jpg'},
    {'nombre': 'Pantalones', 'slug': 'pantalones', 'imagen': 'categorias/pantalones.jpg'},
    {'nombre': 'Blusas/Poleras', 'slug': 'blusas', 'imagen': 'categorias/blusas.jpg'},
    {'nombre': 'Faldas', 'slug': 'faldas', 'imagen': 'categorias/faldas.jpg'},
]

categorias = {}
for cat_data in categorias_data:
    categoria = Categoria.objects.create(
        nombre=cat_data['nombre'],
        slug=cat_data['slug']
    )
    with open(f"media/{cat_data['imagen']}", 'rb') as f:
        categoria.imagen.save(
            Path(cat_data['imagen']).name,
            File(f),
            save=True
        )
    categorias[cat_data['slug']] = categoria

# Crear productos
productos_data = [
    # Blusas
    {'nombre': 'Polera manga corta', 'precio': 7990, 'imagen': 'productos/blu1.jpg', 'categoria': 'blusas'},
    {'nombre': 'Polera manga larga', 'precio': 9990, 'imagen': 'productos/blu2.jpg', 'categoria': 'blusas'},
    {'nombre': 'Polera diseño', 'precio': 12990, 'imagen': 'productos/blu3.jpg', 'categoria': 'blusas', 'en_descuento': True, 'precio_descuento': 8990},
    {'nombre': 'Polera estampada', 'precio': 8990, 'imagen': 'productos/bl4.jpg', 'categoria': 'blusas'},
    
    # Faldas
    {'nombre': 'Falda plisada', 'precio': 15990, 'imagen': 'productos/fal1.jpg', 'categoria': 'faldas'},
    {'nombre': 'Falda corta', 'precio': 12990, 'imagen': 'productos/fal2.jpg', 'categoria': 'faldas', 'en_descuento': True, 'precio_descuento': 9990},
    {'nombre': 'Falda larga', 'precio': 18990, 'imagen': 'productos/fal3.jpg', 'categoria': 'faldas'},
    {'nombre': 'Falda jean', 'precio': 16990, 'imagen': 'productos/fal4.jpg', 'categoria': 'faldas'},
    
    # Pantalones
    {'nombre': 'Jeans clásico', 'precio': 19990, 'imagen': 'productos/pant1.jpg', 'categoria': 'pantalones'},
    {'nombre': 'Pantalón cargo', 'precio': 22990, 'imagen': 'productos/pant2.jpg', 'categoria': 'pantalones', 'en_descuento': True, 'precio_descuento': 17990},
    {'nombre': 'Pantalón formal', 'precio': 24990, 'imagen': 'productos/pant3.jpg', 'categoria': 'pantalones'},
    {'nombre': 'Jeans rasgado', 'precio': 21990, 'imagen': 'productos/pant4.jpg', 'categoria': 'pantalones'},
]

for prod_data in productos_data:
    producto = Producto.objects.create(
        nombre=prod_data['nombre'],
        precio=prod_data['precio'],
        categoria=categorias[prod_data['categoria']],
        en_descuento=prod_data.get('en_descuento', False),
        precio_descuento=prod_data.get('precio_descuento', None)
    )
    with open(f"media/{prod_data['imagen']}", 'rb') as f:
        producto.imagen.save(
            Path(prod_data['imagen']).name,
            File(f),
            save=True
        )

print("Datos de ejemplo creados exitosamente")
