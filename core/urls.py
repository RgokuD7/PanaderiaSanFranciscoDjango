from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('panaderia/', pan, name='pan'),
    path('empanadas/', empanadas, name='empanadas'),
    path('reposteria/', reposteria, name='reposteria'),
    path('carrito/', carrito, name='carrito'),
    path('contacto', contacto, name='contacto'),
    path('preguntas/', preguntas, name='preguntas'),
    path('registrar/', registro_usuario, name='registrar'),
    path('obtener_comunas/', obtener_comunas, name='obtener_comunas'),
    path('login_user', login_user, name='login_user'),
    path('modificar_carrito/', modificar_carrito, name='modificar_carrito'),
]