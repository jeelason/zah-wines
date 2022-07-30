from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Wine(models.Model):
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(2030), MinValueValidator(1900)]
    )
    varietal = models.CharField(max_length=75)
    location = models.CharField(max_length=70)
    tech_sheet = models.URLField(blank=True)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.varietal}"


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.full_name} + {self.email}'


class Consultant(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.full_name} + {self.email}'
