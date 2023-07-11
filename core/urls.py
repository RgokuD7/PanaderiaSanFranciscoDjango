from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('tipoproducto/<int:id_tpproducto>/', tipos_productos, name='tipos_productos'),
    path('carrito/', carrito, name='carrito'),
    path('contacto', contacto, name='contacto'),
    path('preguntas/', preguntas, name='preguntas'),
    path('registrar/', registro_usuario, name='registrar'),
    path('obtener_comunas/', obtener_comunas, name='obtener_comunas'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('modificar_carrito/', modificar_carrito, name='modificar_carrito'),
]