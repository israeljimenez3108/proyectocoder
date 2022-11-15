from django.http import HttpResponse
from django.template import Template, Context, loader

from datetime import datetime

def vista_saludo(request):
    return HttpResponse("""
    <h1>Hola coders! :) </h1>
    <p style='color:red' >Esto es una prueba </p>
    """)


def iniciar_sesion(request):
    return HttpResponse("Pásame tu username y password por WhatsApp ;) ")


def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenid@ {nombre}"

    return HttpResponse(respuesta)

def nacimiento(request, edad):

    fecha = datetime.now().year - int(edad)

    respuesta = f"Tu año de nacimiento es: {fecha}"

    return HttpResponse(respuesta)

def vista_plantilla(request):
    #Abrimos el archivo
    archivo = open(r"C:/Coder/Python/Django/proyectocoder/proyectocoder/templates/plantilla_bonita.html")

    #Creamos el objeto plantilla
    plantilla = Template(archivo.read())

    #Cerramos el archivo
    archivo.close()

    #Diccionario con datos para la plantilla
    datos = {"nombre": "Leonel", "fecha": datetime.now(), "apellido":"Gareis"}

    #Creamos el contexto
    contexto = Context(datos)

    #Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    #Retornamos la respuetsa
    return HttpResponse(documento)


def vista_listado_alumnos(request):
    
    #Abrimos el archivo
    archivo = open(r"C:/Coder/Python/Django/proyectocoder/proyectocoder/templates/listado_alumnos.html")

    #Creamos el template
    plantilla = Template(archivo.read())

    #Cerramos el archivo
    archivo.close()

    #Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Israel Jimenez", "Anabel Martinez", "Susana Franco", "Omar Guadarrama"]

    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    #Creamos el contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)
    
    #Retornamos
    return HttpResponse(documento)


def vista_listado_alumnos2(request):
    #Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Israel Jimenez", "Anabel Martinez", "Susana Franco", "Omar Guadarrama"]

    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)