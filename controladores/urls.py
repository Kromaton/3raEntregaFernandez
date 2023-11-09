from django.urls import path
from controladores.views import (lista_estudiantes, lista_cursos, lista_profesores,
                                 crear_curso, crear_estudiante, crear_profesor,
                                 buscar_cursos, buscar_estudiantes, buscar_profesores)

# URLs del la app
urlpatterns = [
    path('estudiantes/',        lista_estudiantes,  name="lista_estudiantes"),
    path('cursos/',             lista_cursos,       name="lista_cursos"),
    path('profesores/',         lista_profesores,   name="lista_profesores"),
    
    path('crear-cursos/',       crear_curso,        name="crear_curso"),
    path('crear-estudiantes/',  crear_estudiante,   name="crear_estudiante"),
    path('crear-profesores/',   crear_profesor,     name="crear_profesor"),
    
    path('buscar-cursos/',      buscar_cursos,      name='buscar_cursos'),
    path('buscar-estudiantes/', buscar_estudiantes, name='buscar_estudiantes'),
    path('buscar-profesores/',  buscar_profesores,  name='buscar_profesores'),
]