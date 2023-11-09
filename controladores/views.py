from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from controladores.models import Curso, Profesor, Estudiante
from controladores.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario


########## Views de la app ###########

######################################## LISTAS ###############################################

def lista_estudiantes (request):
    contexto = {
        "nav" : "estudiantes",
        "Estudiantes" : Estudiante.objects.all()
    }
    http_response = render (
        request =  request,
        template_name = "controladores/lista_estudiantes.html",
        context = contexto
    )
    return http_response

def lista_cursos (request):
    contexto = {
        "nav" : "cursos",
        "Cursos" : Curso.objects.all(),
    }
    http_response = render (
        request =  request,
        template_name = "controladores/lista_cursos.html",
        context = contexto,
    )
    return http_response

def lista_profesores (request):
    contexto = {
        "nav" : "profesores",
        "Profesores" : Profesor.objects.all()
    }
    http_response = render (
        request =  request,
        template_name = "controladores/lista_profesores.html",
        context = contexto
    )
    return http_response

######################################## CREAR ###############################################

def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            comision = data["comision"]
            curso = Curso(curso_name=nombre, curso_comision=comision)
            curso.save()
            url_exitosa = reverse('lista_cursos')
            return redirect(url_exitosa)
    else:
        formulario = CursoFormulario()
    http_response = render(
        request=request,
        template_name='controladores/formulario_curso.html',
        context={'formulario':formulario},
    )
    return http_response
 
def crear_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            email = data["email"]
            dni = data["dni"]
            telefono = data["telefono"]
            nacimiento = data["nacimiento"]
            estudiante = Estudiante(estudiante_name=nombre,estudiante_lastname=apellido, estudiante_email=email, estudiante_dni=dni, estudiante_phone=telefono, estudiante_birth=nacimiento)
            estudiante.save()
            url_exitosa = reverse('lista_estudiantes')
            return redirect(url_exitosa)
    else: 
        formulario = EstudianteFormulario()
    http_response = render(
        request=request,
        template_name='controladores/formulario_estudiante.html',
        context={'formulario':formulario},
    )
    return http_response

def crear_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            email = data["email"]
            dni = data["dni"]
            telefono = data["telefono"]
            nacimiento = data["nacimiento"]
            profesion = data["profesion"]
            bio = data["bio"]
            profesor = Profesor(profesor_name=nombre,profesor_lastname=apellido, profesor_email=email, profesor_dni=dni, profesor_phone=telefono, profesor_birth=nacimiento, profesor_profesion=profesion, profesor_bio=bio)
            profesor.save()
            url_exitosa = reverse('lista_profesores')
            return redirect(url_exitosa)
    else: 
        formulario = ProfesorFormulario()
    http_response = render(
        request=request,
        template_name='controladores/formulario_profesor.html',
        context={'formulario':formulario},
    )
    return http_response

######################################## BUSCAR ###############################################

def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos = Curso.objects.filter(
            Q(curso_name__contains=busqueda) | Q(curso_comision__contains=busqueda)
        )
        contexto = {
            "nav" : "cursos",
            "Cursos" : cursos,
        }
        http_response = render (
            request = request,
            template_name = 'controladores/lista_cursos.html',
            context = contexto,
        )
        return http_response
    
def buscar_estudiantes(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        estudiantes = Estudiante.objects.filter(
            Q(estudiante_name__contains=busqueda) | Q(estudiante_lastname__contains=busqueda)
        )
        contexto = {
            "nav" : "estudiantes",
            "Estudiantes" : estudiantes,
        }
        http_response = render (
            request = request,
            template_name = 'controladores/lista_estudiantes.html',
            context = contexto,
        )
        return http_response
    
def buscar_profesores(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        profesores = Profesor.objects.filter(
            Q(profesor_name__contains=busqueda) | Q(profesor_lastname__contains=busqueda)
        )
        contexto = {
            "nav" : "profesor",
            "Profesores" : profesores,
        }
        http_response = render (
            request = request,
            template_name = 'controladores/lista_profesores.html',
            context = contexto,
        )
        return http_response