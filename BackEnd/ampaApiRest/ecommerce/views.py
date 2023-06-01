from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Producto, Categoria,CarritoProductos, DetalleCarritoProductos
from .serializers import CategoriaSerializer, ProductoSerializer, CarritoProductosSerializer, DetalleCarritoProductosSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CarritoProductosViewSet(viewsets.ModelViewSet):
    queryset = CarritoProductos.objects.all()
    serializer_class = CarritoProductosSerializer

    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            Prefetch('detalles', queryset=DetalleCarritoProductos.objects.select_related('producto'))
        )


class DetalleCarritoProductosViewSet(viewsets.ModelViewSet):
    queryset = DetalleCarritoProductos.objects.select_related('producto', 'carrito')
    serializer_class = DetalleCarritoProductosSerializer

    def create(self, request, *args, **kwargs):
        producto_id = request.data.get('producto')
        cantidad = request.data.get('cantidad')

        if not producto_id or not cantidad:
            return Response({"detail": "Producto y cantidad son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        producto = Producto.objects.filter(id=producto_id).first()
        if not producto:
            return Response({"detail": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if producto.stock < cantidad:
            return Response({"detail": "Stock insuficiente para este producto"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        detalle = self.get_object()
        cantidad = request.data.get('cantidad')

        if cantidad and detalle.producto.stock < cantidad:
            return Response({"detail": "Stock insuficiente para este producto"}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)