# Generated by Django 3.0 on 2020-10-22 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platillos', '0002_platillo'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, upload_to='img/%Y/%m/%d'),
        ),
    ]
