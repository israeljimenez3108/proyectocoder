from django.shortcuts import render

from django.http import HttpResponse
from appcoder.models import Curso

# Create your views here.

def inicio(request):
    return HttpResponse("Estas en el inicio")

def cursos(request):
    return HttpResponse("Estas en cursos")

def estudiantes(request):
    return HttpResponse("Estas en estudiantes")

def profesores(request):
    return HttpResponse("Estas en profesores")

def entregables(request):
    return HttpResponse("Estas en entregables")

# def listado_cursos(request):
#     cursos = Curso.objects.all()

#     cadena_respuesta = ""

#     for curso in cursos:
#         cadena_respuesta += f"({curso.nombre}, {curso.camada})" + " | " 

#     return HttpResponse(cadena_respuesta)


