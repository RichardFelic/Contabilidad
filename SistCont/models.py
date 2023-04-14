from django import forms
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
import requests
from SistCont.Enums import Season
from django.contrib import messages

# Create your models here.
   
class TipoMoneda(models.Model):
    descripcion = models.CharField(max_length=50)
    codigo_iso = models.CharField(max_length=3, null=True)
    ultima_tasa_cambiaria = models.FloatField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
    def obtener_tasa_cambiaria(self):
        if self.codigo_iso:
            url = f'https://karlus-dev-public-services-app.azurewebsites.net/api/Consult/tasa-cambiaria/{self.codigo_iso.lower()}'
            response = requests.get(url)
            if response.ok:
                tasa = response.json()['tasa']
                self.ultima_tasa_cambiaria = tasa
                self.save()
    
class TipoCuenta(models.Model):
    descripcion = models.CharField(max_length=50)
    origen = models.CharField(max_length=2, choices=[('DB', 'DB'), ('CR', 'CR')])
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
class CatalogoAuxiliares(models.Model):
    id_EC = models.CharField(max_length=10, unique=True, blank=True)
    descripcion= models.CharField(max_length=50)
    id_aux= models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], null=True)
    cuenta = models.CharField(max_length=50, null=True)
    origen = models.CharField(max_length=2, choices=[('DB', 'DB'), ('CR', 'CR')], null=True)
    fecha = models.DateField(default=timezone.now)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.identificador
    
    def save(self, *args, **kwargs):
        if not self.id_EC:
            ult_obj = CatalogoAuxiliares.objects.order_by('-id').first()
            if ult_obj:
                ult_cod = ult_obj.id_EC
                num = int(ult_cod[2:])
                self.id_EC = 'EC{}'.format(num +1)
            else:
                self.id_EC = 'EC1'
        super(CatalogoAuxiliares, self).save(*args, **kwargs)


class Auxiliar(models.Model):
    id_EC = models.CharField(max_length=10, unique=True, blank=True)
    id_aux = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], default=1)
    nombre_aux = models.CharField(max_length=50)
    cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, null=True)
    origen = models.CharField(max_length=2, choices=[('DB', 'DB'), ('CR', 'CR')], null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateField(default=timezone.now)
    estado = models.BooleanField(default=True)
    transferido = models.BooleanField(default=False) 

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.id_EC:
            ult_obj = Auxiliar.objects.order_by('-id').first()
            if ult_obj:
                ult_cod = ult_obj.id_EC
                num = int(ult_cod[2:])
                self.id_EC = 'AC{}'.format(num +1)
            else:
                self.id_EC = 'AC1'
        super(Auxiliar, self).save(*args, **kwargs)
    
    def clean(self):
        if self.monto < 0:
            raise ValidationError("El valor de 'monto' no puede ser negativo.")
        super().clean()
    
    def get_estado_display(self):
        return "Sí" if self.transferido else "No"

    
class CatalogoCuentas(models.Model):
    descripcion = models.CharField(max_length=50)
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE)
    permite_transacciones = models.BooleanField(default=True)
    nivel = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], null=True, blank=True)
    cuenta_mayor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    balance = models.FloatField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
    def determinar_nivel(self):
        if not self.cuenta_mayor:
            return 1
        elif not self.cuenta_mayor.cuenta_mayor:
            return 2
        else:
            return 3
        
    def save(self, *args, **kwargs):
        self.nivel = self.determinar_nivel()
        super().save(*args, **kwargs)

    def clean(self):
        if self.balance < 0:
            raise ValidationError("El valor de 'balance' no puede ser negativo.")
        super().clean()
        
    