from django.shortcuts import render, redirect, get_object_or_404
from SistCont.forms import *
from SistCont.models import *
from rest_framework_swagger.views import get_swagger_view
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.
def home(request):
    catalogocuentas=CatalogoCuentas.objects.all()
    auxiliar=Auxiliar.objects.all()
    num_catalogocuentas=catalogocuentas.count()
    num_auxiliar=auxiliar.count()
    context={'num_catalogocuentas':num_catalogocuentas, 'num_auxiliar':num_auxiliar}
    return render(request, 'SistCont/dashboard.html', context)

#CRUD CATALOGOCUENTAS
def lista_catalogocuenta(request):
    cuenta = CatalogoCuentas.objects.all()
    return render(request, 'SistCont/lista_catalogocuenta.html', {'cuenta': cuenta})

def nueva_catalogocuenta(request):
    if request.method == 'POST':
        form = CatalogoCuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_catalogocuenta')
    else:
        form = CatalogoCuentaForm()
    return render(request, 'SistCont/CRUDS/nueva_catalogocuenta.html', {'form': form})

def editar_catalogocuenta(request, pk):
    pk = str(pk)
    try:
        cuenta = CatalogoCuentas.objects.get(id=pk)
    except CatalogoCuentas.DoesNotExist:
        return redirect('lista_catalogocuenta')
    form = CatalogoCuentaForm(request.POST or None, instance=cuenta)
    if form.is_valid():
        form.save()
        return redirect('lista_catalogocuenta')
    context = {'form':form, 'cuenta':cuenta}
    return render(request, 'SistCont/CRUDS/editar_catalogocuenta.html', context)

def eliminar_catalogocuenta(request, pk):
    cuenta = CatalogoCuentas.objects.get(pk=pk)
    if request.method == 'POST':
        cuenta.delete()
        return redirect('lista_catalogocuenta')
    context = {'cuenta':cuenta}
    return render(request, 'SistCont/CRUDS/borrar_catalogocuenta.html', context)


#CRUD TIPOCUENTA
def lista_tipocuenta(request):
    tipo = TipoCuenta.objects.all()
    return render(request, 'SistCont/lista_tipocuenta.html', {'tipo': tipo})

def nuevo_tipocuenta(request):
    if request.method == 'POST':
        form = TipoCuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tipocuenta')
    else:
        form = TipoCuentaForm()
    return render(request, 'SistCont/CRUDS/nuevo_tipocuenta.html', {'form': form})

def editar_tipocuenta(request, pk):
    pk = str(pk)
    try:
        tipo = TipoCuenta.objects.get(id=pk)
    except TipoCuenta.DoesNotExist:
        return redirect('lista_tipocuenta')
    form = TipoCuentaForm(request.POST or None, instance=tipo)
    if form.is_valid():
        form.save()
        return redirect('lista_tipocuenta')
    context = {'form':form, 'tipo':tipo}
    return render(request, 'SistCont/CRUDS/editar_tipocuenta.html', context)

def eliminar_tipocuenta(request, pk):
    tipo = TipoCuenta.objects.get(pk=pk)
    if request.method == 'POST':
        tipo.delete()
        return redirect('lista_tipocuenta')
    context = {'tipo':tipo}
    return render(request, 'SistCont/CRUDS/borrar_tipocuenta.html', context)



#CRUD TIPOMONEDA
def lista_tipomoneda(request):
    moneda = TipoMoneda.objects.all()
    return render(request, 'SistCont/lista_tipomoneda.html', {'moneda': moneda})

def nuevo_tipomoneda(request):
    if request.method == 'POST':
        form = TipoMonedaForm(request.POST)
        if form.is_valid():
            tipo_moneda=form.save()
            tipo_moneda.obtener_tasa_cambiaria()
            return redirect('lista_tipomoneda')
    else:
        form = TipoMonedaForm()
    return render(request, 'SistCont/CRUDS/nuevo_tipomoneda.html', {'form': form})

