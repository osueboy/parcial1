from django.forms import *
from registroentrada.models import *


class RegistroIO(ModelForm):

    class Meta:
        model = Registro
        fields = ['empleado']




