from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serialisers import PlantSerializer
from .models import Plant

from .serialisers import ProfileSerializer
from .models import Profile

from .serialisers import UserSerializer
from .models import User


class PlantViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def get_queryset(self):
        plant_id = self.request.query_params.get('plant_id')
        # get specific plant
        if plant_id:
            self.queryset.filter(id=plant_id)
        # retrieve user plant lit
        else:
            self.queryset.filter(user=self.request.user.id)
        return self.queryset


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('email')
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
