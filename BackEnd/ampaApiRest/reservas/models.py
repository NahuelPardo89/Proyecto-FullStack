from django.db import models
from usuarios.models import Usuario
from instalaciones.models import Instalaciones


# Create your models here.


#Modelo de reservas
class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    fechaHora = models.DateTimeField(null=False, blank=False)
    costo = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas_usuario')
    instalaciones = models.ForeignKey(Instalaciones, on_delete=models.CASCADE, related_name='instalaciones_usuario')
    
    def __str__(self):
        return f'Reservas de {self.usuario}'
    
    @property
    def costo(self):
        # Obtener el costo de la instalación relacionada
        costo_instalacion = self.instalaciones.costo

        return costo_instalacion

    #Metadata
    class Meta:
        db_table = 'reserva'
        verbose_name='Reserva'
        verbose_name_plural= 'Reservas'
