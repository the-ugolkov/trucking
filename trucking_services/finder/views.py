from geopy.distance import distance
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from finder.models import Location, Cargo, Car
from finder.serializers import CargoSerializer, CarSerializer


def get_nearby_cars(cargo, max_distance=450):
    cargo_coordinates = (cargo.pick_up_location.latitude, cargo.pick_up_location.longitude)
    nearby_cars = Car.objects.filter(payload__gt=cargo.weight)
    result = []

    for car in nearby_cars:
        car_coordinates = (car.location.latitude, car.location.longitude)
        dist = distance(cargo_coordinates, car_coordinates).miles
        if dist <= int(max_distance):
            result.append(car)
    return result


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


class CargoUpdateView(APIView):
    def put(self, request, pk):
        weight = request.data.get('weight')
        description = request.data.get('description')

        cargo = get_object_or_404(Cargo, id=pk)

        cargo.weight = weight
        cargo.description = description
        cargo.save()

        serializer = CargoSerializer(cargo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        cargo = get_object_or_404(Cargo, id=pk)

        cargo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CargoListView(APIView):
    def get(self, request):
        min_weight = request.GET.get('min_weight') if 'min_weight' in request.GET else '1'
        max_weight = request.GET.get('max_weight') if 'max_weight' in request.GET else '1000'
        max_distance = request.GET.get('max_distance') if 'max_distance' in request.GET else '450'

        cargos = Cargo.objects.all()
        if min_weight:
            cargos = cargos.filter(weight__gte=min_weight)
        if max_weight:
            cargos = cargos.filter(weight__lte=max_weight)

        cargo_data = []
        for cargo in cargos:
            nearby_cars = get_nearby_cars(cargo, max_distance)

            serializer = CargoSerializer(cargo)
            filtered_data = {key: value for key, value in serializer.data.items() if key in ['pick_up_location',
                                                                                             'delivery_location']}

            cargo_data.append({
                'cargo': filtered_data,
                'nearby_cars_count': len(nearby_cars)
            })

        return Response(cargo_data)


class CargoDetailView(APIView):
    def get(self, request, pk):
        cargo = get_object_or_404(Cargo, id=pk)
        nearby_cars = get_nearby_cars(cargo)
        nearby_cars_numbers = [car.number for car in nearby_cars]

        serializer = CargoSerializer(cargo)

        return Response({'cargo_data': serializer.data, 'nearby_cars_numbers': nearby_cars_numbers},
                        status=status.HTTP_200_OK)


class CarUpdateView(APIView):
    def put(self, request, pk):
        zip = request.data.get('zip')

        car = get_object_or_404(Car, id=pk)
        location = get_object_or_404(Location, zip=zip)

        car.location = location
        car.save()

        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
