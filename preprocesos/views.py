from django.shortcuts import render
from dataentry.models import SubirArchivo
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, csrf_exempt


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

        print(request.body)

        return JsonResponse({'message': 'Llegó'})
    
    else:

        return JsonResponse({'message': request.method})



def intersecar_grv_niv(request, *args, **kwargs):
    pass


def unir_gravedades(request, *args, **kwargs):
    pass