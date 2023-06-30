from django import forms
from .models import *
from django.core.exceptions import ValidationError

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio','tipo_producto', 'imagen', 'ingredientes', 'stock']

class TipoProductoForm(models.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['tipo_producto']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombres', 'apellidos', 'fec_nac', 'telefono', 'mail', 'password']

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['region']

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['comuna', 'id_region']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['direccion', 'usuario', 'id_comuna']
