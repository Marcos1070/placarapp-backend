from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_cliente')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name} ({self.usuario.username})'


class Categoria(models.Model):
    #categorias de los muebles
    nombre = models.CharField(max_length=100, unique= True)
    descripcion = models.TextField(blank=True, null= True)

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    #locales fisicos
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.ciudad}'

