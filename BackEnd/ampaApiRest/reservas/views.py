from django.shortcuts import render
from .serializers import ReservasSerializer
from .models import Reserva
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets,permissions
# Create your views here.

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer
    
    def get_queryset(self):
        queryset = Reserva.objects.all()
        usuario = self.request.query_params.get('usuario')
        if usuario is not None:
            queryset = queryset.filter(usuario=usuario)
        return queryset