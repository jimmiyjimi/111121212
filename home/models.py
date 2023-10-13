from django.db import models

from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_info = models.CharField(max_length=1000, default='short info')
    year = models.IntegerField()
    main_photo = models.ImageField(upload_to='taciki/', default='default_photo.jpg')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='car_photos/')

# Create your models here.
