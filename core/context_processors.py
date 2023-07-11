from administracion.models import *

def datos_adicionales(request):
    tipos_productos = TipoProducto.objects.all().order_by('tipo_producto')
    datos = {
        'tipos_productos': tipos_productos
    }
    return datos