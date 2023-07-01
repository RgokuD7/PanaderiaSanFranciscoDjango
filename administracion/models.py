from django.db import models
from django.contrib.auth.hashers import check_password
# Create your models here.
class TipoProducto(models.Model):
    id_tipoProducto = models.AutoField(primary_key=True, verbose_name='Id de Tipo Producto')
    tipo_producto = models.CharField(max_length=50, verbose_name='Tipo de Producto')

    def __str__(self):
        return self.tipo_producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name='Id de Producto')
    nombre = models.CharField(max_length=100 ,verbose_name= 'Nombre del Producto')
    descripcion = models.TextField(verbose_name='Descripcion del Producto')
    precio = models.IntegerField(verbose_name='Precio del Producto')
    tipo_producto = models.ForeignKey(TipoProducto, on_delete= models.SET_NULL, null= True, verbose_name='Tipo de Producto')
    imagen = models.ImageField(upload_to= 'img/productos', default='static/core/img/logo.jpg', verbose_name= 'Imagen del Producto')
    ingredientes = models.TextField(verbose_name='Ingredientes del Producto')
    stock = models.IntegerField(verbose_name='Stock del Producto')

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    rut = models.CharField(primary_key= True, max_length= 10, verbose_name= 'Rut')
    nombres = models.CharField(max_length= 50, verbose_name= 'Nombres')
    apellidos = models.CharField(max_length= 50, verbose_name= 'Apellidos')
    fec_nac = models.DateTimeField(verbose_name= 'Fecha Nacimiento')
    telefono = models.IntegerField(verbose_name= 'Telefono')
    mail = models.EmailField(verbose_name= 'Email')
    password = models.CharField(max_length= 15, verbose_name= 'Password')

    def __str__(self):
        return self.rut
    

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name= 'Rut Usuario del Carrito')
    productos = models.ManyToManyField(Producto, through='ItemCarrito', verbose_name= 'Productos de Carrito')

    def __str__(self):
        return self.usuario

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, verbose_name= 'Id de Carrito')
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE, verbose_name= 'Productos de Carrito')
    cantidad = models.PositiveIntegerField(default=1, verbose_name= 'Cantidad de Productos')

    def __str__(self):
        return self.carrito

class Region(models.Model):
    id_region = models.AutoField(primary_key= True, verbose_name= 'Id Region')
    region = models.CharField(max_length=255, verbose_name= 'Region')

    def __str__(self):
        return self.region

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key= True, verbose_name= 'Id Comuna')
    comuna = models.CharField(max_length= 255, verbose_name= 'Comuna')
    id_region = models.ForeignKey(Region, on_delete= models.CASCADE, verbose_name= 'Region')

    def __str__(self):
        return self.comuna


class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True, verbose_name= 'Id direccion')
    direccion = models.CharField(max_length= 255, verbose_name= 'Direccion')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name= 'Rut Usuario del Carrito')
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name= 'Comuna')

    def __str__(self):
        return self.direccion