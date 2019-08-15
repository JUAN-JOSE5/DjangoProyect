from django.urls import path
from .views import *

urlpatterns = [
    path('cocinero/nuevo', nuevococinero),
    path('pedido/', consultarpedidos),
    path('inventario/', inventario),
    path('personal/', personal),
    path('informes/', informes),

]