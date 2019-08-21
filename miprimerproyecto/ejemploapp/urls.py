from django.urls import path, include
from .views import cargar_inicio, LibroList , LibroCreate
urlpatterns = [
    #Vista tipo funcion
    path('',cargar_inicio, name = 'inicio'),
    #Vista tipo clase
    path('libros/', LibroList.as_view(), name = 'listar_libros'),
    path('libros/nuevo/',LibroCreate.as_view(), name = 'nuevo_libro'), #Crear un formulario de una clase

    

]
