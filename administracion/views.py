from django.shortcuts import render, redirect, get_object_or_404
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
def edit_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)

    if request.method == 'POST':
        form = ProductosForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductosForm(instance=producto)
    
    return render(request, 'administracion/edit_producto.html', {'form': form})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    producto.delete()
    return redirect('productos')


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
def edit_tpproducto(request, tpproducto_id):
    tpproducto = get_object_or_404(TipoProducto, id_tipoProducto=tpproducto_id)

    if request.method == 'POST':
        form = TipoProductoForm(request.POST, instance=tpproducto)
        if form.is_valid():
            form.save()
            return redirect('tpproductos')
    else:
        form = TipoProductoForm(instance=tpproducto)
    
    return render(request, 'administracion/edit_tpproducto.html', {'form': form})

@login_required
def eliminar_tpproducto(request, tpproducto_id):
    tpproducto = get_object_or_404(TipoProducto, id_tipoProducto=tpproducto_id)
    tpproducto.delete()
    return redirect('tpproductos')

@login_required
def region(request):
    regiones = Region.objects.all()
    return render(request, 'administracion/region.html', {'regiones': regiones})

@login_required
def add_region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('region')
    else:
            form = RegionForm()
    return render(request, 'administracion/add_region.html', {'form': form})

@login_required
def edit_region(request, region_id):
    region = get_object_or_404(Region, id_region=region_id)

    if request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect('region')
    else:
        form = RegionForm(instance=region)
    
    return render(request, 'administracion/edit_region.html', {'form': form})

@login_required
def eliminar_region(request, region_id):
    region = get_object_or_404(Region, id_region=region_id)
    region.delete()
    return redirect('region')

@login_required
def comuna(request):
    comunas = Comuna.objects.all()
    return render(request, 'administracion/comuna.html', {'comunas': comunas})

@login_required
def add_comuna(request):
    if request.method == 'POST':
        form = ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comuna')
    else:
            form = ComunaForm()
    return render(request, 'administracion/add_comuna.html', {'form': form})

@login_required
def edit_comuna(request, comuna_id):
    comuna = get_object_or_404(Comuna, id_comuna=comuna_id)

    if request.method == 'POST':
        form = ComunaForm(request.POST, instance=comuna)
        if form.is_valid():
            form.save()
            return redirect('comuna')
    else:
        form = ComunaForm(instance=comuna)
    
    return render(request, 'administracion/edit_comuna.html', {'form': form})

@login_required
def eliminar_comuna(request, comuna_id):
    comuna = get_object_or_404(Comuna, id_comuna=comuna_id)
    comuna.delete()
    return redirect('comuna')