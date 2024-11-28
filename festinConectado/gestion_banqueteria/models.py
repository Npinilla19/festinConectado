from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    TIPO_USUARIO = (
        ('clientes', 'Clientes'), 
        ('proveedor', 'Proveedor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO)
    

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Banqueteria(models.Model):
    TIPO_EVENTO = (
        ('matrimonio', 'Matrimonio'),
        ('cumpleaños', 'Cumpleaños'),
        ('corporativo', 'Corporativo'),
        ('licenciatura', 'Licenciatura'),
        ('otro', 'Otro'),
    )

    proveedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_servicio = models.CharField(max_length=200)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    tipo_evento = models.CharField(max_length=50)
    precio_estimado = models.FloatField()
    disponibilidad = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_servicio
 
class Cotizacion(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    banqueteria = models.ForeignKey(Banqueteria, on_delete=models.CASCADE)
    fecha_evento = models.DateTimeField()
    mensaje = models.TextField()

    def __str__(self):
        return f'Cotización para {self.banqueteria.nombre_servicio} por {self.cliente.nombre}'