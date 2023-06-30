from django.shortcuts import render, redirect, get_object_or_404
from administracion.models import *
import json
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def pan(request):
    productos = Producto.objects.all()
    data = json.dumps([{'id': producto.id_producto, 'nombre': producto.nombre, 'descripcion': producto.descripcion, 'precio': producto.precio, 'precio': producto.precio, 'categoria': producto.tipo_producto.id_tipoProducto , 'imagen': producto.img, 'ingredientes': producto.ingredientes, 'stock': producto.stock} for producto in productos])
    return render(request, 'core/pan.html', {'datos': data})

def empanadas(request):
    productos = Producto.objects.all()
    data = json.dumps([{'id': producto.id_producto, 'nombre': producto.nombre, 'descripcion': producto.descripcion, 'precio': producto.precio, 'precio': producto.precio, 'categoria': producto.tipo_producto.id_tipoProducto , 'imagen': producto.img, 'ingredientes': producto.ingredientes, 'stock': producto.stock} for producto in productos])
    return render(request, 'core/empanadas.html', {'datos': data})

def reposteria(request):
    productos = Producto.objects.all()
    data = json.dumps([{'id': producto.id_producto, 'nombre': producto.nombre, 'descripcion': producto.descripcion, 'precio': producto.precio, 'precio': producto.precio, 'categoria': producto.tipo_producto.id_tipoProducto , 'imagen': producto.img, 'ingredientes': producto.ingredientes, 'stock': producto.stock} for producto in productos])
    return render(request, 'core/reposteria.html', {'datos': data})

def carrito(request):
    productos = Producto.objects.all()
    data = json.dumps([{'id': producto.id_producto, 'nombre': producto.nombre, 'descripcion': producto.descripcion, 'precio': producto.precio, 'precio': producto.precio, 'categoria': producto.tipo_producto.id_tipoProducto , 'imagen': producto.img, 'ingredientes': producto.ingredientes, 'stock': producto.stock} for producto in productos])
    return render(request, 'core/carrito.html', {'datos': data})

def contacto(request):
    return render(request, 'core/contacto.html')

def preguntas(request):
    return render(request, 'core/preguntas.html')