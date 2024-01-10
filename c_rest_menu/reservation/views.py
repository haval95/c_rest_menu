from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Reservation
from .serializers import reservation_serializer
from datetime import timedelta


class reserve_view(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = reservation_serializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check for custom validation before saving
        table = serializer.validated_data["table"]
        reservation_time = serializer.validated_data["reservation_time"]
        for_how_long = serializer.validated_data.get("for_how_long", timedelta(hours=1))

        overlapping_reservations = Reservation.objects.filter(
            table=table,
            reservation_time__lt=reservation_time + for_how_long,
            reservation_time__gt=reservation_time,
        ).exclude(id=serializer.validated_data.get("id", None))

        if overlapping_reservations.exists():
            return Response(
                {
                    "error": "This reservation conflicts with existing reservations for the same table and time."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
