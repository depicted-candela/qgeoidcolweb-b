from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from dataentry.models import SubirArchivo

from .tools import Herramientas


class CsrfTokenView(APIView):

    """Send to the login interface the token CSRF as a cookie."""

    def get(self, request, *args, **kwargs) -> Response:

        csrf_token = get_token(request)

        return Response(csrf_token)


# Template de proyectos de terreno
def prjs_terr(request, *args, **kwargs):

    return render(request, "preprocesos/prjs_terrestres.html")


# Mostrar projectos de la base de datos
def mostrar_prjs_terr(request, *args, **kwargs):

    if request.method == 'GET':

        archs = SubirArchivo.objects.all()

        ser_data = serializers.serialize('json', archs)

        return JsonResponse({'prjs': ser_data})


class RecibirInfoPreprocess(APIView):

    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def post(self, request, *args, **kwargs):

        tool = int(request.POST.get("tool"))
        items = request.POST.get("item").split(',')
        items = [int(i) for i in items]

        herramientas = Herramientas()
        hr = herramientas.aunar_producto(tool, *items)

        return JsonResponse({'message': 'Hecho'})


## Recibir información para preprocesar archivos subidos a /media
@csrf_exempt
def recibir_info_preprocess(self, request, *args, **kwargs):

    if request.method == "POST":

        tool = request.POST.get("tool")
        name = request.POST.get("item")

        return JsonResponse({'message': 'Hecho!'})
