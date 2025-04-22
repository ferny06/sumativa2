from django.urls import path
from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'tienda'

# Vista personalizada para logout
def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('tienda:index'))

urlpatterns = [
    path('', views.index, name='index'),
    path('blusas/', views.blusas, name='blusas'),
    path('faldas/', views.faldas, name='faldas'),
    path('pantalones/', views.pantalones, name='pantalones'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('contacto/', views.contacto, name='contacto'),
    path('iniciosesion/', views.iniciosesion, name='iniciosesion'),
    path('registrate/', views.registrate, name='registrate'),
    path('olvidada/', views.olvidada, name='olvidada'),
    path('admin/', views.admin_view, name='admin'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('descuentos/', views.descuentos, name='descuentos'),
    path('novedades/', views.novedades, name='novedades'),
    path('logout/', custom_logout, name='logout'),
]
