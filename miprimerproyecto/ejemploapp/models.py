from django.db import models

# Create your models here.(crea tu modelo aqui)
class libro (models.Model):
    nombre=models.CharField(max_length=45)
    descripcion=models.CharField(max_length=45)
    ISBN=models.CharField(max_length=45)
    Copias=models.IntegerField()
class Prestamo(models.Model):
    Fechaprestamo=models.DateField("Fecha de prestamo",max_length=45)
    nombrecliente=models.CharField("Nombre del cliente",max_length=45)
    telefonocliente=models.CharField("Telefono cliente",max_length=45)
    estado=models.BooleanField()
class ejemplar(models.Model):
    numeroejemplar=models.CharField("Numero ejemplar",max_length=45)
    fechadecompra=models.DateField("Fecha de compra",max_length=45)
    libro=models.ForeignKey(libro,on_delete=models.CASCADE)
class DetallePrestamo(models.Model):
    prestamo=models.ForeignKey(Prestamo,on_delete=models.CASCADE)
    ejemplar=models.ForeignKey(ejemplar,on_delete=models.CASCADE)
