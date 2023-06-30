from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required
def usuario(request):
    return render(request, 'administracion/usuario.html')

@login_required
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'administracion/productos.html', {'productos': productos})

@login_required
def tpproductos(request):
    return render(request, 'administracion/tpproductos.html')

@login_required
def region(request):
    return render(request, 'administracion/region.html')

@login_required
def comuna(request):
    return render(request, 'administracion/comuna.html')
