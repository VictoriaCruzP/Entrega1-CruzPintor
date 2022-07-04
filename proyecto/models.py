from django.db import models

# Create your models here.
class Nombre(models.Model):
    nombre=models.CharField(max_length=100)
   
    
class Edad(models.Model):
    edad=models.IntegerField()
    
class Telefono(models.Model):
    telefono=models.IntegerField()      