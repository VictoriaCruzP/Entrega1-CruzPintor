from django.urls import path
from .views import crear_usuario, listado_usuarios, vista_uno

urlpatterns = [
    path('', vista_uno, name='index'),
    path('listado_usuarios/', listado_usuarios, name='listado_usuarios'),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),
]