from django.urls import path

from .views import (
    category_view,
    single_category_view,
    create_order_view,
)

urlpatterns = [
    path("categories/", category_view.as_view(), name="category_view"),
    path(
        "categories/<int:pk>",
        single_category_view.as_view(),
        name="single_category_view",
    ),
    path("order/", create_order_view.as_view(), name="order_view"),
]
