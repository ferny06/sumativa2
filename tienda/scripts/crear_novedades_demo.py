from tienda.models import Producto
from django.core.files import File
import os

def crear_novedades_demo():
    base_path = os.path.join('media', 'productos')
    novedades = [
        {
            'nombre': 'Vestido Floral Primavera',
            'categoria': 'novedades',
            'precio_original': 24990,
            'precio_descuento': 19990,
            'es_descuento': True,
            'descripcion': 'Vestido largo con estampado floral, ideal para la temporada.',
            'identificador': 7001,
            'imagen': 'vestido1.jpg',
        },
        {
            'nombre': 'Chaqueta Denim Oversize',
            'categoria': 'novedades',
            'precio_original': 29990,
            'precio_descuento': 24990,
            'es_descuento': True,
            'descripcion': 'Chaqueta de mezclilla oversize, tendencia actual.',
            'identificador': 7002,
            'imagen': 'chaqueta1.jpg',
        },
        {
            'nombre': 'Falda Midi Satinada',
            'categoria': 'novedades',
            'precio_original': 18990,
            'precio_descuento': 15990,
            'es_descuento': False,
            'descripcion': 'Falda midi de satín, elegante y cómoda.',
            'identificador': 7003,
            'imagen': 'falda_novedad1.jpg',
        },
        {
            'nombre': 'Polera Tie Dye',
            'categoria': 'novedades',
            'precio_original': 12990,
            'precio_descuento': 9990,
            'es_descuento': True,
            'descripcion': 'Polera con diseño tie dye, colores vibrantes.',
            'identificador': 7004,
            'imagen': 'polera1.jpg',
        },
        {
            'nombre': 'Sweater Tejido Pastel',
            'categoria': 'novedades',
            'precio_original': 15990,
            'precio_descuento': 12990,
            'es_descuento': False,
            'descripcion': 'Sweater tejido en tonos pastel, suave y abrigador.',
            'identificador': 7005,
            'imagen': 'sweater1.jpg',
        },
    ]
    for prod in novedades:
        imagen_path = os.path.join(base_path, prod['imagen'])
        obj, creado = Producto.objects.get_or_create(
            identificador=prod['identificador'],
            defaults={
                'nombre': prod['nombre'],
                'categoria': prod['categoria'],
                'precio_original': prod['precio_original'],
                'precio_descuento': prod['precio_descuento'],
                'es_descuento': prod['es_descuento'],
                'descripcion': prod['descripcion'],
                'precio': prod['precio_descuento'] if prod['es_descuento'] else prod['precio_original'],
            }
        )
        if creado and os.path.exists(imagen_path):
            with open(imagen_path, 'rb') as f:
                obj.imagen.save(prod['imagen'], File(f), save=True)
            print(f"Producto creado: {prod['nombre']} con imagen {prod['imagen']}")
        elif creado:
            print(f"Producto creado: {prod['nombre']} (sin imagen, archivo no encontrado)")
        else:
            print(f"Ya existe: {prod['nombre']}")

if __name__ == "__main__":
    crear_novedades_demo()
