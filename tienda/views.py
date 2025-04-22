from django.shortcuts import render, redirect
from .models import Categoria, Producto, Carrito
from .forms import ProductoForm, CarritoAddForm
from usuarios.decorators import rol_requerido
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    categorias = Categoria.objects.all()
    productos_descuento = Producto.objects.filter(es_descuento=True)[:4]
    return render(request, 'index.html', {
        'categorias': categorias,
        'productos_descuento': productos_descuento
    })

def blusas(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    productos = Producto.objects.filter(categoria='blusas')
    return render(request, 'blusas.html', {'productos': productos})

def faldas(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    productos = Producto.objects.filter(categoria='faldas')
    return render(request, 'faldas.html', {'productos': productos})

def pantalones(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    productos = Producto.objects.filter(categoria='pantalones')
    return render(request, 'pantalones.html', {'productos': productos})

@login_required
@rol_requerido('usuario')
def carrito(request):
    items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.producto.precio_actual() * item.cantidad for item in items)
    return render(request, 'carrito.html', {'items': items, 'total': total})

def contacto(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    return render(request, 'contacto.html')

def iniciosesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tienda:index')
        else:
            return render(request, 'iniciosesion.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'iniciosesion.html')

def registrate(request):
    # Redirigir siempre al registro real
    return redirect('/usuarios/registro/')

def olvidada(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    # Eliminado: return render(request, 'olvidada.html')
    # La plantilla olvidada.html ya no existe, por lo tanto, la vista se puede eliminar o redirigir a otra página.
    return redirect('tienda:iniciosesion')  # Redirigir a otra página

@rol_requerido('admin')
def admin_view(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    return render(request, 'admin.html')

@rol_requerido('admin')
def agregar_producto(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente.')
            return redirect('admin_view')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

@rol_requerido('admin')
def lista_productos(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

@rol_requerido('admin')
def editar_producto(request, producto_id):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado correctamente.')
            return redirect('tienda:lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

@rol_requerido('admin')
def eliminar_producto(request, producto_id):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('tienda:lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

@login_required
@rol_requerido('usuario')
def agregar_al_carrito(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        messages.error(request, 'El producto seleccionado no existe.')
        return redirect('tienda:index')
    carrito_item, created = Carrito.objects.get_or_create(usuario=request.user, producto=producto)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        carrito_item.cantidad = cantidad
        carrito_item.save()
        messages.success(request, f'{producto.nombre} agregado al carrito.')
        return redirect('tienda:carrito')
    return redirect('tienda:carrito')

@login_required
@rol_requerido('usuario')
def eliminar_del_carrito(request, item_id):
    item = Carrito.objects.get(pk=item_id, usuario=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Producto eliminado del carrito.')
        return redirect('tienda:carrito')
    return render(request, 'eliminar_del_carrito.html', {'item': item})

def novedades(request):
    if not request.user.is_authenticated:
        return redirect('tienda:iniciosesion')
    productos = Producto.objects.filter(categoria='novedades')
    return render(request, 'novedades.html', {'productos': productos})

def descuentos(request):
    productos = Producto.objects.filter(es_descuento=True)
    return render(request, 'descuentos.html', {'productos': productos})
