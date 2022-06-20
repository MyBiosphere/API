from rest_framework import serializers

from .models import Plant
from .models import Profile
from .models import User
from .models import HouseMetrics
from .models import SensorsBox


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'user', 'room']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'email', 'plants')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class MetricsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HouseMetrics
        fields = ('id', 'box', 'co2', 'temperature', 'humidity')


class SensorsBoxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorsBox
        fields = ('id', 'user', 'boxNumber')
