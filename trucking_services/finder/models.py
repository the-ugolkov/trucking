import re

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Cargo(models.Model):
    pick_up_location = models.ForeignKey('Location', related_name='pick_up_cargo_set', on_delete=models.CASCADE)
    delivery_location = models.ForeignKey('Location', related_name='delivery_cargo_set', on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description = models.TextField()

    def __str__(self):
        return f"{self.description[:50]}...   Из {self.pick_up_location.city} в {self.delivery_location.city}"


class Location(models.Model):
    city = models.CharField(max_length=123)
    state = models.CharField(max_length=123)
    zip = models.CharField(unique=True, max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.zip} | {self.city}, {self.state}"


class Car(models.Model):
    number = models.CharField(
        max_length=5,
        unique=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    payload = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

    def __str__(self):
        return f"{self.number}   Грузополъемность: {self.payload} кг. Локация: {self.location.city}"

    def clean(self):
        super().clean()
        if self.number:
            pattern = r'^\d{4}[A-Z]$'
            if not re.match(pattern, self.number):
                raise ValidationError("Номер должен быть в формате XXXXA, где X - цифра, A - заглавная буква")
