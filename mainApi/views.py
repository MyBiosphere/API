from rest_framework import viewsets

from .serialisers import PlantSerializer
from .models import Plant


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('name')
    serializer_class = PlantSerializer
