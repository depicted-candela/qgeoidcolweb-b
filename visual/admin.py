from django.contrib import admin
from preprocesos.models import RawDataQuasiTerreno

# Register your models here.
@admin.register(RawDataQuasiTerreno)
class RawDataQuasiTerrenoAdmin(admin.ModelAdmin):
    list_display = ('id', 'posicion', 'elevacion', 'gravedad', 'nomenclatura', 'project_id')

# admin.site.register(RawDataQuasiTerreno, RawDataQuasiTerrenoAdmin)