from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'Categoria'
        verbose_name='Categoria'
        verbose_name_plural= 'Categorias'
    def __str__(self):
        return (self.nombre)
        
class Producto(models.Model):
    nombre = models.CharField(max_length=50,null=False, blank=False)
    marca = models.CharField(max_length=50,null=False, blank=False)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    foto = models.ImageField(upload_to='assets/img/productos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"

    class Meta:
        db_table = 'Producto'
        verbose_name='Producto'
        verbose_name_plural= 'Productos'