from django.db import models

# Create your models here.
class Imagen(models.Model):
    id_img = models.AutoField(primary_key=True, verbose_name='Id de la Imagen')
    nombre_img = models.CharField(max_length= 50, verbose_name= 'Nombre de la Imagen') 
    imagen = models.ImageField(upload_to='static/adminstracion/img/productos/')

    def __str__(self):
        return self.imagen

class tipoProducto(models.Model):
    id_tipoProducto = models.AutoField(primary_key=True, verbose_name='Id de Tipo Producto')
    tipo_producto = models.CharField(max_length=50, verbose_name='Tipo de Producto')

    def __str__(self):
        return self.tipo_producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name='Id de Producto')
    nombre = models.CharField(max_length=100 ,verbose_name= 'Nombre del Producto')
    descripcion = models.TextField(verbose_name='Descripcion del Producto')
    precio = models.IntegerField(verbose_name='Precio del Producto')
    tipo_producto = models.ForeignKey(tipoProducto, on_delete= models.SET_NULL, null= True, verbose_name='Tipo de Producto')
    img = models.ForeignKey(Imagen, on_delete= models.SET_NULL, null= True, verbose_name='Nombre de la Imagen del Producto')
    ingredientes = models.TextField(verbose_name='Ingredientes del Producto')
    stock = models.IntegerField(verbose_name='Stock del Producto')

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    rut = models.CharField(primary_key= True, max_length= 10, verbose_name= 'Rut Usuario')
    nombres = models.CharField(max_length= 50, verbose_name= 'Nombres Usuario')
    apellidos = models.CharField(max_length= 50, verbose_name= 'Apellidos Usuario')
    fec_nac = models.DateField(verbose_name= 'Fecha Nacimiento Usuario')
    telefono = models.IntegerField(verbose_name= 'Telefono Usuario')
    mail = models.EmailField(verbose_name= 'Email Usuario')
    password = models.CharField(max_length= 15, verbose_name= 'Password Usuario')

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
    id_region = models.IntegerField(primary_key= True, verbose_name= 'Id Region')
    region = models.CharField(max_length=255, verbose_name= 'Region')

    def __str__(self):
        return self.region

class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key= True, verbose_name= 'Id Comuna')
    comuna = models.CharField(max_length= 255, verbose_name= 'Comuna')
    id_region = models.ForeignKey(Region, on_delete= models.CASCADE, verbose_name= 'Id Region')

    def __str__(self):
        return self.comuna


class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True, verbose_name= 'Id direccion')
    direccion = models.CharField(max_length= 255, verbose_name= 'Direccion')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name= 'Rut Usuario del Carrito')
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name= 'Id comuna')

    def __str__(self):
        return self.direccion