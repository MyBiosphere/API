from rest_framework import serializers

from .models import Plant
from .models import Profile
from .models import User
from .models import HouseMetrics
from .models import SensorsBox
from .models import Task


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'room',
                  'status', 'watering', 'sunshine', 'repot', 'blooming_time', 'picture',
                  'user'
                  ]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # plant_name = serializers.CharField(source='plant.name')
    plant_name = serializers.ReadOnlyField()
    plant_id = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'done',
                  'user',
                  'plant_related', 'plant', 'plant_name', 'plant_id',
                  'sensor'
                  ]


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
        fields = ('id', 'box_id', 'date', 'soil_humidity', 'fine_particle', 'co2', 'temperature', 'humidity')


class SensorsBoxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorsBox
        fields = ('id', 'user', 'boxNumber')
