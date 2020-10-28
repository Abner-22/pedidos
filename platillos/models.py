from django.db import models
from datetime import time

# Create your models here.

class TipoPlatillo(models.Model):
    tipo = models.CharField('Tipo de platillo', max_length=50, help_text='Ej. Desayuno, Almuerzo, Cena, etc.')
    desde = models.TimeField()
    hasta = models.TimeField()


    def __str__(self):
        tipo = '{0}, desde {1} hasta {2}'
        return tipo.format(self.tipo, self.desde, self.hasta)

    class Meta:
        db_table = 'tipo_platillo'
        verbose_name = 'Tipo de platillo'
        verbose_name_plural = 'Tipos de platillos'
        unique_together = ['tipo']

class Platillo(models.Model):
    nombre = models.CharField('Nombre del platillo', max_length=50)
    tipo = models.ForeignKey(TipoPlatillo, on_delete=models.CASCADE)
    descripcion = models.TextField('Descripción')
    imagen = models.ImageField(upload_to='img/%Y/%m/%d', max_length=255, blank=True)
    precio = models.PositiveIntegerField(default=0)

    def __str__(self):
        plat = '{0} disponible desde {1} hasta {2}'
        return plat.format(self.nombre, self.tipo.desde, self.tipo.hasta)

    class Meta:
        db_table = 'platillo'
        verbose_name = 'Platillo'
        verbose_name_plural = 'Platillos'
        unique_together = ['nombre']
