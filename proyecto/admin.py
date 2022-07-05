from django.contrib import admin

from .models import Auto, Usuario, Localidad

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Auto)
admin.site.register(Localidad)
