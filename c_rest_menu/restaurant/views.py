from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, permissions, status

from .models import category, menu_item, order
from .serializers import (
    category_serializer,
    menu_item_serializer,
    order_Serializer,
    orderd_item_serializer,
)
from rest_framework.permissions import IsAuthenticated


class category_view(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = category_serializer


class single_category_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = category_serializer


class order_view(generics.ListCreateAPIView):
    queryset = order.objects.all()
    serializer_class = order_Serializer
