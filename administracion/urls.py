from django.urls import path
from .views import *
urlpatterns = [
    path('usuario', usuario, name='usuario'),
    path('productos', productos, name='productos'),
    path('add_producto', add_producto, name= 'add_producto'),
    path('tpproductos', tpproductos, name='tpproductos'),
    path('add_tpproducto', add_tpproducto, name= 'add_tpproducto'),
    path('region', region, name='region'),
    path('comuna', comuna, name='comuna'),
]