

from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer, RegisterSerializer, LoginSerializer

# Vista para administrador
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UsuarioSerializer

#vista perfil usuario
class UserPerfilView(generics.RetrieveUpdateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return self.request.user

    @action(detail=False, methods=['post'])
    def cambiar_contrasena(self, request, pk=None):
        user = self.get_object()
        old_password = request.data.get("old_password")
        if not user.check_password(old_password):
            return Response({"old_password": ["Contraseña incorrecta."]}, status=status.HTTP_400_BAD_REQUEST)
        new_password = request.data.get("new_password")
        new_password2 = request.data.get("new_password2")
        if new_password != new_password2:
            return Response({"new_password": ["Las dos contraseñas no coinciden."]}, status=status.HTTP_400_BAD_REQUEST)
        try:
            password_validation.validate_password(new_password, user)
        except forms.ValidationError as error:
            return Response({"new_password": list(error)}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
        },status=status.HTTP_201_CREATED)

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": UsuarioSerializer(user, context=self.get_serializer_context()).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        else:
            print('Serializer errors:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout API
class LogoutAPI(generics.GenericAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        
        try:
            refresh_token = request.data.get("refresh")
            
            if not refresh_token:
                return Response({"error": "No se proporcionó token de actualización"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=204)

        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=400)