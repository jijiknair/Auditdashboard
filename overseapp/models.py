
from django.contrib.auth.models import User
from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    rent_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='office_images/')

    def __str__(self):
        return self.name