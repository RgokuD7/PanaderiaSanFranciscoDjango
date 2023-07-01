from django.urls import path
from .views import *
urlpatterns = [
    path('usuario', usuario, name='usuario'),
    path('productos', productos, name='productos'),
    path('add_producto', add_producto, name= 'add_producto'),
    path('edit_producto/<int:producto_id>/', edit_producto, name= 'edit_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name= 'eliminar_producto'),
    path('tpproductos', tpproductos, name='tpproductos'),
    path('add_tpproducto', add_tpproducto, name= 'add_tpproducto'),
    path('edit_tpproducto/<int:tpproducto_id>/', edit_tpproducto, name='edit_tpproducto'),
    path('eliminar_tpproducto/<int:tpproducto_id>/', eliminar_tpproducto, name='elimar_tpproducto'),
    path('region', region, name='region'),
    path('add_region', add_region, name='add_region'),
    path('edit_region/<int:region_id>/', edit_region, name='edit_region'),
    path('eliminar_region/<int:region_id>/', eliminar_region, name='eliminar_region'),
    path('comuna', comuna, name='comuna'),
    path('add_comuna', add_comuna, name='add_comuna'),
    path('edit_comuna/<int:comuna_id>/', edit_comuna, name='edit_comuna'),
    path('eliminar_comuna/<int:comuna_id>/', eliminar_comuna , name='eliminar_comuna'),
]
