
from .models import Usuario
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.db import IntegrityError

# User Serializer
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'dni', 'nombre', 'apellido', 'email', 'telefono', 'direccion')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('dni', 'nombre', 'apellido', 'email', 'telefono', 'direccion', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = Usuario.objects.create_user(
                dni=validated_data['dni'], 
                password=validated_data['password'],
                nombre=validated_data['nombre'], 
                apellido=validated_data['apellido'],
                email=validated_data['email'], 
                telefono=validated_data['telefono'], 
                direccion=validated_data['direccion']
            )
            return user
        except IntegrityError:
            raise serializers.ValidationError("Un usuario con este DNI o correo electrónico ya existe.")

# Login Serializer
class LoginSerializer(serializers.Serializer):
    dni = serializers.IntegerField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data.get('dni'), password=data.get('password'))
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Usuario o contraseña incorrecto")
