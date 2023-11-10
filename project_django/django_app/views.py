from django.shortcuts import render
from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola desde django")

def miEdad(request, edad):
    return HttpResponse("Hola tu edad es: %s" %edad)

def index(request):
    return render(request, 'index.html')

def alumnos(request):
    return render(request, 'Alumnos.html')

def buscar(request):
    return render(request, 'Busqueda_Alumnos.html')

def materia(request):
    return render(request, 'Materias.html')

def docente(request):
    return render(request, 'Docentes.html')

