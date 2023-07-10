from django.forms.models import model_to_dict
from django.shortcuts import render
from dataentry.models import SubirArchivo
from django.http import JsonResponse

# Create your views here.
def prjs_terrestres(request, *args, **kwargs):

    return render(request, "preprocesos/prjs_terrestres.html")

# Mostrar projectos de la base de datos
def mostrar_prjs_terr(request, *args, **kwargs):

    archs = SubirArchivo.objects.all()

    dicts = {arch.id: [arch.name, arch.detalles] for arch in archs}

    return JsonResponse(dicts)