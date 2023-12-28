from django.urls import path
from .views import booking_view, menu_view, single_menu_item, single_booking_item

urlpatterns = [
    path("bookings/", booking_view.as_view(), name="booking_view"),
    path("menu/", menu_view.as_view(), name="menu_view"),
    path("menu/<int:pk>/", single_menu_item.as_view(), name="single_menu_view"),
    path(
        "bookings/<int:pk>/", single_booking_item.as_view(), name="single_booking_view"
    ),
]
