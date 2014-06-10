from django.contrib import admin

# Register your models here.
from registroentrada.models import Empleado, Movimientos

admin.site.register(Empleado)
admin.site.register(Movimientos)
