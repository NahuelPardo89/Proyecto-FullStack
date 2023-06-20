from django.contrib import admin
from .models import Instalaciones
# Register your models here.
class InstalacionesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion','foto']


admin.site.register(Instalaciones, InstalacionesAdmin)