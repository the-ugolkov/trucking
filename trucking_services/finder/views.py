from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from finder.models import Location, Cargo
from finder.serializers import CargoSerializer


class CargoCreateView(APIView):
    def post(self, request):
        zip_pick_up = request.data.get('zip_pick_up')
        zip_delivery = request.data.get('zip_delivery')
        weight = request.data.get('weight')
        description = request.data.get('description')

        pick_up_location = get_object_or_404(Location, zip=zip_pick_up)
        delivery_location = get_object_or_404(Location, zip=zip_delivery)

        cargo = Cargo.objects.create(
            pick_up_location=pick_up_location,
            delivery_location=delivery_location,
            weight=weight,
            description=description
        )

        serializer = CargoSerializer(cargo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)