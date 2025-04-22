from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
import re
from django.core.exceptions import ValidationError

class RegistroUsuarioForm(UserCreationForm):
    nombre = forms.CharField(max_length=100, required=True, label='Nombre Completo')
    telefono = forms.CharField(max_length=15, required=True, label='Teléfono')
    email = forms.EmailField(required=True, label='Correo Electrónico')
    sexo = forms.ChoiceField(choices=Usuario.SEXOS, required=True, label='Sexo')
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label='Fecha de Nacimiento')

    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'telefono', 'email', 'sexo', 'fecha_nacimiento', 'password1', 'password2']

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not re.match(r'^\+?\d{9,15}$', telefono):
            raise ValidationError('Ingrese un número de teléfono válido (9-15 dígitos, puede incluir +).')
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError('Este correo ya está registrado.')
        return email

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha is None:
            raise ValidationError('Ingrese una fecha válida.')
        return fecha

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contraseñas no coinciden.')
        # Validaciones personalizadas
        if len(password1) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        if not re.search(r'[A-Z]', password1):
            raise ValidationError('La contraseña debe tener al menos una letra mayúscula.')
        if not re.search(r'\d', password1):
            raise ValidationError('La contraseña debe tener al menos un número.')
        if not re.search(r'[^\w]', password1):
            raise ValidationError('La contraseña debe tener al menos un caracter especial.')
        return password2

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
