from django.contrib import admin
from .models import Reserva
# Register your models here.

class ReservasAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'instalaciones', 'costo','fecha', 'hora']

admin.site.register(Reserva, ReservasAdmin)
