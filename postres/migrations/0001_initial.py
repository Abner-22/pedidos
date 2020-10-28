# Generated by Django 3.0 on 2020-10-22 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del postre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('imagen', models.ImageField(blank=True, max_length=255, upload_to='img/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Postre',
                'verbose_name_plural': 'Postres',
                'db_table': 'postre',
                'unique_together': {('nombre',)},
            },
        ),
    ]