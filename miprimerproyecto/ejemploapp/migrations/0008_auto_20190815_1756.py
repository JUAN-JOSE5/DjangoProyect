# Generated by Django 2.1 on 2019-08-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemploapp', '0007_auto_20190815_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='fechadecompra',
            field=models.DateField(max_length=45, verbose_name='Fecha de compra'),
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='numeroejemplar',
            field=models.CharField(max_length=45, verbose_name='Numero ejemplar'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='nombrecliente',
            field=models.CharField(max_length=45, verbose_name='Nombre del cliente'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='telefonocliente',
            field=models.CharField(max_length=45, verbose_name='Telefono cliente'),
        ),
    ]
