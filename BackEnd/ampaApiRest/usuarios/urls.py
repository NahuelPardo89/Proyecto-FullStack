from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RegisterAPI, LoginAPI, LogoutAPI
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from .views import UsuarioViewSet, RegisterAPI, LoginAPI, LogoutAPI, UserPerfilView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('perfil/', UserPerfilView.as_view(), name='perfil'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]