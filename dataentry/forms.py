from django.forms import ModelForm
from .models import SubirArchivo

class SubirArchivoForm(ModelForm):

    """
    Formato para subir archivos de cualquier formato
    """

    class Meta:
        model = SubirArchivo
        fields = ['name', 'file', 'tipo', 'detalles']
        labels = {
            'name': 'Nombre (utilice minúsculas y no tildes)',
            'file': 'Archivo',
            'tipo': 'Tipo de proyecto',
            'detalles': 'Detalles'
        }
    
    ## Inicializador de instancia SubirArchivosForm
    def __init__(self, *args, **kwargs):    
        
        ## Utilizar 
        super(SubirArchivoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['rows'] = 8