from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Booking, Menu
from .serializers import booking_serializer, menu_serializer


# Create your views here.
class booking_view(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = booking_serializer


class menu_view(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menu_serializer
