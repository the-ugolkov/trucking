import random
import re
import string

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def generate_random_letter():
    return random.choice(string.ascii_uppercase)


class Cargo(models.Model):
    pick_up_location = models.ForeignKey('Location', related_name='pick_up_cargo_set', on_delete=models.CASCADE)
    delivery_location = models.ForeignKey('Location', related_name='delivery_cargo_set', on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description = models.TextField()


class Location(models.Model):
    city = models.CharField(max_length=123)
    state = models.CharField(max_length=123)
    zip = models.CharField(unique=True, max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Car(models.Model):
    number = models.CharField(
        max_length=5,
        unique=True,
        default=''.join(str(random.randint(1000, 9999))) + generate_random_letter())
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    payload = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

    def clean(self):
        super().clean()
        if self.number:
            pattern = r'^\d{4}[A-Z]$'
            if not re.match(pattern, self.number):
                raise ValidationError("Номер должен быть в формате XXXXA, где X - цифра, A - заглавная буква")

    # def save(self, *args, **kwargs):
    #     if not self.location:
    #         locations = Location.objects.all()
    #         if locations:
    #             self.location = random.choice(locations)
    #     super().save(*args, **kwargs)