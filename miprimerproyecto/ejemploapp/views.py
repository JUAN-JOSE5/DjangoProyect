from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 

from .models import libro

def cargar_inicio(request):
    return render(request,"ejemploapp/index.html")

class LibroList(ListView):
    model = libro
    template_name = 'ejemploapp/lista_libros.html'

class LibroCreate(CreateView):
    model = libro
    fields = ['nombre','descripcion','ISBN','Copias']
    template_name = 'ejemploapp/nuevo_libro.html'
    success_url = reverse_lazy('listar_libros')
