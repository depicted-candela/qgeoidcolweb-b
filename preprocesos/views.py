from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.gis.geos import GEOSGeometry

from dataentry.models import SubirArchivo

from .read import reader
from .cleaner import Limpiadores
from .joiner import Unificadores
from .intersecter import Intersectadores
from .models  import RawDataQuasiTerreno, RawProjectQuasiTerreno, TypeRawProjectQuasi

import json


# Crea el token necesario para la seguridad del usuario
def get_csrf_token(request):

    if request.method == "GET":

        csrf_token = get_token(request)

        return JsonResponse({'csrfToken': csrf_token})


# Template de proyectos de terreno
def prjs_terr(request, *args, **kwargs):

    return render(request, "preprocesos/prjs_terrestres.html")


# Mostrar projectos de la base de datos
def mostrar_prjs_terr(request, *args, **kwargs):

    if request.method == 'GET':

        archs = SubirArchivo.objects.all()
        ser_data = serializers.serialize('json', archs)

        return JsonResponse({'prjs': ser_data})


# Recibir datos de la aplicación front-end
@csrf_exempt
def rcbr_args_prjs_trr(request):

    if request.method == 'POST':

        raw = json.loads(request.body)
        data = raw['data']
        ids = [d['pk'] for d in data]
        prjs = SubirArchivo.objects.filter(pk__in=ids)
        things = [reader(prj) for prj in prjs]

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
        
        unificador = Unificadores()
        grvs = unificador.unificar_verticalmente(things)
        
        intersectador = Intersectadores()
        intersectado = intersectador.intersectar_nomenclatura(things[2], grvs)

        intctdf = intersectado['df']
        files = intersectado['files']

        tp = TypeRawProjectQuasi.objects.get(tipo='gravedades_nivelacion')

        rpqt = RawProjectQuasiTerreno()
        rpqt.user = User.objects.last()
        rpqt.proyecto = 'quasi-geoide'
        rpqt.tipo_proyecto = tp
        rpqt.tipo_intersection = 'nomenclatura'
        rpqt.origen_coordenadas = 'nivelacion'
        rpqt.archivo_origen = files
        rpqt.save()

        last_rpqt = RawProjectQuasiTerreno.objects.last()

        intctdf = intctdf.values

        size_lote = 100
        filas_totales = intctdf.shape[0]

        for i in range(0, filas_totales, size_lote):

            lote = intctdf[i:i+size_lote]

            objetos_modelo = [
                RawDataQuasiTerreno(posicion=GEOSGeometry(i[1].wkt),
                                    nomenclatura=i[0],
                                    elevacion=i[2],
                                    gravedad=i[3],
                                    project=last_rpqt) for i in lote
                                    ]
            
            RawDataQuasiTerreno.objects.bulk_create(objetos_modelo)

        print("Hecho!")

        return JsonResponse({'message': 'Llegó'})

    else:

        return JsonResponse({'message': request.method})


def intersecar_grv_niv(request, *args, **kwargs):
    pass


def unir_gravedades(request, *args, **kwargs):
    pass