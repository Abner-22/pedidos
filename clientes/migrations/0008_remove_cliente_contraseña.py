# Generated by Django 3.0 on 2020-10-28 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20201028_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='contraseña',
        ),
    ]
