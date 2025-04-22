from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from functools import wraps

def rol_requerido(rol):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if hasattr(request.user, 'rol') and request.user.rol == rol:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden('No tienes permiso para acceder a esta página.')
        return _wrapped_view
    return decorator
