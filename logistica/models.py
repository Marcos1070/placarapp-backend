from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    cuit = models.CharField(max_length=13, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre



class MovimientoStock(models.Model):

    TIPO_CHOICES = [
        ("ENTRADA", "Entrada"),
        ("SALIDA", "Salida"),
    ]

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES
    )

    cantidad = models.PositiveIntegerField()

    fecha = models.DateTimeField(auto_now_add=True)

    observacion = models.TextField(blank=True)

    proveedor = models.ForeignKey(
        "logistica.Proveedor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="movimientos"
    )

    producto = models.ForeignKey(
        "catalogo.Producto",
        on_delete=models.PROTECT,
        related_name="movimientos_stock"
    )

    def __str__(self):
        return f"{self.tipo} - {self.cantidad} unidades"

class Envio(models.Model):

    ESTADO_CHOICES = [
        ("PENDIENTE", "Pendiente"),
        ("PREPARANDO", "Preparando"),
        ("EN_CAMINO", "En camino"),
        ("ENTREGADO", "Entregado"),
        ("CANCELADO", "Cancelado"),
    ]

    direccion = models.CharField(max_length=200)

    fecha_estimada = models.DateField(
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=12,
        choices=ESTADO_CHOICES,
        default="PENDIENTE"
    )

    numero_seguimiento = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )

    pedido = models.OneToOneField(
        "ventas.Pedido",
        on_delete=models.PROTECT,
        related_name="envio"
    )
    
    def __str__(self):
        return f"Envío {self.id} - {self.estado}"