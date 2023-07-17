from django.forms import ModelForm
from .models import TypeRawProjectQuasi, RawDataQuasiTerreno, RawDataQuasiAerea, RawProjectQuasiTerreno, RawProjectQuasiAerea


class TypeRawProjectQuasi(ModelForm):
    
    """
    Formato para subir tipos para el proyecto quasi-geoidal
    """

    class Meta:
        model = TypeRawProjectQuasi
        fields = ('detalles', 'tipo')
        labels = {
            'detalles': 'Descripción del tipo de proyecto para el modelo Quasigeoidal',
            'tipo': 'Tipo'
        }
    
    def __init__(self, *args, **kwargs):

        super(TypeRawProjectQuasi, self).__init(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['rows'] = 8


class RawProjectQuasiTerrenoForm(ModelForm):

    class Meta:
        model = RawProjectQuasiTerreno
        fields = ('proyecto', 'user', 'tipo')
        labels = {
            'proyecto': 'Tipo de proyecto quasi-geoidal',
            'user': 'Usuario a cargo',
            'tipo': 'Tipo de proyecto',
        }

    ## Inicializador de instancia TypeRawProjectQuasiForm
    def __init__(self, *args, **kwargs):    
        
        super(RawProjectQuasiTerrenoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['rows'] = 8