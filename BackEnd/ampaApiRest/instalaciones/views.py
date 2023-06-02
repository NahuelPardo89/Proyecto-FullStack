from django.shortcuts import render
from .serializers import InstalacionesSerializer
from .models import Instalaciones
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


# Create your views here.

class InstalacionesViewSet(viewsets.ModelViewSet):
    queryset = Instalaciones.objects.all()
    serializer_class = InstalacionesSerializer