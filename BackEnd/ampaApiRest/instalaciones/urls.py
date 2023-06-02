from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import InstalacionesViewSet


router = DefaultRouter()
router.register(r'instalaciones', InstalacionesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
