from django.db import models
from usuarios.models import Usuario


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




class CarritoProductos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='carritos')
    monto = models.DecimalField(max_digits=6, decimal_places=2,default=0.0)

    def __str__(self):
        return f'Carrito de {self.usuario}'

    def actualizar_monto(self):
        self.monto = sum([detalle.monto for detalle in self.detalles.all()])
        self.save()
        self.refresh_from_db()

    class Meta:
        db_table = 'CarritoProductos'
        verbose_name = 'CarritoProductos'
        verbose_name_plural = 'CarritosProductos'


class DetalleCarritoProductos(models.Model):
    carrito = models.ForeignKey(CarritoProductos, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    monto = models.DecimalField(max_digits=6, decimal_places=2,default=0.0)

    def __str__(self):
        return f'{self.cantidad} de {self.producto} en {self.carrito}'

    def save(self, *args, **kwargs):
        if self.producto.stock < self.cantidad:
            raise ValueError("Stock insuficiente para este producto")
            
        self.monto = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)
        self.carrito.actualizar_monto()

    class Meta:
        db_table = 'DetalleCarritoProducto'
        verbose_name = 'DetalleCarritoProducto'
        verbose_name_plural = 'DetallesCarritosProductos'

class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    carrito = models.OneToOneField(CarritoProductos, on_delete=models.SET_NULL, null=True)