from rest_framework import serializers
from ..models import Toolbox, Building

class ToolboxSerializers(serializers.ModelSerializer):
    class Meta:
        model = Toolbox
        fields =['id', 'building', "Rent_status"]

class BuildingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['Adress']