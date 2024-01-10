from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.


class Table(models.Model):
    number = models.IntegerField(unique=True)
    number_seats = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"Table: {self.number} Seats: {self.number_seats}"


class Reservation(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="reserved_table"
    )
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    for_how_long = models.DurationField(default=timedelta(hours=1))
    status = models.CharField(
        max_length=20,
        choices=[
            ("confirmed", "Confirmed"),
            ("pending", "Pending"),
            ("canceled", "Canceled"),
        ],
        default="pending",
    )

    class Meta:
        unique_together = ("table", "reservation_time")
