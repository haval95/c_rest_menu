from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=25)
    name_lang = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.name


class menu_item(models.Model):
    name = models.CharField(max_length=35)
    name_lang = models.CharField(max_length=35, default=None)
    describtion = models.CharField(max_length=100)
    describtion_lang = models.CharField(max_length=100, default=None)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category_id = models.ForeignKey(
        category,
        related_name="menu_items",
        on_delete=models.CASCADE,
    )

    img = models.ImageField(blank=True)

    def __str__(self) -> str:
        return self.name


class order(models.Model):
    customer_id = models.ForeignKey(
        User,
        related_name="User",
        on_delete=models.CASCADE,
    )
    time = models.DateTimeField(auto_now_add=True)
    total_order_b4_discount = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(limit_value=0),
            MaxValueValidator(limit_value=100),
        ],
    )
    total_order_after_discount = models.DecimalField(max_digits=8, decimal_places=2)


class ordered_item(models.Model):
    order_id = models.ForeignKey(order, related_name="order", on_delete=models.CASCADE)
    item_id = models.ForeignKey(
        menu_item, related_name="menu_item", on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.item_id.name


# class Booking(models.Model):
#     name = models.CharField(max_length=50)
#     no_guests = models.IntegerField()
#     booking_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.name} : {str(self.no_guests)}"

#     def get_item(self):
#         return f"{self.name} : {str(self.no_guests)}"


# class Menu(models.Model):
#     title = models.CharField(max_length=50)
#     price = models.DecimalField(decimal_places=2, max_digits=6)
#     ingriediant = models.CharField(max_length=200)
