from django.db import models
from usuarios.models import Usuario
from instalaciones.models import Instalaciones

# Create your models here.

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField(default='08:00')
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=1500)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas_usuario')
    instalaciones = models.ForeignKey(Instalaciones, on_delete=models.CASCADE, related_name='instalaciones_usuario')
    
    def __str__(self):
        return f'Reservas de {self.usuario}'

    
    # Metadata
    class Meta:
        db_table = 'reserva'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
