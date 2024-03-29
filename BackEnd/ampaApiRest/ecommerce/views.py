from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from rest_framework import viewsets,permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Producto, Categoria,CarritoProductos, DetalleCarritoProductos, Factura
from .serializers import CategoriaSerializer, ProductoSerializer, CarritoProductosSerializer, DetalleCarritoProductosSerializer,FacturaSerializer, FacturaSerializer2
from usuarios.models import Usuario

#Permisos de solo lectura a menos que sea admin
class IsAdminOrReadOnly(permissions.BasePermission):
  
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or \
           (request.user and request.user.is_staff):
            return True
        return False


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly ]
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly ]
    serializer_class = ProductoSerializer

class CarritoProductosViewSet(viewsets.ModelViewSet):
    queryset = CarritoProductos.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CategoriaSerializer
    serializer_class = CarritoProductosSerializer
    def retrieve(self, request, *args, **kwargs):
        usuario_id = kwargs.get('pk')
        queryset = CarritoProductos.objects.filter(usuario_id=usuario_id)
        carrito = get_object_or_404(queryset)
        serializer = self.get_serializer(carrito)
        
        return Response(serializer.data)
    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            Prefetch('detalles', queryset=DetalleCarritoProductos.objects.select_related('producto'))
        )


class DetalleCarritoProductosViewSet(viewsets.ModelViewSet):
    queryset = DetalleCarritoProductos.objects.select_related('producto', 'carrito')
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = DetalleCarritoProductosSerializer
    

    def create(self, request, *args, **kwargs):
        producto_id = request.data.get('producto')
        cantidad = request.data.get('cantidad')
        usuario_id = request.data.get('usuario')
        print(request.data)

        usuario = Usuario.objects.filter(id=usuario_id).first()
        if not usuario:
            return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        carrito, created = CarritoProductos.objects.get_or_create(usuario=usuario)
        if created:
            carrito.save()

        if not producto_id or not cantidad:
            return Response({"detail": "Producto y cantidad son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        producto = Producto.objects.filter(id=producto_id).first()
        if not producto:
            return Response({"detail": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if producto.stock < cantidad:
            return Response({"detail": "Stock insuficiente para este producto"}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(carrito=carrito)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        detalle = self.get_object()
        cantidad = request.data.get('cantidad')

        if cantidad and detalle.producto.stock < cantidad:
            return Response({"detail": "Stock insuficiente para este producto"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            return super().update(request, *args, **kwargs)
        except ValueError as e:
            raise ValidationError({'detail': str(e)})

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = FacturaSerializer2
    @action(detail=False, methods=['get'], url_path='usuario/(?P<usuario_id>\d+)')
    def get_facturas_por_usuario(self, request, usuario_id=None):
        print(request.data)
        try:
            user = Usuario.objects.get(id=usuario_id)
            
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=404)
        facturas = Factura.objects.filter(carrito__usuario=user)
        serializer = FacturaSerializer2(facturas, many=True)
        return Response(serializer.data)

class PagoViewSet(viewsets.ViewSet):

    def create(self, request):
        # Simula el proceso de pago
        
        
        usuario_id = request.data.get('usuario')
        
        carrito = CarritoProductos.objects.filter(usuario_id=usuario_id).first()
        print(carrito)
        
        if not carrito:
            return Response({"detail": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        

        
        factura_data = {
            'carrito': carrito.id,
            'subtotal': carrito.monto,
            'total': carrito.monto,
            'estado':'PA'  
        }

        factura_serializer = FacturaSerializer(data=factura_data)
        if factura_serializer.is_valid():
            factura_serializer.save()
            

            # Actualiza el stock del producto.
            for detalle in carrito.detalles.all():
                producto = detalle.producto
                producto.stock -= detalle.cantidad
                producto.save()
            carrito.detalles.all().delete()
            return Response(factura_serializer.data, status=status.HTTP_201_CREATED)

        return Response(factura_serializer.errors, status=status.HTTP_400_BAD_REQUEST)