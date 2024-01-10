from rest_framework import serializers
from .models import Reservation, Table
from datetime import timedelta


class table_serializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class reservation_serializer(serializers.ModelSerializer):
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), source="table", write_only=True
    )
    table = table_serializer(read_only=True)

    class Meta:
        model = Reservation
        fields = "__all__"
