from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


class TypeRawProject(models.Model):

    """
    Tabla padre relacionadora de tipos y proyectos crudos
    """

    id = models.AutoField(primary_key=True)
    detalles = models.CharField(max_length=100, blank=False, default=None)

    class Meta:

        abstract=True
        unique_together = ('id', 'detalles')
        ordering = ('id')
        verbose_name = 'tipo padre para proyecto geodésico'
        verbose_name_plural = 'tipos padre para proyecto geodésico'


class TypeRawProjectQuasi(TypeRawProject):

    """
    Tabla hija relacionadora de proyectos para el modelo
    quasi-geoidal y sus tipos
    """

    TIPOS = [
        ('nivelacion', 'Nivelación'),
        ('gravterrabs', 'Gravedad terrestre absoluta'),
        ('gravterrrel', 'Gravedad terrestre relativa'),
        ('gravedades', 'Gravedades terrestres absolutas y relativas'),
    ]

    tipo = models.CharField(max_length=15, choices=TIPOS, unique=True)

    class Meta:
        verbose_name = 'tipo hijo del modelo quasi-geoidal'
        verbose_name_plural = 'tipos hijo del modelo quasi-geoidal'


class RawData(models.Model):

    """
    Tabla padre relacionadora de datos con proyectos geodeśicos
    """

    id = models.AutoField(primary_key=True)
    posicion = models.PointField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ('id',)
        verbose_name = 'modelo padre de datos para proyecto geodeśico'
        verbose_name_plural = 'modelos padre de datos para proyecto geodésico'
    

class RawDataQuasiTerreno(RawData):

    """
    Tabla hija relacionadora de datos terrestres crudos con proyectos crudos
    para el modelo quasi-geoidal
    """

    elevacion = models.DecimalField(max_digits=10, decimal_places=3)
    gravedad = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = 'modelo hijo terrestre de datos para el modelo quasi-geoidal'
        verbose_name_plural = 'modelos hijos terrestres de datos para el modelo quasi-geoidal'


class RawDataQuasiAerea(RawData):

    """
    Tabla hija relacionadora de datos aéreos crudos con proyectos crudos
    para el modelo quasi-geoidal
    """

    spring = models.DecimalField(max_digits=10, decimal_places=3)
    beam = models.DecimalField(max_digits=10, decimal_places=3)
    acc_hor = models.DecimalField(max_digits=10, decimal_places=3)
    acc_vert = models.DecimalField(max_digits=10, decimal_places=3)
    eotvos = models.DecimalField(max_digits=10, decimal_places=3)
    altitud = models.DecimalField(max_digits=10, decimal_places=3)
    # Agregar demás variables necesarias

    class Meta:
        verbose_name = 'modelo hijo terrestre de datos para el modelo quasi-geoidal'
        verbose_name_plural = 'modelos hijos terrestres de datos para el modelo quasi-geoidal'


class RawProject(models.Model):

    """
    Tabla padre relacionadora de proyectos crudos, sus tipos
    y sus datos
    """

    PROYECTOS = [
        ('quasi-geoide', 'Modelo Quasi-geoidal')
    ]

    id = models.AutoField(primary_key=True)
    proyecto = models.CharField(max_length=20, choices=PROYECTOS)
    
    class Meta:
        abstract = True
        ordering = ('id',)
        verbose_name = 'proyecto padre para proyecto geodésico'
        verbose_name_plural = 'proyectos padre para proyecto geodésico'


class RawProjectQuasiTerreno(RawProject):
    
    """
    Tabla hija relacionadora de proyectos crudos terrestres para el modelo
    quasi-geoidal, sus tipos y datos
    """

    TIPO_INTERSECCION = [
        ('original', 'Original'),
        ('nomenclatura', 'Por nomenclatura'),
        ('coordenadas', 'Por coordenadas'),
        ]

    user = models.ForeignKey(
        User,
        related_name='proyectos_crudos_quasigeodales_terreno',
        on_delete=models.PROTECT
    )
    data = models.ForeignKey(
        RawDataQuasiTerreno,
        related_name='proyectos_crudos_quasi_geoidales',
        on_delete=models.CASCADE,
        blank=True,
    )
    tipo_intersection = models.CharField(max_length=20, choices=TIPO_INTERSECCION, default='original')

    class Meta:
        verbose_name = 'proyecto hijo terrestre crudo para el modelo quasi-geoidal'
        verbose_name_plural = 'proyectos hijos terrestres crudos para el modelo quasi-geoidal'


class RawProjectQuasiAerea(RawProject):
    
    """
    Tabla hija relacionadora de proyectos crudos terrestres para el modelo
    quasi-geoidal, sus tipos y datos
    """
    
    user = models.ForeignKey(
        User,
        related_name='proyectos_crudos_quasigeodales_aerea',
        on_delete=models.PROTECT
    )
    data = models.ForeignKey(
        RawDataQuasiAerea,
        related_name='proyectos_crudos_quasi_geoidales',
        on_delete=models.CASCADE,
        blank=True,
    )

    class Meta:
        verbose_name = 'proyecto hijo terrestre crudo para el modelo quasi-geoidal'
        verbose_name_plural = 'proyectos hijos terrestres crudos para el modelo quasi-geoidal'