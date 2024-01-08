from rest_framework import serializers
from .models import menu_item, category, order
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
    menu_items = menu_item_serializer(many=True, read_only=True)

    class Meta:
        model = category
        fields = ["name", "name_lang", "menu_items"]


class order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = "__all__"
