from rest_framework import serializers
from .models import SubirArchivo


class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubirArchivo
        fields = ('id', 'file')