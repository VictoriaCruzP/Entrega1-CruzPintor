from urllib import request
from webbrowser import get
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from proyecto.forms import FormUsuario
from proyecto.models import Usuario


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
                telefono=data.get('telefono'),
                marca=data.get('marca'),
                año=data.get('año'),
                provincia=data.get('provincia'),
                cp=data.get('cp'),
            )
            usuario.save()
           
        
            return render(request, 'listado_usuarios.html', {})
        
        else:
            return render(request, 'crear_usuario.html', {'form': form})
    
    
    form_usuario = FormUsuario()
    
    return render(request, 'crear_usuario.html', {'form':form_usuario})

def listado_usuarios(request):
    listado_usuario1= Usuario.objects.all()
    
    return render(request, 'listado_usuarios.html', {'listado_usuario1': listado_usuario1})



