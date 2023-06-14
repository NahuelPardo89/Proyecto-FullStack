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
    