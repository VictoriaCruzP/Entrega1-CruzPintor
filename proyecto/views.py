from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.shortcuts import render
from proyecto.models import Edad, Nombre, Telefono


# Create your views here.

def vista_uno(request):
    return render(request, 'index.html')
def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha : {fecha_actual}')

def un_template(request):
    
    
    nombre = Nombre (nombre = 'Victoria')
    nombre.save()
    edad = Edad (edad= 28)
    edad.save()
    telefono = Telefono (telefono= 611150440)
    telefono.save()
   
    return render(request, 'mi_template.html', {'lista_objeto': [nombre, edad, telefono]})

