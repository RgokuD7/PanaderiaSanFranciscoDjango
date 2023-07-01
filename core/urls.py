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
    path('registrar/', registrar, name='registrar'),
    path('login_user', login_user, name='login_user'),
    path('agregar_al_carrito/', agregar_al_carrito, name='agregar_al_carrito'),
]