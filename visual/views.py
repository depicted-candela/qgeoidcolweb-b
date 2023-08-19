from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from rest_framework.views import APIView

from preprocesos import models as pm

import json


class getProjectNames(APIView):

    def get(self, request, *args, **kwargs):

        proyectos = pm.RawProjectQuasiTerreno.objects.all()
        proyectos = serializers.serialize('json', proyectos)

        return JsonResponse({'proyectos': proyectos})

class getDataProjects(APIView):

    def post(self, request, *args, **kwargs):

        try:

            var = json.loads(request.body.decode('utf-8'))['id']
            data = pm.RawDataQuasiTerreno.objects.filter(project_id__in=var)
            data = serializers.serialize('json', data)

        except:

            data = None

        return JsonResponse({'data': data})