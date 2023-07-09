from django import forms
from .models import *
from django.core.exceptions import ValidationError

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio','tipo_producto', 'imagen', 'ingredientes', 'stock']

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['tipo_producto']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
        widgets = {
            'fec_nac': forms.DateInput(attrs={'type': 'date'}),
        }  # Incluir todos los campos del modelo

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['direccion']
        
class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['region']
class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['comuna', 'id_region']


class LoginForm(forms.Form):
    rut = forms.CharField(label="RUT")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        rut = cleaned_data.get("rut")
        password = cleaned_data.get("password")

        if rut and password:
            try:
                user = Usuario.objects.get(rut=rut)
            except Usuario.DoesNotExist:
                raise forms.ValidationError("RUT incorrecto")

            if not user.password == password:
                raise forms.ValidationError("Contraseña incorrecta")

        return cleaned_data
