from rest_framework.serializers import ModelSerializer

from finder.models import Cargo, Location, Car


class CargoSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'