from django.shortcuts import render, redirect, get_object_or_404
from administracion.models import *
from administracion.forms import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def pan(request):
    rut_usuario = request.session.get('rut')  # Obtiene el "rut" guardado en la sesión
    elementos_carrito = []

    if rut_usuario:
        try:
            usuario = Usuario.objects.get(rut=rut_usuario)
            carrito = Carrito.objects.get(usuario=usuario)
            elementos_carrito = carrito.itemcarrito_set.all()
        except (Usuario.DoesNotExist, Carrito.DoesNotExist):
            pass  # El usuario con ese "rut" no existe, o no tiene carrito aún

    productos = Producto.objects.all()
    return render(request, 'core/pan.html', {'productos': productos, 'elementos_carrito': elementos_carrito})

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

def registro_usuario(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.none()  # Comunas vacías por defecto

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        direccion_form = DireccionForm(request.POST)

        if usuario_form.is_valid() and direccion_form.is_valid():
            usuario = usuario_form.save()
            direccion = direccion_form.save(commit=False)
            direccion.usuario = usuario
            direccion.save()
            # Resto del código de redirección o respuesta

    else:
        usuario_form = UsuarioForm()
        direccion_form = DireccionForm()

    context = {
        'usuario_form': usuario_form,
        'direccion_form': direccion_form,
        'regiones': regiones,
        'comunas': comunas,
    }
    return render(request, 'core/registrar.html', context)

def obtener_comunas(request):
    region_id = request.GET.get('region_id')
    comunas = Comuna.objects.filter(id_region=region_id)
    data = [{'id_comuna': comuna.id_comuna, 'comuna': comuna.comuna} for comuna in comunas]
    return JsonResponse(data, safe=False)

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

            request.session['rut'] = rut
            # Si el usuario y la contraseña son correctos, puedes redirigir al usuario a la página de inicio.
            return redirect('home')

    else:
        form = LoginForm()

    return render(request, 'core/login_user.html', {'form': form})


def modificar_carrito(request):
    if request.method == 'POST':
        usuario_rut = request.POST.get('usuario_rut')
        producto_id = request.POST.get('producto_id')
        op = request.POST.get('op')

        try:
            usuario = Usuario.objects.get(rut=usuario_rut)
            # Obtener el carrito del usuario
            carrito, created = Carrito.objects.get_or_create(usuario=usuario)
            if op == 'empty':
                print(producto_id, op, )
                carrito.delete()
                carrito.save()
                return JsonResponse({'success': True, 'message': 'Carrito modificado correctamente.'})

            producto = Producto.objects.get(id_producto=producto_id)

            # Obtener el item correspondiente al producto en el carrito
            item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

            if op == 'add':
                # Aumentar la cantidad del producto en el carrito
                if created == False:
                    item.cantidad += 1
                item.save()
            elif op == 'del1':
                # Disminuir la cantidad del producto en el carrito
                if item.cantidad > 1:
                    item.cantidad -= 1
                    item.save()
                else:
                    # Eliminar el producto del carrito si la cantidad es 1
                    item.delete()
            elif op == 'del':
                # Eliminar el producto completo del carrito
                item.delete()
            carrito.save()

            # Devolver una respuesta JSON indicando que se modificó correctamente
            return JsonResponse({'success': True, 'message': 'Carrito modificado correctamente.'})
        except Usuario.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El usuario no existe.'})
        except Producto.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El producto no existe.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Error al modificar el carrito.', 'xd': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido.'})
