from django import forms

class FormUsuario(forms.Form):
    nombre=forms.CharField(max_length=100)
    edad=forms.IntegerField()
    telefono=forms.IntegerField()
    marca=forms.CharField(max_length=100)
    año=forms.IntegerField()
    provincia=forms.CharField(max_length=100)
    cp=forms.IntegerField()
    