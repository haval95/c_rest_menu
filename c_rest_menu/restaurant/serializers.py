from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class menu_serializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class booking_serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
