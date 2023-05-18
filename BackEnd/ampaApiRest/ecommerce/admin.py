from django.contrib import admin
from django.contrib import admin
from .models import Proveedor, Categoria, Producto

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['idProveedor', 'nombre', 'empresa', 'telefono']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['idProducto', 'nombre', 'marca', 'descripcion', 'precio', 'stock', 'proveedor', 'categoria']

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)