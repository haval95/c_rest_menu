from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, permissions, status

# from .models import Booking, Menu
from .serializers import booking_serializer, menu_serializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


# # Create your views here.
# class booking_view(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = booking_serializer


# class single_booking_item(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = booking_serializer


# class menu_view(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = menu_serializer
#     permission_classes = [IsAuthenticated]


# class single_menu_item(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = menu_serializer
