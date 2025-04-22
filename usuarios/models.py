from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('usuario', 'Usuario'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='usuario')
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    sexo = models.CharField(max_length=1, choices=SEXOS)
    fecha_nacimiento = models.DateField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'telefono', 'sexo', 'fecha_nacimiento']

    def __str__(self):
        return f"{self.username} ({self.rol})"

# Nota: Recuerda migrar y configurar AUTH_USER_MODEL en settings.py
