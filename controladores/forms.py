from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    comision = forms.IntegerField(required=True, max_value=99999)
    
class EstudianteFormulario (forms.Form):
    nombre = forms.CharField(required=True,max_length=256)
    apellido = forms.CharField(max_length=256)
    email = forms.EmailField(required=True)
    dni = forms.CharField(max_length=32)
    telefono = forms.CharField(max_length=20)
    nacimiento = forms.DateField(required=False)
 
class ProfesorFormulario (forms.Form):
    nombre = forms.CharField(required=True,max_length=256)
    apellido = forms.CharField(max_length=256)
    email = forms.EmailField(required=True)
    dni = forms.CharField(max_length=32)
    telefono = forms.CharField(max_length=20)
    nacimiento = forms.DateField(required=False)
    profesion = forms.CharField(max_length=128, required=False)
    bio = forms.CharField(max_length=512, required=False)