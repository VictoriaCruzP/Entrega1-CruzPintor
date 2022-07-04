from django.urls import path
from .views import vista_uno, un_template, fecha

urlpatterns = [
    path('', vista_uno),
    path('mi-template/<nombre_admin>/<edad_admin>/<telefono_admin>', un_template),
    path('fecha/', fecha),
]