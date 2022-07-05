from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=100)
    edad=models.IntegerField()
    telefono=models.IntegerField()
    marca=models.CharField(max_length=100)
    año=models.IntegerField()
    provincia=models.CharField(max_length=100)
    cp=models.IntegerField() 