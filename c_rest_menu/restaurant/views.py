from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, status

from .models import Category, Menu_item, Order, Ordered_item, Cart, CartItem
from .serializers import (
    category_serializer,
    menu_item_serializer,
    order_Serializer,
    ordered_item_serializer,
    CartItemSerializer,
)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class category_view(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = category_serializer


class single_category_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = category_serializer


class create_order_view(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = order_Serializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Get the current user
        user = self.request.user

        try:
            cart = Cart.objects.get(customer_id=user)
        except Cart.DoesNotExist:
            return Response(
                {"message": "Cart is empty"}, status=status.HTTP_404_NOT_FOUND
            )

        # Create the order
        order = Order.objects.create(customer_id=user)

        # Get the cart items and create order items based on them
        cart_items = cart.items.all()
        order_items = []
        total = 0
        for cart_item in cart_items:
            order_item = Ordered_item.objects.create(
                order=order,
                menu_item=cart_item.menu_item,
                quantity=cart_item.quantity,
                unit_price=cart_item.unit_price,
                total_price=cart_item.total_price,
            )
            total += cart_item.total_price

            order_items.append(order_item)
        order.total_order_before_discount = total

        discount_value = request.data.get("discount")

        if (
            len(discount_value)
            and not isinstance(discount_value, str)
            and int(discount_value)
            and 0 <= int(discount_value) <= 100
        ):
            order.discount = int(discount_value)
            order.total_order_after_discount = total * (
                (100 - int(discount_value)) / 100
            )
        else:
            order.total_order_after_discount = total

        order.save()

        # Delete the cart
        cart.delete()

        # Serialize the order and order items
        serializer = self.get_serializer(order)
        data = serializer.data
        data["ordered_items"] = ordered_item_serializer(order_items, many=True).data

        return Response(data)


class CartItemView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
