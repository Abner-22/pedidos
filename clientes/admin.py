from django.contrib import admin
from clientes.models import Cliente, NumeroTelefonico, Direccion

# Register your models here.

class TelefonoCliente(admin.TabularInline):
    model = NumeroTelefonico
    extra = 0

class DireccionCliente(admin.StackedInline):
    model = Direccion
    extra = 0

class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefonoCliente, DireccionCliente]
    readonly_fields = ['estado']
    search_fields = ['nombres', 'apellidos']
    list_filter = ['genero', 'estado']
    fieldsets = (
        ('Datos de Acceso al Sistema', {
            'fields': (('usuario', 'contraseña'))
        }),
        ('Datos Personales', {
            'fields': (('nombres', 'apellidos'), ('genero','fecha_nacimiento'), 'correo','estado')
        }),
        ('Datos de Facturación', {
            #'classes': ('collapse',), #Menú desplegable
            'fields': ('nit', 'nombre_facturacion'),
        }),
    )
    list_display = ['nombres', 'apellidos', 'edad', 'nit','estado']
    ordering = ['nombres'] #visualizaremos los datos ordenados por nombres
    #autocomplete_fields = ['municipio',]

class TelefonoAdmin(admin.ModelAdmin):
    search_fields = ['cliente__nombres', 'cliente__apellidos', 'numero','tipo']
    list_filter = ['tipo']
    list_display = ['cliente', 'tipo', 'numero']
    autocomplete_fields = ['cliente']

class DireccionAdmin(admin.ModelAdmin):
    search_fields = ['cliente__nombres', 'cliente__apellidos', 'nombre']
    list_filter = ['estado', 'municipio__departamento']
    list_display = ['cliente', 'nombre', 'municipio', 'direccion', 'estado']
    autocomplete_fields = ['cliente']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(NumeroTelefonico, TelefonoAdmin)
admin.site.register(Direccion, DireccionAdmin)
