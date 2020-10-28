from django.db import models

# Create your models here.

class Postre(models.Model):
    nombre = models.CharField('Nombre del postre', max_length=50)
    descripcion = models.TextField('Descripción')
    imagen = models.ImageField(upload_to='img/%Y/%m/%d', max_length=255, blank=True)
    precio = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'postre'
        verbose_name = 'Postre'
        verbose_name_plural = 'Postres'
        unique_together = ['nombre']
