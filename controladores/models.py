from django.db import models

# Create your models here.

class Curso (models.Model):
    curso_name = models.CharField(max_length=64)
    curso_comision = models.IntegerField()
    
    def __str__(self):
        return f"{self.curso_name} ({self.curso_comision})"
    
class Estudiante (models.Model):
    estudiante_name = models.CharField(max_length=256)
    estudiante_lastname = models.CharField(max_length=256)
    estudiante_email = models.EmailField(blank=True)
    estudiante_dni = models.CharField(max_length=32)
    estudiante_phone = models.CharField(max_length=20, blank=True, null=True)
    estudiante_birth = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.estudiante_lastname}, {self.estudiante_name}"
    
class Profesor (models.Model):
    profesor_name = models.CharField(max_length=256)
    profesor_lastname = models.CharField(max_length=256)
    profesor_email = models.EmailField(blank=True)
    profesor_dni = models.CharField(max_length=32)
    profesor_phone = models.CharField(max_length=20, blank=True, null=True)
    profesor_birth = models.DateField(null=True)
    profesor_profesion = models.CharField(max_length=128)
    profesor_bio = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.profesor_lastname}, {self.profesor_name}"