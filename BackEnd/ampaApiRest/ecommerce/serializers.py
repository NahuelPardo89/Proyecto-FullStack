from rest_framework import serializers

from .models import Producto, Categoria, DetalleCarritoProductos, CarritoProductos, Factura

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'  

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DetalleCarritoProductosSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    monto = serializers.ReadOnlyField()
    class Meta:
        model = DetalleCarritoProductos
        fields = ['producto', 'cantidad', 'monto']

class CarritoProductosSerializer(serializers.ModelSerializer):
    monto = serializers.ReadOnlyField()
    detalles = DetalleCarritoProductosSerializer(many=True, read_only=True)

    class Meta:
        model = CarritoProductos
        fields = ['usuario', 'monto', 'detalles']

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'