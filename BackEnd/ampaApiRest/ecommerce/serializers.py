from rest_framework import serializers

from .models import Producto, Categoria, DetalleCarritoProductos, CarritoProductos, Factura
from usuarios.serializers import UsuarioShortSerializer
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'  

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DetalleCarritoProductosSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    carrito = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = DetalleCarritoProductos
        fields = ['id','producto', 'cantidad',  'carrito', 'monto']

class CarritoProductosSerializer(serializers.ModelSerializer):
    usuario= UsuarioShortSerializer()
    monto = serializers.ReadOnlyField()
    detalles = DetalleCarritoProductosSerializer(many=True, read_only=True)

    class Meta:
        model = CarritoProductos
        fields = ['usuario',  'detalles', 'monto']

class FacturaSerializer(serializers.ModelSerializer):
    carrito=CarritoProductosSerializer()
    class Meta:
        model = Factura
        fields = '__all__'