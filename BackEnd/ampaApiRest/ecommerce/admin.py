from django.contrib import admin
from django.contrib import admin
from .models import  Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'marca', 'descripcion', 'precio', 'stock',  'categoria','foto']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)