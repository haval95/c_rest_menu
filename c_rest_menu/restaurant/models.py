from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)
    name_lang = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.name


class Menu_item(models.Model):
    name = models.CharField(max_length=35)
    name_lang = models.CharField(max_length=35, default=None)
    describtion = models.CharField(max_length=100)
    describtion_lang = models.CharField(max_length=100, default=None)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category_id = models.ForeignKey(
        Category,
        related_name="menu_items",
        on_delete=models.CASCADE,
    )

    img = models.ImageField(blank=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    customer_id = models.ForeignKey(
        User, related_name="order_user", on_delete=models.CASCADE, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total_order_before_discount = models.DecimalField(
        max_digits=8, decimal_places=2, default=0
    )
    discount = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(limit_value=0),
            MaxValueValidator(limit_value=100),
        ],
    )
    total_order_after_discount = models.DecimalField(
        max_digits=8, decimal_places=2, default=0
    )
    status = models.BooleanField(default=False)


class Ordered_item(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="ordered_items"
    )
    menu_item = models.ForeignKey(Menu_item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField(null=True)
    total_price = models.PositiveIntegerField(null=True)


class Cart(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    menu_item = models.ForeignKey(Menu_item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.PositiveIntegerField(null=True)
    total_price = models.PositiveIntegerField(null=True)
