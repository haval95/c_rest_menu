from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, permissions, status

from .models import category, menu_item, order
from .serializers import (
    category_serializer,
    menu_item_serializer,
    order_Serializer,
)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class category_view(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = category_serializer


class single_category_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = category_serializer


class create_order_view(generics.ListCreateAPIView):
    queryset = order.objects.all()
    serializer_class = order_Serializer
