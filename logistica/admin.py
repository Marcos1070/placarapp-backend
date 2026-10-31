from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import (Proveedor, Envio, MovimientoStock)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'cuit', 'email', 'activo')
    search_fields = ('nombre', 'cuit')
    list_filter = ('activo',)
    ordering = ('nombre',)

@admin.register(MovimientoStock)
class MovimientoStockAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "producto",
        "tipo",
        "cantidad",
        "fecha",
        "proveedor",
    )

    list_filter = ("tipo", "fecha")
    search_fields = (
        "producto__nombre",
        "proveedor__nombre",
        "observacion",
    )
    ordering = ("-fecha",)

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pedido",
        "direccion",
        "fecha_estimada",
        "estado",
        "numero_seguimiento",
    )

    list_filter = ("estado", "fecha_estimada")

    search_fields = (
        "direccion",
        "numero_seguimiento",
    )