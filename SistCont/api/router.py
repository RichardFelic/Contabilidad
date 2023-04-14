from rest_framework.routers import DefaultRouter
from SistCont.api.views import *

router_auxiliares= DefaultRouter()

router_auxiliares.register(prefix='SistCont', basename='SistCont', viewset=AuxiliarApiViewSet)

router_tipos = DefaultRouter()

router_tipos.register(prefix='SistCont', basename='SistCont', viewset=TipoMonedaApiViewSet)