# Generated by Django 2.1 on 2019-08-15 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemploapp', '0006_auto_20190815_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='copiar',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='Fechaprestamo',
            field=models.DateField(max_length=45, verbose_name='Fecha de prestamo'),
        ),
    ]