def editar_tipomoneda(request, pk):
    pk = str(pk)
    try:
        moneda = TipoMoneda.objects.get(id=pk)
    except TipoMoneda.DoesNotExist:
        return redirect('lista_tipomoneda')
    form = TipoMonedaForm(request.POST or None, instance=moneda)
    if form.is_valid():
        tipo_moneda = form.save()
        tipo_moneda.obtener_tasa_cambiaria()
        return redirect('lista_tipomoneda')
    context = {'form':form, 'moneda':moneda}
    return render(request, 'SistCont/CRUDS/editar_tipomoneda.html', context)
    
def eliminar_tipomoneda(request, pk):
    moneda = TipoMoneda.objects.get(pk=pk)
    if request.method == 'POST':
        moneda.delete()
        return redirect('lista_tipomoneda')
    context = {'moneda':moneda}
    return render(request, 'SistCont/CRUDS/borrar_tipomoneda.html', context)

#CRUD AUXILIAR
def lista_auxiliar(request):
    auxiliar = Auxiliar.objects.all()
    return render(request, 'SistCont/lista_auxiliar.html', {'auxiliar': auxiliar})

def nuevo_auxiliar(request):
    if request.method == 'POST':
        form = AuxiliarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_auxiliar')
    else:
        form = AuxiliarForm()
    return render(request, 'SistCont/CRUDS/nuevo_auxiliar.html', {'form': form})

def editar_auxiliar(request, pk):
    pk = str(pk)
    try:
        auxiliar = Auxiliar.objects.get(id=pk)
    except Auxiliar.DoesNotExist:
        return redirect('lista_auxiliar')
    form = AuxiliarForm(request.POST or None, instance=auxiliar)
    if form.is_valid():
        form.save()
        return redirect('lista_auxiliar')
    context = {'form':form, 'auxiliar':auxiliar}
    return render(request, 'SistCont/CRUDS/editar_auxiliar.html', context)       
        
def eliminar_auxiliar(request, pk):
    auxiliar = Auxiliar.objects.get(pk=pk)
    if request.method == 'POST':
        auxiliar.delete()
        return redirect('lista_auxiliar')
    context = {'auxiliar':auxiliar}
    return render(request, 'SistCont/CRUDS/borrar_auxiliar.html', context)   

def ver_auxiliar(request, pk):
    auxiliar = Auxiliar.objects.get(pk=pk)
    context = {'auxiliar':auxiliar}
    return render(request, 'SistCont/CRUDS/ver_auxiliar.html', context)   

#ENTRADA CONTABLE
def lista_entradacontable(request):
    entrada = CatalogoAuxiliares.objects.all()
    return render(request, 'SistCont/lista_entradacontable.html', {'entrada': entrada})


    #auxiliar = Auxiliar.objects.get(id=pk)
    #if request.method == 'POST':
        #auxiliar.delete()
        #return redirect('lista_auxiliar')
        
    #context = {'auxiliar':auxiliar}
    #return render(request, 'SistCont/CRUDS/lista_auxiliar.html', context)   

def transferir_registro(request, pk):
    aux = Auxiliar.objects.filter(pk=pk)
    try:
        for i in aux:
            CatalogoAuxiliares.objects.create(
                id_EC = 'EC{}'.format(i.id_EC[2:]),
                id_aux = str(i.id_aux),
                descripcion = i.nombre_aux,
                cuenta = i.cuenta,
                origen = i.origen,
                monto = i.monto,
                fecha = i.fecha,
                estado= True
            )
        #Auxiliar.objects.filter(pk=pk).delete()
            i.transferido = True # actualiza el campo transferido a True
            i.save()
        messages.success(request, "Los registros se han transferido correctamente.")
    except IntegrityError:
        messages.error(request, "BIEN")
        return redirect('lista_auxiliar')
    return redirect('lista_auxiliar')

def eliminar_entradacontable(request, pk):
    entrada = get_object_or_404(CatalogoAuxiliares, pk=pk)
    entrada.delete()
    return redirect('lista_entradacontable')

