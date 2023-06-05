from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CategoriaViewSet,CarritoProductosViewSet, DetalleCarritoProductosViewSet,FacturaViewSet, PagoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'carritos', CarritoProductosViewSet)
router.register(r'detalles-carrito', DetalleCarritoProductosViewSet)
router.register(r'factura', FacturaViewSet)
router.register(r'pagos', PagoViewSet, basename='pagos')
urlpatterns = [
    path('', include(router.urls)),
]