from django.contrib import admin
from .models import Usuario, Banqueteria, Cotizacion

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'tipo_usuario', 'correo')
    search_fields = ('nombre', 'apellido', 'correo')
    list_filter = ('tipo_usuario', )

class BanqueteriaAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'nombre_servicio', 'tipo_evento', 'precio_estimado', 'disponibilidad')
    search_fields = ('nombre_servicio', 'descripcion', 'direccion', 'comuna')
    list_filter = ('tipo_evento', 'proveedor')

class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'banqueteria', 'fecha_evento', 'mensaje')
    search_fields = ('cliente_nombre', 'banqueteria_nombre_servicio', 'mensaje')
    list_filter = ('cliente', 'fecha_evento')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Banqueteria, BanqueteriaAdmin)
admin.site.register(Cotizacion, CotizacionAdmin)