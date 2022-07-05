from urllib import request
from webbrowser import get
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from proyecto.forms import FormUsuario
from proyecto.models import Auto, Localidad, Usuario


# Create your views here.

def vista_uno(request):
    return render(request, 'index.html')

def crear_usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            usuario = Usuario(
                nombre=data.get('nombre'),
                edad=data.get('edad'),
                telefono=data.get('telefono')   
            )
            usuario.save()
           
            auto = Auto(
                marca=data.get('marca'),
                año=data.get('año')   
            )
            auto.save()

            localidad = Localidad(
                provincia=data.get('provincia'),
                cp=data.get('cp')   
            )
            localidad.save()
        
            return render(request, 'listado_usuarios.html', {})
        
        else:
            return render(request, 'crear_usuario.html', {'form': form})
    
    
    form_usuario = FormUsuario()
    
    return render(request, 'crear_usuario.html', {'form':form_usuario})

def listado_usuarios(request):
    listado_usuario1= Usuario.objects.all()
    listado_autos=Auto.objects.all()
    listado_localidad=Localidad.objects.all()
    
    return render(request, 'listado_usuarios.html', {'listado_usuario1': listado_usuario1, 'listado_autos':listado_autos, 'listado_localidad':listado_localidad})



