from django.shortcuts import render

# Views del projecto

def inicio (request):
    contexto = {
        "nav" : "index",
    }
    http_response = render(
        request = request,
        template_name = 'inicio.html',
        context = contexto,
    )
    return http_response

def prueba (request):
    contexto = {
        "nav" : "prueba",
    }
    http_response = render(
        request = request,
        template_name = 'prueba.html',
        context = contexto,
    )
    return http_response