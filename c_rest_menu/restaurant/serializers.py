from rest_framework import serializers
from .models import Menu_item, Category, Order, Ordered_item, Cart, CartItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class menu_item_serializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_item
        fields = "__all__"


class category_serializer(serializers.ModelSerializer):
    menu_items = menu_item_serializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["name", "name_lang", "menu_items"]


class CartItemSerializer(serializers.ModelSerializer):
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=Menu_item.objects.all(), source="menu_item", write_only=True
    )
    menu_item = menu_item_serializer(read_only=True)

    class Meta:
        model = CartItem
        fields = [
            "id",
            "menu_item",
            "quantity",
            "unit_price",
            "menu_item_id",
            "total_price",
        ]

    def create(self, validated_data):
        # Get the menu_item and quantity from the validated data
        menu_item = validated_data["menu_item"]
        quantity = 1
        if "quantity" in self.context["request"].data:
            quantity = validated_data["quantity"]
        # Get the current user
        user = self.context["request"].user

        # Try to retrieve the user's existing cart
        cart = Cart.objects.filter(customer_id=user).first()

        if cart:
            # Check if a CartItem with the same menu_item exists in the cart
            cart_item = CartItem.objects.filter(cart=cart, menu_item=menu_item).first()

            if cart_item:
                # If the CartItem exists, update the quantity
                cart_item.quantity += quantity
                cart_item.total_price = cart_item.quantity * cart_item.unit_price
                cart_item.save()
            else:
                # If the CartItem does not exist, create a new one
                cart_item = CartItem.objects.create(
                    cart=cart,
                    menu_item=menu_item,
                    quantity=quantity,
                    unit_price=menu_item.price,
                    total_price=menu_item.price * quantity,
                )

        else:
            # If the cart doesn't exist, create a new cart and add the item to it
            cart = Cart.objects.create(customer_id=user)
            cart_item = CartItem.objects.create(
                cart=cart,
                menu_item=menu_item,
                quantity=quantity,
                unit_price=menu_item.price,
                total_price=menu_item.price * quantity,
            )

        return cart_item


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class ordered_item_serializer(serializers.ModelSerializer):
    menu_item = menu_item_serializer()

    class Meta:
        model = Ordered_item
        fields = [
            "id",
            "menu_item",
            "quantity",
        ]


class order_Serializer(serializers.ModelSerializer):
    customer_id = UserSerializer()
    order_items = ordered_item_serializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
