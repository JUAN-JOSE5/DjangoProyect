from django.contrib import admin
from .models import libro, Prestamo, ejemplar, DetallePrestamo

admin.site.register(libro)
admin.site.register(Prestamo)
admin.site.register(ejemplar)
admin.site.register(DetallePrestamo)

# Register your models here.
