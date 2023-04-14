from django import forms
from .models import *

class CatalogoCuentaForm(forms.ModelForm):
    class Meta:
        model = CatalogoCuentas
        fields = '__all__'
        


class TipoCuentaForm(forms.ModelForm):
    class Meta:
        model = TipoCuenta
        fields = '__all__'


class TipoMonedaForm(forms.ModelForm):
    class Meta:
        model = TipoMoneda
        fields = ['descripcion','codigo_iso', 'estado' ]


class AuxiliarForm(forms.ModelForm):
    class Meta:
        model = Auxiliar
        fields = ['id_aux','nombre_aux', 'cuenta', 'origen', 'monto', 'fecha', 'estado' ]