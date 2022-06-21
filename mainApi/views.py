from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serialisers import PlantSerializer
from .models import Plant

from .serialisers import TaskSerializer
from .models import Task

from .serialisers import ProfileSerializer
from .models import Profile

from .serialisers import UserSerializer
from .models import User

from .serialisers import MetricsSerializer
from .models import HouseMetrics

from .serialisers import SensorsBoxSerializer
from .models import SensorsBox


class PlantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def get_queryset(self):
        plant_id = self.request.query_params.get('plant_id')
        # get specific plant
        if plant_id:
            res = self.queryset.filter(id=plant_id)
        # retrieve user plant lit
        else:
            res = self.queryset.filter(user=self.request.user)
        # return result
        return res


class TaskViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        plant_id = self.request.query_params.get('task_id')
        # get specific plant
        if plant_id:
            res = self.queryset.filter(id=plant_id)
        # retrieve user plant lit
        else:
            res = self.queryset.filter(user=self.request.user)
        # return result
        return res


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('email')
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class MetricsViewSet(viewsets.ModelViewSet):
    queryset = HouseMetrics.objects.all()
    serializer_class = MetricsSerializer


class SensorBoxViewSet(viewsets.ModelViewSet):
    queryset = SensorsBox.objects.all()
    serializer_class = SensorsBoxSerializer
