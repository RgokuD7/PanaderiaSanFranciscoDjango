from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required
def usuario(request):
    return render(request, 'administracion/usuario.html')

@login_required
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'administracion/productos.html', {'productos': productos})

@login_required
def add_producto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')  # Redirige a la página de lista de productos después de guardar el producto
    else:
        form = ProductosForm()
    return render(request, 'administracion/add_producto.html', {'form': form})


@login_required
def tpproductos(request):
    tpproductos = TipoProducto.objects.all()
    return render(request, 'administracion/tpproductos.html', {'tpproductos': tpproductos})

@login_required
def add_tpproducto(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tpproductos')
    else:
            form = TipoProductoForm()
    return render(request, 'administracion/add_tpproducto.html', {'form': form})

@login_required
def region(request):
    regiones = Region.objects.all()
    return render(request, 'administracion/region.html', {'regiones': regiones})

@login_required
def comuna(request):
    comunas = Comuna.objects.all()
    return render(request, 'administracion/comuna.html', {'comunas': comunas})
