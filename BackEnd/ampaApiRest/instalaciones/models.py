from django.db import models

# Create your models here.

class Instalaciones(models.Model):
    idInstalacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='instalaciones/', null=True, blank=True)

    
    class Meta:
        db_table = 'instalaciones'
        verbose_name='Instalacion'
        verbose_name_plural= 'Instalaciones'
    def __str__(self):
        return (self.nombre)