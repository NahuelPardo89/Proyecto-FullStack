from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['dni', 'nombre', 'apellido', 'telefono', 'direccion', 'is_active', 'is_staff']