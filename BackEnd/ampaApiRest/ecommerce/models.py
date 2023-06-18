from django.db import models
from usuarios.models import Usuario
from django.db import transaction

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
    foto = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca} -${self.precio}"

    class Meta:
        db_table = 'Producto'
        verbose_name='Producto'
        verbose_name_plural= 'Productos'




class CarritoProductos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='carritos')
   
    @property
    def monto(self):
        return sum([detalle.monto for detalle in self.detalles.all()])
    
    @property
    def detalles_carrito(self):
        return [str(detalle) for detalle in self.detalles.all()]
   
    def __str__(self):
        return f'Carrito de {self.usuario}'

    

    class Meta:
        db_table = 'CarritoProductos'
        verbose_name = 'CarritoProductos'
        verbose_name_plural = 'CarritosProductos'


class DetalleCarritoProductos(models.Model):
    carrito = models.ForeignKey(CarritoProductos, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()

    @property
    def monto(self):
        return self.producto.precio * self.cantidad

    def save(self, *args, **kwargs):
        with transaction.atomic():
            self.producto.refresh_from_db()
            if self.producto.stock < self.cantidad:
                raise ValueError("Stock insuficiente para este producto")
            super().save(*args, **kwargs)

    class Meta:
        db_table = 'DetalleCarritoProducto'
        verbose_name = 'DetalleCarritoProducto'
        verbose_name_plural = 'DetallesCarritosProductos'

class Factura(models.Model):
    ESTADOS = (
        ('PE', 'Pendiente'),
        ('PA', 'Pagado'),        
    )
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='PE')
    carrito = models.OneToOneField(CarritoProductos, on_delete=models.SET_NULL, null=True)
    @property
    def total(self):
        return self.subtotal - self.descuento

    class Meta:
        db_table = 'Factura'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'