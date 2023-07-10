from django.contrib.auth.models import User
from django.db import models

"""
Modelos crudos
"""

class SubirArchivo(models.Model):

    """
    Clase para modelar datos crudos
    """

    OPCIONES = [
        ('nivelacion', 'Nivelación'),
        ('gravterrabs', 'Gravedad terrestre absoluta'),
        ('gravterrabs', 'Gravedad terrestre relativa'),
        ('gravedades', 'Gravedades terrestres absolutas y relativas'),
    ]

    user = models.ForeignKey(
        User,
        related_name='subir_archivos',
        on_delete=models.PROTECT
    )
    
    ## Variables necesarias para entender el archivo
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to='media/')
    tipo = models.CharField(max_length=20, choices=OPCIONES)
    detalles = models.CharField(max_length=250)

    class Meta:
        ## Ordenar por
        ordering = ('-id',)

    ## Guardar el archivo temporal
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    ## Definición para la función print
    def __str__(self):
        return f"Archivo {self.name} de tipo {self.tipo}, proveniente del archivo {self.file}"