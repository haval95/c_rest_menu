from django.urls import path
from .views import booking_view, menu_view

urlpatterns = [
    path("bookings/", booking_view.as_view(), name="booking_view"),
    path("menu/", menu_view.as_view(), name="menu_view"),
]
