from django.contrib import admin
from .models import Tecnico
from .models import Orden
from .models import Cliente
# Register your models here.

admin.site.register(Tecnico)
admin.site.register(Orden)
admin.site.register(Cliente)

