from django.db import models
from django.utils import timezone

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=50)
    no_guests = models.IntegerField()
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} : {str(self.no_guests)}"

    def get_item(self):
        return f"{self.name} : {str(self.no_guests)}"


class Menu(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    ingriediant = models.CharField(max_length=200)
