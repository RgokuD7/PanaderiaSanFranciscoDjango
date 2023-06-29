from django.urls import path
from .views import *
urlpatterns = [
    path('home', home, name='home'),
    path('panaderia/', pan, name='pan'),
    path('empanadas/', empanadas, name='empanadas'),
    path('reposteria/', reposteria, name='reposteria'),
    path('carrito/', carrito, name='carrito'),
    path('contacto', contacto, name='contacto'),
    path('preguntas/', preguntas, name='preguntas'),
]