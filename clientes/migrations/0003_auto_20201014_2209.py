# Generated by Django 3.0 on 2020-10-15 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_direccion'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='direccion',
            table='direccionclientes',
        ),
    ]