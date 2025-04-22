from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, LoginForm
from django.contrib import messages
from .models import Usuario
from django.db.models import Q

# Create your views here.

# Vista de registro de usuario

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.rol = 'usuario'  # Todos los registros normales serán usuarios
            usuario.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Vista de login personalizada

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username_or_email, password=password)
        if user is None:
            # Intentar login por email
            try:
                user_obj = Usuario.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except Usuario.DoesNotExist:
                user = None
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido/a {user.nombre}!')
            return redirect('tienda:novedades')
        else:
            messages.error(request, 'Usuario/correo o contraseña incorrectos.')
    return render(request, 'iniciosesion.html')

# Vista de logout

def logout_view(request):
    logout(request)
    return redirect('login')
