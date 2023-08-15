from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from preprocesos import models as pm

from rest_framework.views import APIView


class getProjectNames(APIView):

    def get(self, request, *args, **kwargs):

        proyectos = pm.RawProjectQuasiTerreno.objects.all()
        proyectos = serializers.serialize('json', proyectos)

        return JsonResponse({'proyectos': proyectos})

class getDataProjects(APIView):

    def post(self, request, *args, **kwargs):

        print(request.POST.get('id'))

        try:

            data = pm.RawDataQuasiTerreno.objects.filter(project_id=request.POST.get('id'))
            data = serializers.serialize('json', data)

        except:

            data = None

        return JsonResponse({'data': data})