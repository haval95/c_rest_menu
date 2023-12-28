from rest_framework import serializers
from .models import Menu, Booking


class menu_serializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        feilds = "__all__"


class booking_serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        feilds = "__all__"
