from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente, Categoria, Sucursal


#serializador para el usuario nativo de django
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']



#serializador para el cliente (incluye los datos del usuario asociado)
class ClienteSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = Cliente
        fields = ['id', 'usuario', 'telefono', 'direccion', 'ciudad']


#serializador para categoria de los muebles
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


#serializador para Sucursal
class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'