from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CategoriaViewSet,CarritoProductosViewSet, DetalleCarritoProductosViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'carritos', CarritoProductosViewSet)
router.register(r'detalles-carrito', DetalleCarritoProductosViewSet)
urlpatterns = [
    path('', include(router.urls)),
]