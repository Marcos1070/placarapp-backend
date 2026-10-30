from django.contrib import admin
from .models import Cliente, Categoria, Sucursal


admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Sucursal)