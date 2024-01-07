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
    menu_items = menu_item_serializer(many=True, read_only=True)

    class Meta:
        model = category
        fields = ["name", "name_lang", "menu_items"]


class orderd_item_serializer(serializers.ModelSerializer):
    item_id = menu_item_serializer(read_only=True)

    class Meta:
        model = ordered_item
        fields = ["quantity", "sub_total", "item_id"]


class order_Serializer(serializers.ModelSerializer):
    order_item = orderd_item_serializer(many=True, read_only=True)

    class Meta:
        model = order
        fields = [
            "customer_id",
            "time",
            "total_order_before_discount",
            "order_item",
        ]
