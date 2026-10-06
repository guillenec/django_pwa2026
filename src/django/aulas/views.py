from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def nuevoHello(request):
    return HttpResponse("Hola mundo desde Django!");

def bye(request):
    return HttpResponse("Chau desde Django!");

def edad(request, anios):
    mensaje = f"Tienes {anios} años!";
    return HttpResponse(mensaje);

def cumpleanios(request, anios, futuro):
    incremebnto = futuro - datetime.now().year;
    mensaje = f"En {futuro} tendrás {anios + incremebnto} años!";
    return HttpResponse(mensaje);