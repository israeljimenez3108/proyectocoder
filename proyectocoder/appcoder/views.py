from django.shortcuts import render

from django.http import HttpResponse
from appcoder.models import Curso, Profesor
from appcoder.forms import ProfesorFormulario

# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html")
    
def cursos(request):
    #Obtenemos el listado de objetos en la bd
    cursos = Curso.objects.all()
    for curso in cursos:
        print(curso.nombre)
    return render(request, "appcoder/cursos.html")

def creacion_curso(request):

    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]

        curso = Curso(nombre=nombre_curso, camada=numero_camada)

        curso.save()

    return render(request, "appcoder/curso_formulario.html")

def buscar_curso(request):
    
    return render(request, "appcoder/busqueda_cursos.html")


def resultado_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]

    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "appcoder/resultados_busqueda_cursos.html",{"cursos":cursos})

    
def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")
    
def profesores(request):
    return render(request, "appcoder/profesores.html")

def creacion_profesores(request):

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        #Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data["nombre"], apellido = data["apellido"], email = data["email"], profesion = data["profesion"])

            profesor.save()
        

    formulario = ProfesorFormulario()

    contexto = {"formulario": formulario}

    return render(request, "appcoder/profesores_formulario.html", contexto)
    
def entregables(request):
    return render(request, "appcoder/entregables.html")



# def listado_cursos(request):
#     cursos = Curso.objects.all()

#     cadena_respuesta = ""

#     for curso in cursos:
#         cadena_respuesta += f"({curso.nombre}, {curso.camada})" + " | " 

#     return HttpResponse(cadena_respuesta)


