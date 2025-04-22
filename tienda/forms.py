from django import forms
from .models import Producto, Carrito

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria', 'es_descuento', 'precio_original', 'precio_descuento']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class CarritoAddForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
        }
