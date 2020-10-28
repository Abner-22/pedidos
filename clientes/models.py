from datetime import datetime
from django.contrib.auth.models import User, Group
from django.db import models
from direcciones.models import Municipio

# Create your models here.

class Cliente(models.Model):
    opciones_genero = (('M', 'Masculino'), ('F', 'Femenino'), )
    usuario = models.CharField('Usuario', unique=True, max_length=50, blank=True, help_text='Nombre que utilizará para ingresar al sistema')
    contraseña = models.CharField('Contraseña', max_length=50, blank=True, help_text='Constraseña que utilizará para ingresar al sistema')
    nombres = models.CharField('Nombres', max_length=50, help_text='Ingresar solo los nombres')
    apellidos = models.CharField('Apellidos', max_length=50, help_text='Ingresar solo los apellidos')
    genero = models.CharField('Género', max_length=1, choices=opciones_genero, default='M')
    fecha_nacimiento = models.DateField('Fecha de nacimiento', help_text='Ejemplo: 01/01/1991')
    nombre_facturacion = models.CharField('Nombre de facturación', max_length=50, help_text='Nombre que saldrá en la factura')
    nit = models.CharField('NIT', max_length=11, help_text='NIT que aparecerá en la factura')
    correo = models.EmailField('Correo Electrónico', max_length=254, blank=True)
    estado = models.BooleanField('Estado', default=True)

    def __str__(self):
        nombre = '{0} {1}'
        return nombre.format(self.nombres, self.apellidos)

    def edad (self) :
        edad = int((datetime.now().date() - self.fecha_nacimiento).days / 365.25)
        return '%s años' % edad

    def creater_user(self):
        user = User(
            username=self.usuario,
            first_name=self.nombres,
            last_name=self.apellidos,
            email=self.correo,
            is_staff=True,
            is_active=True)
        user.set_password(self.contraseña)
        user.save()
        group = Group.objects.get(name='Cliente')
        user.groups.add(group)

    def save(self, **kwargs):
        try:
            user = User.objects.get(username=self.usuario)
            super(Cliente, self).save()
        except:
            self.creater_user()
            super(Cliente, self).save()

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class NumeroTelefonico(models.Model):
    opciones_tipo = (('C','Celular'),('P','Particular'),('L','Laboral'),('R','Residencial'),('O','Otro'))
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, verbose_name = 'Cliente')
    tipo = models.CharField('Tipo número telefónico', choices=opciones_tipo, max_length=1, default='C', help_text='Elegir el tipo de número telefónico. Ej. Celular')
    numero = models.PositiveIntegerField ('Número de Teléfono', help_text='Solo ingresar números')

    def __str__(self):
        return str(self.numero)

    def ClienteNombre (self) :
        return self.cliente

    class Meta:
        db_table = 'telefonosclientes'
        verbose_name = 'Número telefónico de cliente'
        verbose_name_plural = 'Agenda telefónica de clientes'
        unique_together = ['numero']

class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, verbose_name = 'Cliente')
    nombre = models.CharField('Nombre de la dirección', max_length=50, help_text='Nombre de referencia de la dirección Ej. Hogar#1.')
    calle = models.CharField('Calle', max_length=2, help_text='Solo ingresar el número de calle', blank=True)
    avenida = models.CharField('Avenida', max_length=2, help_text='Solo ingresar el número de avenida', blank=True)
    colonia = models.CharField('Colonia', max_length=30, help_text='Nombre de la colonia', blank=True)
    barrio = models.CharField('Barrio', max_length=30, help_text='Nombre del barrio', blank=True)
    residencial = models.CharField('Residencial', max_length=30, help_text='Nombre del residencial', blank=True)
    manzana = models.CharField('Manzana', max_length=2, blank=True)
    lote = models.CharField('Lote', max_length=3, help_text='Solo ingresar el número de lote', blank=True)
    numero_casa = models.CharField('Número de Casa', max_length=5, help_text='Ej. 4-10, 10-52, etc.', blank=True)
    zona = models.CharField('Zona', max_length=30, help_text='Nombre del barrio', blank=True)
    municipio = models.ForeignKey(Municipio, on_delete = models.CASCADE, verbose_name = 'Municipio')
    direccion = models.CharField('Dirección', max_length=100, help_text='Dirección exacta donde recibirá el pedido.')
    estado = models.BooleanField('Estado', default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'direccionclientes'
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'
        unique_together = ['cliente', 'nombre']
