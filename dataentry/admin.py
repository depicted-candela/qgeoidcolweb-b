from django.contrib import admin
from .models import SubirArchivo
from preprocesos.models import TypeRawProjectQuasi, RawProject, RawProjectQuasiTerreno


class SubirArchivoAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'file', 'tipo', 'detalles')

class TypeRawProjectQuasiAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'detalles')

class RawProjectQuasiTerrenoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'user', 'data')

admin.site.register(SubirArchivo, SubirArchivoAdmin)
admin.site.register(TypeRawProjectQuasi, TypeRawProjectQuasiAdmin)
admin.site.register(RawProjectQuasiTerreno, RawProjectQuasiTerrenoAdmin)