from django.contrib import admin
from rest_framework.exceptions import ValidationError
from .models import  Categoria, Producto, CarritoProductos,DetalleCarritoProductos
class DetalleCarritoProductosAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except ValueError as e:
            raise ValidationError({'detail': str(e)})



class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'marca', 'descripcion', 'precio', 'stock',  'categoria','foto']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(CarritoProductos)
admin.site.register(DetalleCarritoProductos, DetalleCarritoProductosAdmin)