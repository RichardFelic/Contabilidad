from rest_framework.viewsets import ModelViewSet
from SistCont.models import *
from SistCont.api.serializers import *

class AuxiliarApiViewSet(ModelViewSet):
    serializer_class= AuxiliarSerializer
    queryset = Auxiliar.objects.all()

class TipoMonedaApiViewSet(ModelViewSet):
    serializer_class= TipoMonedaSerializer
    queryset = TipoMoneda.objects.all()