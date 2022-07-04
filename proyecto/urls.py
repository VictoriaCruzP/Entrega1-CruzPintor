from django.urls import path
from .views import vista_uno, un_template, fecha

urlpatterns = [
    path('', vista_uno, name='index'),
    path('mi-template/', un_template, name='mi_template'),
    path('fecha/', fecha),
]