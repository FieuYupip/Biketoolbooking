from .serializers import ToolboxSerializers, BuildingSerializers
from rest_framework import generics
from ..models import Toolbox, Building

class ToolboxListView(generics.ListCreateAPIView):
    queryset = Toolbox.objects.all()
    serializer_class = ToolboxSerializers

class ToolboxDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toolbox.objects.all()
    serializer_class = ToolboxSerializers
    
