# Generated by Django 3.0 on 2020-10-15 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direcciones', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de referencia de la dirección Ej. Hogar#1.', max_length=50, verbose_name='Nombre de la cirección')),
                ('direccion', models.CharField(help_text='Dirección exacta donde recibirá el pedido.', max_length=100, verbose_name='Dirección')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente', verbose_name='Cliente')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direcciones.Municipio', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciones',
                'db_table': 'telefonesclientes',
                'unique_together': {('cliente', 'nombre')},
            },
        ),
    ]
