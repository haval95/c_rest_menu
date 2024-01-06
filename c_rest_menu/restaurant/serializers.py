from rest_framework import serializers
from .models import menu_item, category, order, ordered_item
from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["url", "username", "email", "groups"]


class menu_item_serializer(serializers.ModelSerializer):
    class Meta:
        model = menu_item
        fields = "__all__"


class category_serializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = "__all__"


class orderd_item_serializer(serializers.ModelSerializer):
    class Meta:
        model = ordered_item
        fields = "__all__"


class order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = "__all__"


# class menu_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         fields = "__all__"


# class booking_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = "__all__"
