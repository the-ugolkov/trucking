import string
import random

from django.core.management.base import BaseCommand

from finder.models import Car, Location


def generate_random_letter():
    return random.choice(string.ascii_uppercase)


def get_random_location():
    count = Location.objects.count()
    if count > 0:
        random_index = random.randint(0, count - 1)
        random_location = Location.objects.all()[random_index]
        return random_location
    else:
        return None


class Command(BaseCommand):
    help = 'Creation of 20 cars'

    def handle(self, *args, **options):
        for i in range(20):
            car = Car()
            car.number = ''.join(str(random.randint(1000, 9999))) + generate_random_letter()
            car.payload = random.randint(1, 1000)
            car.location = get_random_location()

            car.save()

        self.stdout.write(self.style.SUCCESS('Cars successfully created'))