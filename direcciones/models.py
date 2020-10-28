from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField('Nombre del Departamento', max_length=50, help_text='Ejemplo: Chiquimula, Zacapa, entre otros.')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        unique_together = ['nombre'] #no puede existir otro departamento con el mismo nombre

class Municipio(models.Model):
    nombre = models.CharField('Nombre del Municipio', max_length=50, help_text='Ejemplo: Chiquimula, Esquipulas, Quezaltepeque, etc.')
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)

    def __str__(self):
        cadena = '{}, {}'
        return cadena.format(self.nombre, self.departamento)

    class Meta:
        db_table = 'municipio'
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        unique_together = [('nombre','departamento'),] #no puede existir otro municipio con el mismo nombre
