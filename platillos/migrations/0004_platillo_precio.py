# Generated by Django 3.0 on 2020-10-22 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platillos', '0003_platillo_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='precio',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
