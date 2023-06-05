from rest_framework import serializers
from .models import Instalaciones

class InstalacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instalaciones
        fields = '__all__' 