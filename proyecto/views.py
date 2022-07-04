from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.shortcuts import render
from .models import Edad, Nombre, Telefono


# Create your views here.

def vista_uno(request):
    return HttpResponse('<h1>Mi Blog</h1>')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha : {fecha_actual}')

def un_template(request, nombre_admin, edad_admin, telefono_admin):
    
    
    nombre = Nombre (nombre = nombre_admin)
    nombre.save()
    edad = Edad (edad= edad_admin)
    edad.save()
    telefono = Telefono (telefono= telefono_admin)
    telefono.save()
   
    return render(request, 'index.html', {'lista_objeto': [nombre, edad, telefono]})

