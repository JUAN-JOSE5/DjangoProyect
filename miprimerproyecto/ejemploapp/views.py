from django.shortcuts import render
from django.http import HttpResponse

# Create your views here(crea tu vista aqui).

def saludar(request):
    respuesta="<ul>"
    respuesta= respuesta + "<li> elemento 1 </i>"
    respuesta= respuesta + "<li> elemento 2 </i>"
    respuesta= respuesta + "<li> elemento 3 </i>"
    respuesta= respuesta + "</u>"

    return HttpResponse(respuesta)

def nuevococinero(request):

    return HttpResponse("<p>Esta es la pagian de nuevo cocinero</p>")

def consultarpedidos(request):
    
    return HttpResponse("<p>Consultar pedidos</p>")

def inventario(request):
    
    return HttpResponse("<p>Revisar Inventarios</p>")

def personal(request):
    
    return HttpResponse("<p>Verificar personal activo</p>")

def informes(request):
    
    return HttpResponse("<p>Consultar informes diarios</p>")