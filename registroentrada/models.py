from django.db import models
# Create your models here.
from django.forms import DateTimeInput

class Movimientos(models.Model):
    tipo = models.CharField(max_length=50, help_text='Tipo de movimiento')


class Empleado(models.Model):
    nombre = models.CharField(max_length=200, help_text='Tu nombre')


class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado,
                                 default=Empleado.objects.get(id=1),
                                 blank=False,
                                 choices=Empleado.objects.all().values_list('id', 'nombre'))
    fecha = models.DateTimeField(auto_now=True)
    movimiento = models.ForeignKey(Movimientos,
                                   default=Movimientos.objects.get(id=1),
                                   blank=False,
                                   choices=Movimientos.objects.all().values_list('id', 'tipo'))
    foto = models.CharField(max_length=255)


