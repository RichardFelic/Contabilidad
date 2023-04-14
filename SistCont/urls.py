from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    #MAIN 
    path('', views.home, name='home'),

    #CRUD CATALOGOCUENTAS
    path('lista_catalogocuenta/',views.lista_catalogocuenta, name='lista_catalogocuenta'),
    path('nueva_catalogocuenta/',views.nueva_catalogocuenta, name='nueva_catalogocuenta'),
    path('editar_catalogocuenta/<str:pk>/',views.editar_catalogocuenta, name='editar_catalogocuenta'),
    path('eliminar_catalogocuenta/<str:pk>/',views.eliminar_catalogocuenta, name='eliminar_catalogocuenta'),

    #CRUD TIPOCUENTA
    path('lista_tipocuenta/',views.lista_tipocuenta, name='lista_tipocuenta'),
    path('nuevo_tipocuenta/',views.nuevo_tipocuenta, name='nuevo_tipocuenta'),
    path('editar_tipocuenta/<str:pk>/',views.editar_tipocuenta, name='editar_tipocuenta'),
    path('eliminar_tipocuenta/<str:pk>/',views.eliminar_tipocuenta, name='eliminar_tipocuenta'),
    

    #CRUD TIPOMONEDA
    path('lista_tipomoneda/',views.lista_tipomoneda, name='lista_tipomoneda'),
    path('nuevo_tipomoneda/',views.nuevo_tipomoneda, name='nuevo_tipomoneda'),
    path('editar_tipomoneda/<str:pk>/',views.editar_tipomoneda, name='editar_tipomoneda'),
    path('eliminar_tipomoneda/<str:pk>/',views.eliminar_tipomoneda, name='eliminar_tipomoneda'),

    #CRUD AUXILIAR
    path('lista_auxiliar/',views.lista_auxiliar, name='lista_auxiliar'),
    path('nuevo_auxiliar/',views.nuevo_auxiliar, name='nuevo_auxiliar'),
    path('editar_auxiliar/<str:pk>/',views.editar_auxiliar, name='editar_auxiliar'),
    path('eliminar_auxiliar/<str:pk>/',views.eliminar_auxiliar, name='eliminar_auxiliar'),
    path('ver_auxiliar/<str:pk>/',views.ver_auxiliar, name='ver_auxiliar'),

    #ENTRADA CONTABLE
    path('lista_entradacontable/',views.lista_entradacontable, name='lista_entradacontable'),

    # Transferir a CatalogoAuxiliares
    path('transferir_registro/<str:pk>/',views.transferir_registro, name='transferir_registro'),
    path('eliminar_entradacontable/<str:pk>/',views.eliminar_entradacontable, name='eliminar_entradacontable'),

    #SWAGGER
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='docs'),
]

