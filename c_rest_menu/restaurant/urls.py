from django.urls import path

from .views import category_view, single_category_view

urlpatterns = [
    path("categories/", category_view.as_view(), name="category_view"),
    path(
        "categories/<int:pk>",
        single_category_view.as_view(),
        name="single_category_view",
    ),
    # path("bookings/", booking_view.as_view(), name="booking_view"),
    # path("menu/", menu_view.as_view(), name="menu_view"),
    # path("menu/<int:pk>/", single_menu_item.as_view(), name="single_menu_view"),
    # path(
    #     "bookings/<int:pk>/", single_booking_item.as_view(), name="single_booking_view"
    # ),
]
