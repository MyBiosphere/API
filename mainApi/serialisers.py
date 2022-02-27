from rest_framework import serializers

from .models import Plant


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'description')
