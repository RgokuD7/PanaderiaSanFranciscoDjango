from django.urls import path
from .views import *
urlpatterns = [
    path('usuario', usuario, name='usuario'),
    path('productos', productos, name='productos'),
    path('tpproductos', tpproductos, name='tpproductos'),
    path('region', region, name='region'),
    path('comuna', comuna, name='comuna'),
]