from django.contrib import admin

from proyecto.models import Edad, Nombre, Telefono

# Register your models here.

admin.site.register(Nombre)
admin.site.register(Edad)
admin.site.register(Telefono)
