from django.shortcuts import render, redirect, get_object_or_404
from administracion.models import *
from administracion.forms import *
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def pan(request):
    productos = Producto.objects.all()
    return render(request, 'core/pan.html', {'productos': productos})

def empanadas(request):
    productos = Producto.objects.all()
    return render(request, 'core/empanadas.html', {'productos': productos})

def reposteria(request):
    productos = Producto.objects.all()
    return render(request, 'core/reposteria.html', {'productos': productos})

def carrito(request):
    productos = Producto.objects.all()
    return render(request, 'core/carrito.html', {'productos': productos})

def contacto(request):
    return render(request, 'core/contacto.html')

def preguntas(request):
    return render(request, 'core/preguntas.html')

def registrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
            form = UsuarioForm()
    return render(request, 'core/registrar.html', {'form': form})

def verify_password(raw_password, stored_password):
    return raw_password == stored_password

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']

            try:
                user = Usuario.objects.get(rut=rut)
            except Usuario.DoesNotExist:
                form.add_error(None, "RUT incorrecto")
                return render(request, 'core/login_user.html', {'form': form})

            if not verify_password(password, user.password):
                form.add_error(None, "Contraseña incorrecta")
                return render(request, 'core/login_user.html', {'form': form})

            # Si el usuario y la contraseña son correctos, puedes redirigir al usuario a la página de inicio.
            return redirect('home')

    else:
        form = LoginForm()

    return render(request, 'core/login_user.html', {'form': form})


def agregar_al_carrito(request):
    if request.method == 'POST':
        usuario_rut = request.POST.get('usuario_rut')
        producto_id = request.POST.get('producto_id')
        cantidad = request.POST.get('cantidad')

        try:
            usuario = Usuario.objects.get(rut=usuario_rut)
        except Usuario.DoesNotExist:
            return JsonResponse({'mensaje': 'Usuario no encontrado.'}, status=400)

        try:
            carrito = Carrito.objects.get(usuario=usuario)
        except Carrito.DoesNotExist:
            carrito = Carrito(usuario=usuario)
            carrito.save()

        producto = Producto.objects.get(id=producto_id)

        item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        item_carrito.cantidad = cantidad
        item_carrito.save()

        return JsonResponse({'mensaje': 'Producto agregado al carrito exitosamente.'})