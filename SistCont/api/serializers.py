from rest_framework.serializers import ModelSerializer
from SistCont.models import *

class AuxiliarSerializer(ModelSerializer):
    class Meta:
        model = Auxiliar
        fields= ['id', 'id_EC','id_aux','nombre_aux', 'cuenta', 'origen', 'monto']

class TipoMonedaSerializer(ModelSerializer):
    class Meta:
        model = TipoMoneda
        fields= ['id', 'descripcion','ultima_tasa_cambiaria']