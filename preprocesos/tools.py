from django.contrib.auth.models import User
from django.contrib.gis.geos import GEOSGeometry



from dataentry.models import SubirArchivo

from .read import reader
from .cleaner import Limpiadores
from .joiner import Unificadores
from .intersecter import Intersectadores
from .models import RawDataQuasiTerreno, RawProjectQuasiTerreno, TypeRawProjectQuasi


class Herramientas:

    """
    Clase aunadora de módulos y creadora de productos
    """

    ## Constructor de aunadores por producto
    def aunar_producto(self, tool, *args):

        aunador = get_aunador(tool)

        aunador(args)

        return "Hecho!"


## Trae aunador según producto
def get_aunador(tool):
    
    ## Cuando se quieren unir gravedades relativas, gravedades absolutas
    ## y nivelaciones por cada tipo un archivo
    if tool == 1:

        return aunador_gravedades_relativa_absoluta_nivelacion


## Cuando se quieren unir gravedades relativas, gravedades absolutas
## y nivelaciones por cada tipo un archivo
def aunador_gravedades_relativa_absoluta_nivelacion(*args):

    ## Lee archivos de la carpeta /media
    largs = list(args[0])
    prjs = SubirArchivo.objects.filter(pk__in=largs)
    things = [reader(prj) for prj in prjs]

    ## Limpia horizontal y verticalmente iterando sobre archivos temporales leídos
    for thing in things:

        limpiador = Limpiadores()

        if thing.elipsoide.name == 'WGS 84' or thing.proyeccion == 'EPSG:4326':

            if thing.tipo == 'nivelacion':
                temp_df = limpiador.limpiar_verticalmente(thing, 'Tipo_Coord', select='CALCULADA')
                thing.set_df_file_tipo(temp_df, thing.file, thing.tipo)
                temp_df = limpiador.limpiar_horizontalmente(thing, 'Nomenclatu', 'Altura_m_s')
            
            elif thing.tipo == 'gravterrabs':
                temp_df = limpiador.limpiar_verticalmente(thing, 'OBS', select = 'N/A')
                thing.set_df_file_tipo(temp_df, thing.file, thing.tipo)
                temp_df = limpiador.limpiar_horizontalmente(thing, 'COD_IGAC_S', 'GRAV')

            elif thing.tipo == 'gravterrrel':
                temp_df = limpiador.limpiar_verticalmente(thing, 'Tipo_Coord', select='Calculada')
                thing.set_df_file_tipo(temp_df, thing.file, thing.tipo)
                temp_df = limpiador.limpiar_horizontalmente(thing, 'Nomenc', 'Grav_mGal')

            else:
                raise ValueError(f"El tipo {thing.tipo} es no soportado")
        
        else:
            raise ValueError(f"La proyección {thing.proyeccion} es desconocida")

        thing.set_df_file_tipo(temp_df, thing.file, thing.tipo)
    

    ## Unifica verticalmente gravedades
    unificador = Unificadores()
    grvs = unificador.unificar_verticalmente(things)
    
    ## Selecciona archivo de nivelación
    niv = [t for t in things if t.tipo == "nivelacion"]

    ## Intersecta gravedades unificadas y nivelación
    intersectador = Intersectadores()

    intersectado = intersectador.intersectar_nomenclatura(niv[0], grvs)

    ## Crea proyecto contenedor de metadatos para entradas del modelo
    ## quasigeoidal para observaciones en terreno
    rpqt = RawProjectQuasiTerreno()
    rpqt.user = User.objects.last()
    rpqt.proyecto = 'quasi-geoide'
    rpqt.tipo_proyecto = TypeRawProjectQuasi.objects.get(tipo='gravedades_nivelacion')
    rpqt.tipo_intersection = 'nomenclatura'
    rpqt.origen_coordenadas = 'nivelacion'
    rpqt.archivo_origen = intersectado['files']
    rpqt.save()

    ## Configuración para guardar dataframe en base de datos de postgresql
    size_lote = 100
    intctdf = intersectado['df'].values
    filas_totales = intctdf.shape[0]

    ## Guarda por lotes data frame en base de datos atada a proyecto contenedor
    ## de metadatos
    for i in range(0, filas_totales, size_lote):

        lote = intctdf[i:i+size_lote]

        objetos_modelo = [
            RawDataQuasiTerreno(posicion=GEOSGeometry(i[1].wkt),
                                nomenclatura=i[0],
                                elevacion=i[2],
                                gravedad=i[3],
                                project=RawProjectQuasiTerreno.objects.last()) for i in lote
                                ]
        
        RawDataQuasiTerreno.objects.bulk_create(objetos_modelo)

    return True