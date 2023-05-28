from celery import shared_task

from finder.management.commands.create_cars import get_random_location
from finder.models import Car


@shared_task
def update_cars_location():
    cars = Car.objects.all()

    for car in cars:
        car.location = get_random_location()
        car.save()