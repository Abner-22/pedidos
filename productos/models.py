from django.db import models

# Create your models here.
class TamañoBebida(models.Model):
    tamaño = models.CharField('Tamaño de bedido', max_length=50, help_text='Ej. Pequeña, Mediana, Grande, etc.')
    descripcion = models.CharField('Descripción', max_length=10, help_text='Ej. 360 ml, 600 ml, 1 litro, etc.')

    def __str__(self):
        tam = '{0} {1}'
        return tam.format(self.tamaño, self.descripcion)

    class Meta:
        db_table = 'tamaño_bebida'
        verbose_name = 'Tamaño de bebida'
        verbose_name_plural = 'Tamaños de bebidas'
        unique_together = ['tamaño', 'descripcion']

class Bebidas(models.Model):
    nombre = models.CharField('Nombre de la bebida', max_length=50, help_text='Refresco de tamarindo, refresco de jamaica, coca-cola, seven up, etc.')
    tamaño = models.ForeignKey(TamañoBebida, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img/%Y/%m/%d', max_length=255, blank=True)
    precio = models.PositiveIntegerField(default=0)

    def __str__(self):
        bebida = '{0} - {1} ({2})'
        return bebida.format(self.nombre, self.tamaño.tamaño, self.tamaño.descripcion)

    class Meta:
        db_table = 'bebida'
        verbose_name = 'Bebida'
        verbose_name_plural = 'Bebidas'
        unique_together = ['nombre', 'tamaño']
