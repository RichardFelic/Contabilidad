from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(CatalogoCuentas)
admin.site.register(TipoMoneda)
admin.site.register(TipoCuenta)
admin.site.register(CatalogoAuxiliares)
@admin.register(Auxiliar)
class AuxiliarAdmin(admin.ModelAdmin):
    list_display=['id', 'id_aux','nombre_aux', 'cuenta', 'origen', 'monto', 'fecha', 'estado']

