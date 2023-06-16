from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ReservasViewSet


router = DefaultRouter()
router.register(r'reservas', ReservasViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('reservas/list_all/', ReservasViewSet.as_view({'get': 'list_all_reservas'}), name='reservas-list-all'),
]
