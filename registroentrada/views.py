from django.core.management.commands import sql
from django.shortcuts import render
# Create your views here.
from registroentrada.models import *
from registroentrada.forms import *


def homeview(request):
    return render(request, 'home.html', '')


def form_empleado(request):
    form = RegistroIO()

    return render(request, 'form_empleado.html', {'data': form})


def landing(request):
    if request.method == 'POST':
        emp = Empleado.objects.get(id=request.POST['empleado'])
        x = Registro(empleado=emp)
        x.save()
        return render(request, 'landing.html', x)






