from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=50)
    no_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now=True)


class Menu(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    ingriediant = models.CharField(max_length=200)
