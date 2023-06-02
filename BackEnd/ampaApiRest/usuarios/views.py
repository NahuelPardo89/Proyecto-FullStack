

from rest_framework import viewsets
from .models import Usuario

from rest_framework import generics, permissions

from rest_framework.response import Response
from .serializers import UsuarioSerializer, RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UsuarioSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UsuarioSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

# Logout API
class LogoutAPI(generics.GenericAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "No se proporcionó token de actualización"}, status=400)

            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=204)

        except Exception as e:
            return Response({"error": str(e)}, status=400)