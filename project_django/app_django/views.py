from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    mensaje = "¡Hola, bienvenido a mi sitio web!"
    return HttpResponse(mensaje)

