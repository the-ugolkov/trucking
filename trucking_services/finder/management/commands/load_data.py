import csv
from django.core.management.base import BaseCommand
from finder.models import Location

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                location = Location()
                location.zip = row['zip']
                location.latitude = row['lat']
                location.longitude = row['lng']
                location.city = row['city']
                location.state = row['state_name']

                location.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
