# Generated by Django 2.1 on 2019-08-15 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemploapp', '0003_auto_20190815_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleprestamo',
            old_name='id_ejemplar',
            new_name='ejemplar',
        ),
        migrations.RenameField(
            model_name='detalleprestamo',
            old_name='id_prestamo',
            new_name='prestamo',
        ),
    ]